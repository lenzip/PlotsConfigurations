#!/usr/bin/env python

import os
import sys
import math
import tempfile
import subprocess
import resource
import ROOT
import numpy as np
import root_numpy as rnp

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binning

ws_dir = sys.argv[1] # directory where workspace and other fit result files are
observable = sys.argv[2] # name of the observable
sr = sys.argv[3] # name of the signal region bin to shift (e.g. PTH_0_20)
try:
    dnscale = float(sys.argv[4]) # signal content in the bin will be shifted by sqrt(original signal) * dnscale
except IndexError:
    dnscale = 1.

mus = ['r_%d' % i for i in range(len(binning.bins[observable]))]

if observable == 'ptH':
    delta = '2.5'
elif observable == 'njet':
    delta = '9.52'

def get_counts(workspace):
    """
    Add up (over all categories) the integrals of reco-level bin sr
    """

    model = workspace.pdf('model_s')
    x = workspace.var('CMS_th1x')
    xset = ROOT.RooArgSet(x)
    ch = workspace.cat('CMS_channel')
    
    count = 0.
    
    for index in range(ch.numBins('')):
        ch.setBin(index)
        bin_name = ch.getLabel()
    
        if '_CR_' in bin_name:
            continue
    
        if sr not in bin_name:
            continue
    
        func = workspace.arg('prop_bin%s' % bin_name)
        integ = func.createIntegral(xset)
        count += integ.getVal()

    return count


# Pick up the best-fit asimov dataset

path = '%s/higgsCombineBestFitUnregAsimov.GenerateOnly.mH120.root' % ws_dir
source = ROOT.TFile.Open(path)
asimov_s = source.Get('toys/toy_asimov')
source.Close()

path = '%s/higgsCombineBestFitUnregAsimovBkgOnly.GenerateOnly.mH120.root' % ws_dir
source = ROOT.TFile.Open(path)
asimov_b = source.Get('toys/toy_asimov')
source.Close()

# Signal contribution in the Asimov dataset in the signal region bin sr
n = 0.
for nd in range(asimov_s.numEntries()):
    point = asimov_s.get(nd)
    bin_name = point.find('CMS_channel').getLabel()
    
    if '_CR_' in bin_name or sr not in bin_name:
        continue

    asimov_b.get(nd)

    n += asimov_s.weight() - asimov_b.weight()

# Compute the best-fit (to the Asimov dataset) signal yield

ws_path = '%s/higgsCombineAltReg_BestFitUnregAsimov.MultiDimFit.mH120.root' % ws_dir

muhat = np.array(tuple(rnp.root2array(ws_path, 'limit', mus)[0]))

source = ROOT.TFile.Open(ws_path)
workspace = source.Get('w')
source.Close()

workspace.loadSnapshot('MultiDimFit')

# integral with best-fit mu values
nuhat = get_counts(workspace)

for mu in mus:
    workspace.var(mu).setVal(0.)

# integral with mu = 0
bkghat = get_counts(workspace)

nuhat -= bkghat

# Create a new dataset with signal content in one reco-level bin scaled by (1 + sqrt(n) * dnscale / n)

new_data = asimov_s.emptyClone()

dn = math.sqrt(n) * dnscale
reldn = dn / n

for nd in range(asimov_s.numEntries()):
    point_s = asimov_s.get(nd)
    bin_name = point_s.find('CMS_channel').getLabel()
    weight = asimov_s.weight()
    if sr in bin_name:
        asimov_b.get(nd)
        weight += (weight - asimov_b.weight()) * reldn

    new_data.add(point_s, weight)

with tempfile.NamedTemporaryFile(suffix='.root', delete=False) as tfile:
    tmpname = tfile.name

output = ROOT.TFile.Open(tmpname, 'recreate')
new_data.Write('data_obs')
output.Close()

cmd = ['combine', '%s/fullmodel.root' % ws_dir]
cmd += ['-M', 'MultiDimFit', '--algo', 'none']
cmd += ['--setParameters', 'regularize=1,delta=%s' % delta]
cmd += ['--X-rtd', 'MINIMIZER_analytic']
cmd += ['-D', '%s:data_obs' % tmpname]
proc = subprocess.Popen(cmd)
proc.communicate()

os.unlink(tmpname)

outname = 'higgsCombineTest.MultiDimFit.mH120.root'

# dmu = mu values from the fit to the perturbed dataset - mu values from the fit to the original dataset
dmu = np.array(tuple(rnp.root2array(outname, 'limit', mus)[0])) - muhat

os.unlink(outname)

try:
    os.makedirs('%s/bias' % ws_dir)
except OSError:
    pass

# bias = dmu / dn * (nuhat - n)
# The basic idea is that nuhat should be ~ n if there is no regularization bias
# So nuhat - n is the bias in terms of bin content, and dmu / dn converts that into the bias in terms of mu values
bias = np.array([tuple(dmu / dn * (nuhat - n))], dtype=[(mu, 'f4') for mu in mus])

rnp.array2root(bias, '%s/bias/bias_%s.root' % (ws_dir, sr), 'bias')
