# cuts


#supercut = 'mll>12  \
#            && Lepton_pt[0]>25 && Lepton_pt[1]>20 \
#            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
#            && PuppiMET_pt > 30 \
#            && abs(Lepton_eta[0] - Lepton_eta[1])<2.0 \
#            '

supercut = 'mll>12  \
            && Lepton_pt[0]>25 && Lepton_pt[1]>20 && Lepton_pt[2]>15 \
            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
            && bVeto \
            '
## 2jets

cuts['hww2l2v_13TeV_of2j_WH_SS_WZ_1j'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13))\
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       && WH3l_mlll > 100 \
                                       && PuppiMET_pt > 30 \
                                       && abs(WH3l_chlll) == 1 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_WZ_2j'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13)) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)>30 \
                                       && WH3l_mlll > 100 \
                                       && PuppiMET_pt > 30 \
                                       && abs(WH3l_chlll) == 1 \
                                       '

#cuts['hww2l2v_13TeV_of2j_WH_SS_Vg_1j'] = '((Lepton_pdgId[0]*Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13))\
#                                       && Alt$(CleanJet_pt[0],0)>30 \
#                                       && Alt$(CleanJet_pt[1],0)<30 \
#                                       && (((abs(Lepton_pdgId[1])==13 || Electron_lostHits[Lepton_electronIdx[1]]>0)) || ((abs(Lepton_pdgId[2])==13 || Electron_lostHits[Lepton_electronIdx[2]]>0))) \
#                                       '
#
'''
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)>30 \
                                       && mjj < 100 \
                                       '

cuts['hww2l2v_13TeV_of2j_WH_SS_ll_2j'] = '((Lepton_pdgId[0] * Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0] * Lepton_pdgId[1] == 11*11)) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)>30 \
                                       && mjj < 100 \
                                       && abs(mll-91.2)>15 \
                                       '
## 1jet

cuts['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 13*13) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_ee_1j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*11) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       && abs(mll-91.2)>15 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_ll_1j'] = '((Lepton_pdgId[0] * Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0] * Lepton_pdgId[1] == 11*11)) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       && abs(mll-91.2)>15 \
                                       '

'''
'''
## Signal regions
cuts['hww2l2v_13TeV_of2j_WH_SS_ll_1j'] = '((Lepton_pdgId[0] * Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0] * Lepton_pdgId[1] == 11*11)) \
                                       && abs(mll-91.2)>12 \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_ll_2j'] = '((Lepton_pdgId[0] * Lepton_pdgId[1] == 13*13) || (Lepton_pdgId[0] * Lepton_pdgId[1] == 11*11)) \
                                       && abs(mll-91.2)>12 \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)>30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)<30 \
                                       '
cuts['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13) \
                                       && Alt$(CleanJet_pt[0],0)>30 \
                                       && Alt$(CleanJet_pt[1],0)>30 \
                                       '
'''
