#Aliases (mostly btag)

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

#2017
#bWP = '0.1522' #Loose
bWP = '0.4941'

aliases['bVeto'] = {
    'expr': '(Sum$( CleanJet_pt > 20.0 && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > '+bWP+' ) == 0)'
}

# Temporary patch for BTV postprocessor bug (no SF for eta < 0, <= 102X_nAODv5_Full2018v5)

#2017
btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}

aliases['btagSF'] = {
'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}

systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:

    aliases['Jet_btagSF_shapeFix_up_%s' % s] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + s),
        'samples': mc
    }

    aliases['Jet_btagSF_shapeFix_down_%s' % s] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + s),
        'samples': mc
    }

    aliases['btagSF'+s+'up']   = { 
        'expr': aliases['btagSF']['expr'].replace('shapeFix','shapeFix_up_'+s),
        'samples':mc  
    }
    aliases['btagSF'+s+'down'] = { 
        'expr': aliases['btagSF']['expr'].replace('shapeFix','shapeFix_down_'+s),
        'samples':mc  
    }

aliases['EleWPTight'] = {
    'expr' : '(abs(Lepton_pdgId[0])==13 || Electron_cutBased[Lepton_electronIdx[0]]>=4) \
           && (abs(Lepton_pdgId[1])==13 || Electron_cutBased[Lepton_electronIdx[1]]>=4) \
           && (abs(Lepton_pdgId[2])==13 || Electron_cutBased[Lepton_electronIdx[2]]>=4)',
}
