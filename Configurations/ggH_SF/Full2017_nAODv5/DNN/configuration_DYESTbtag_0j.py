# example of configuration file
treeName= 'Events'

tag = 'BG_DY_NOHR_2017_btag_0j'

# used by mkShape to define output directory for root files
outputDir = 'rootFile'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables_0j.py'

# file with list of cuts
cutsFile = 'cuts_DYESTbtag_0j.py' 

# file with list of samples
samplesFile = 'samples_DYEST.py' 

# file with list of samples
plotFile = 'plot.py' 



# luminosity to normalize to (in 1/fb)
lumi = 41.5

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotGGH'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
#nuisancesFile = 'nuisances.py'

