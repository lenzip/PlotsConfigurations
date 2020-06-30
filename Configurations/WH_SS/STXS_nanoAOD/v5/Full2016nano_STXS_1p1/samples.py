import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *


from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

samples={}

skim=''
##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

directory = treeBaseDir+'Summer16_102X_nAODv4_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/'+skim

def makeMCDirectory(var=''):
    if var:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        #return '/afs/cern.ch/user/d/ddicroce/public/Summer16/l2tightOR__{var}'.format(var=var)
        return '/afs/cern.ch/user/s/shoh/public/latino_STXS/WH2l/'+var+'/wwSel'
    else:
        #return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        return '/afs/cern.ch/user/d/ddicroce/public/Summer16/l2tightOR'

#mcDirectory   = makeMCDirectory()
mcStxs        = makeMCDirectory('2016')

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

#eleWP='mva_90p_Iso2016'
eleWP='cut_WP_Tight80X_SS'
#eleWP='mva_90p_Iso2016'
#eleWP='mvaFall17V2Iso_WP90_SS'
muWP='cut_Tight80x'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
GenLepMatch   = 'GenLepMatch'+Nlep+'l'


################################################
############## FAKE WEIGHTS ####################
################################################

if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

#FIXME b-tagging to be optimized
# Definitions in aliases.py


SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2016B-Nano14Dec2018_ver2-v1'] ,
            ['C','Run2016C-Nano14Dec2018-v1'] ,
            ['D','Run2016D-Nano14Dec2018-v1'] ,
            ['E','Run2016E-Nano14Dec2018-v1'] ,
            ['F','Run2016F-Nano14Dec2018-v1'] ,
            ['G','Run2016G-Nano14Dec2018-v1'] ,
            ['H','Run2016H-Nano14Dec2018-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }


#mcCommonWeight = 'XSWeight*SFweight*GenLepMatch*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############

useDYtt = False
useDYHT = True

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

if useDYtt:
    files = getSampleFiles(directory, 'DYJetsToTT_MuEle_M-50',False,'nanoLatino_') + \
            getSampleFiles(directory, 'DYJetsToLL_M-10to50-LO',False,'nanoLatino_')

    samples['DY'] = {
        'name': files,
        'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
        'FilesPerJob': 2,
    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

else:
    files = getSampleFiles(mcStxs, 'DYJetsToLL_M-50_ext2',True,'nanoLatino_') + \
            getSampleFiles(mcStxs, 'DYJetsToLL_M-10to50-LO',True,'nanoLatino_')

    samples['DY'] = {
        'name': files,
        'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
        'FilesPerJob': 2,
        'suppressNegative' :['all'],
        'suppressNegativeNuisances' :['all'],

    }
    # Add DY HT Samples
    if useDYHT :
        samples['DY']['name'] +=   getSampleFiles(mcStxs, 'DYJetsToLL_M-5to50_HT-70to100',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-5to50_HT-100to200_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-5to50_HT-200to400_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-5to50_HT-400to600_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-5to50_HT-600toinf',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-70to100',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-100to200_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-200to400_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-400to600_ext1',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-600to800',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-800to1200',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-1200to2500',True,'nanoLatino_') \
                                 + getSampleFiles(mcStxs, 'DYJetsToLL_M-50_HT-2500toinf',True,'nanoLatino_')

    addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

    if useDYHT :
        # Remove high HT from inclusive samples
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2'  , 'LHE_HT<70.0')
        addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO', 'LHE_HT<70.0')
        # pt_ll weight
        addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100'       ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-100to200_ext1' ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400_ext1' ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600_ext1' ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf'      ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100'          ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1'    ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1'    ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1'    ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800'         ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200'        ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500'       ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toinf'        ,ptllDYW_LO)






'''
ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext1',False,'nanoLatino_')
                                + getSampleFiles(directory,'DYJetsToLL_M-50-LO_ext2',False,'nanoLatino_'),
#                                + getSampleFiles(directory,'DYJetsToLL_M-50_ext2',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 5,
                 }

DYbaseW = getBaseWnAOD(directory,'Summer16_102X_nAODv4_Full2016v5',['DYJetsToLL_M-50-LO_ext1','DYJetsToLL_M-50-LO_ext2'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext1',     DYbaseW+'/baseW')
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext2',DYbaseW+'/baseW')

#addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext1',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext2',ptllDYW_LO)
#addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)
'''
############ Top ############

Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

samples['top'] = {    'name'   :   getSampleFiles(mcStxs,'TTTo2L2Nu',True,'nanoLatino_')
                                 + getSampleFiles(mcStxs,'ST_s-channel',True,'nanoLatino_')
                                 + getSampleFiles(mcStxs,'ST_t-channel_antitop',True,'nanoLatino_')
                                 + getSampleFiles(mcStxs,'ST_t-channel_top',True,'nanoLatino_')
                                 + getSampleFiles(mcStxs,'ST_tW_antitop',True,'nanoLatino_')
                                 + getSampleFiles(mcStxs,'ST_tW_top',True,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 5,
                 }

addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)

############ WW ############

#FIXME Add nllW weight to WW
samples['WW'] = {    'name'   :   getSampleFiles(mcStxs,'WWTo2L2Nu',True,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*nllW' ,
                 }


samples['WWewk'] = {   'name'  : getSampleFiles(mcStxs, 'WpWmJJ_EWK',True,'nanoLatino_'),
                       'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+ '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*(lhe_mW1[0] > 60. && lhe_mW1[0] < 100. && lhe_mW2[0] > 60. && lhe_mW2[0] < 100.)', #filter tops and Higgs, limit w mass
                   }

samples['ggWW']  = {  'name'   : getSampleFiles(mcStxs,'GluGluWWTo2L2Nu_MCFM',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'isData': ['0'],
                   }

############ Vg ############

samples['Vg']  =  {     'name'   :   getSampleFiles(mcStxs,'Wg_MADGRAPHMLM',True,'nanoLatino_')
                                   + getSampleFiles(mcStxs,'Zg',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC + '*(Gen_ZGstar_mass <= 0)',
                        'FilesPerJob' : 5 ,
                  }
addSampleWeight(samples, 'Vg', 'Zg', '(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')

######## VgS ########
#FIXME: k-factor?
samples['VgS']  = {    'name':   getSampleFiles(mcStxs,'Wg_MADGRAPHMLM',True,'nanoLatino_')
                               + getSampleFiles(mcStxs,'Zg',True,'nanoLatino_')
                               + getSampleFiles(mcStxs,'WZTo3LNu_mllmin01',True,'nanoLatino_') ,
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                       'FilesPerJob' : 2 ,
                  }
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass >0)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

#FIXME Add normalization k-factor
samples['VZ']  = {  'name'   :   getSampleFiles(mcStxs,'ZZTo2L2Nu',True,'nanoLatino_')
                               + getSampleFiles(mcStxs,'ZZTo2L2Q',True,'nanoLatino_')
                               + getSampleFiles(mcStxs,'ZZTo4L',True,'nanoLatino_')
                               + getSampleFiles(mcStxs,'WZTo2L2Q',True,'nanoLatino_'),
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*1.11',
                    'FilesPerJob' : 3,
                 }


############ VVV ############

samples['VVV']  = {  'name'   :   getSampleFiles(mcStxs,'ZZZ',True,'nanoLatino_')
                                + getSampleFiles(mcStxs,'WZZ',True,'nanoLatino_')
                                + getSampleFiles(mcStxs,'WWZ',True,'nanoLatino_')
                                + getSampleFiles(mcStxs,'WWW',True,'nanoLatino_'),
                                #+ getSampleFiles(mcStxs,'WWG',True,'nanoLatino_'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                  }



##########################################
################ SIGNALS #################
##########################################

############ ggH H->WW ############
#FIXME Add reweighting to MiNLO NNLOPS or use NNLOPS sample when available
samples['ggH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'GluGluHToWWTo2L2NuPowheg_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }

############ VBF H->WW ############
samples['qqH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'VBFHToWWTo2L2Nu_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }

############ ZH H->WW ############

samples['ZH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'HZJ_HToWW_M125',True,'nanoLatino_'), #FIXME replace with 125 GeV sample when available
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }

samples['ggZH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'ggZH_HToWW_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }

############ WH H->WW ############

#samples['WH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'HWplusJ_HToWW_M125',True,'nanoLatino_')
#                                   + getSampleFiles(mcStxs,'HWminusJ_HToWW_M125',True,'nanoLatino_'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

samples['WH_hww'] = { 'name'   :
                      getSampleFiles(mcStxs,'HWplusJ_HToWW_M125',True,'nanoLatino_')
                      + getSampleFiles(mcStxs,'HWminusJ_HToWW_M125',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'suppressNegativeNuisances' :['all'],
                      'subsamples' : {
                          'PTV_LT150' : 'HTXS_stage1_1_cat_pTjet30GeV==301 || HTXS_stage1_1_cat_pTjet30GeV==302',
                          'PTV_GT150' : 'HTXS_stage1_1_cat_pTjet30GeV==303 || HTXS_stage1_1_cat_pTjet30GeV==304 || HTXS_stage1_1_cat_pTjet30GeV==305',
                          'FWDH'      : 'HTXS_stage1_1_cat_pTjet30GeV==300'
                      }
                  }


############ ttH ############

#samples['ttH_hww']  = {  'name'   :   getSampleFiles(mcStxs,'ttHToNonbb_M125',True,'nanoLatino_'),
#                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

############ bbH ############
#FIXME Missing samples


############ H->TauTau ############

splitHtt=False
if not splitHtt:

  samples['H_htt'] = {  'name'   :   getSampleFiles(mcStxs,'GluGluHToTauTau_M125',True,'nanoLatino_')
                                   + getSampleFiles(mcStxs,'VBFHToTauTau_M125',True,'nanoLatino_')
                                   + getSampleFiles(mcStxs,'HZJ_HToTauTau_M125',True,'nanoLatino_')
                                   + getSampleFiles(mcStxs,'HWplusJ_HToTauTau_M125',True,'nanoLatino_')
                                   + getSampleFiles(mcStxs,'HWminusJ_HToTauTau_M125',True,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'suppressNegative' :['all'],
                         'suppressNegativeNuisances' :['all'],
                     }
else:

  samples['ggH_htt']  = {  'name'   : getSampleFiles(mcStxs,'GluGluHToTauTau_M125',True,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['qqH_htt']  = {  'name'   : getSampleFiles(mcStxs,'VBFHToTauTau_M125',True,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['ZH_htt']  = {  'name'   : getSampleFiles(mcStxs,'HZJ_HToTauTau_M125',True,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['WH_htt']  = {  'name'   :  getSampleFiles(mcStxs,'HWplusJ_HToTauTau_M125',True,'nanoLatino_')
                                    + getSampleFiles(mcStxs,'HWminusJ_HToTauTau_M125',True,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }


###########################################
################## FAKE ###################
###########################################



#samples['Fakes']  = {  'name'   :   getSampleFiles(mcStxs,'WJetsToLNu-LO',True,'nanoLatino_')
#                                  + getSampleFiles(mcStxs,'TTToSemiLeptonic',True,'nanoLatino_'),
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
#                       'FilesPerJob': 3,
#                    }
#
'''
samples['Fakes']  = {   'name': [ ] ,
                       #'weight' : fakeW+'*'+METFilter_DATA+'*((Lepton_pdgId[0]*Lepton_pdgId[1]==11*13) || (Lepton_pdgId[0]*Lepton_pdgId[1]==11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1]==13*13))',              #   weight/cut
                       'weight' : fakeW+'*'+METFilter_DATA,
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 10 ,
                     }
'''

#samples['Fakes_ee']  = {   'name': [ ] ,
#                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==11*11)',              #   weight/cut
#                       'weights' : [ ] ,
#                       'isData': ['all'],
#                       'FilesPerJob' : 15 ,
#                     }

samples['Fakes_mm']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==13*13)',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }

samples['Fakes_em']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==11*13)',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }


for Run in DataRun :
  directory = treeBaseDir+'Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__fakeW/'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
#      samples['Fakes']['name'].append(iFile)
#      samples['Fakes']['weights'].append(DataTrig[DataSet])

      samples['Fakes_mm']['name'].append(iFile)
      samples['Fakes_mm']['weights'].append(DataTrig[DataSet])
      samples['Fakes_em']['name'].append(iFile)
      samples['Fakes_em']['weights'].append(DataTrig[DataSet])

###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 10 ,
                  }

for Run in DataRun :
  directory = treeBaseDir+'/Run2016_102X_nAODv4_Full2016v5/DATAl1loose2016v5__l2loose__l2tightOR2016v5/'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])
