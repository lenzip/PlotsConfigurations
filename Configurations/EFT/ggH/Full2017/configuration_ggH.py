# example of configuration file
treeName= 'Events'


tag = 'ggH_0M'


# used by mkShape to define output directory for root files
outputDir = 'rootFile'+tag

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables_ggH.py'

# file with list of cuts
cutsFile = 'cuts_ggH.py' 

# file with list of samples
samplesFile = 'samples_ggH.py' 

# file with list of samples
plotFile = 'plot_ggH.py' 



# luminosity to normalize to (in 1/fb)
lumi = 41.5

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot'+tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'


