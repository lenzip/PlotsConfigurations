# cuts
# Looking only at FatJet category with two jets of 30 JeV
# Removing events with the two highest pt jets are between [2.5,3.2] eta

supercut = "Lepton_pt[0]>30  \
            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)>0.5\
            && ( Alt$(Lepton_isTightElectron_mvaFall17V1Iso_WP90[1], 0) < 0.5 \
                && Alt$(Lepton_isTightMuon_cut_Tight_HWWW[1],0) < 0.5 ) \
            && VBS_category == 0  \
            && vbs_pt_high >= 30  \
            && vbs_pt_low >= 30 "
# Vbs jets are the jets extracted by MaxMjj association from the CleanJet after FatJet cleaning

# cuts["fatjet_ele_incl"] = 'abs(Lepton_pdgId[0])==11 \
#                         && Lepton_pt[0] >= 40 \
#                         '

# cuts["fatjet_mu_incl"] = 'abs(Lepton_pdgId[0])==13  \
#                         && Lepton_pt[0] >= 30 \
#                         '               

cuts["CR_ele_looseVBS"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && bVeto   \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["CR_mu_looseVBS"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && bVeto    \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["CR_ele_topCR"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && !bVeto   \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["CR_mu_topCR"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && !bVeto    \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["CR_ele_WjetsCR"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && bVeto   \
                        && PuppiMET_pt > 30 \
                        && (CleanFatJet_mass[0] < 65 || CleanFatJet_mass[0] > 105) \
                        '

cuts["CR_mu_WjetsCR"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >=300    \
                        && deltaeta_vbs >= 2  \
                        && bVeto    \
                        && PuppiMET_pt > 30 \
                        && (CleanFatJet_mass[0] < 65 || CleanFatJet_mass[0] > 105) \
                        '

cuts["SR_ele_tightVBS"] = 'abs(Lepton_pdgId[0])==11 \
                       && Lepton_pt[0] >= 40 \
                       && mjj_vbs >=600    \
                       && deltaeta_vbs >= 3.5  \
                       && bVeto    \
                       && PuppiMET_pt > 30 \
                       && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                       '

cuts["SR_mu_tightVBS"] = 'abs(Lepton_pdgId[0])==13 \
                       && Lepton_pt[0] >= 30 \
                       && mjj_vbs >=600    \
                       && deltaeta_vbs >= 3.5  \
                       && bVeto    \
                       && PuppiMET_pt > 30 \
                       && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                       '


cuts["SR_ele_topCR"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=600    \
                        && deltaeta_vbs >= 3.5  \
                        && !bVeto   \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["SR_mu_topCR"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >=600    \
                        && deltaeta_vbs >= 3.5  \
                        && !bVeto    \
                        && PuppiMET_pt > 30 \
                        && CleanFatJet_mass[0] > 65 && CleanFatJet_mass[0] < 105 \
                        '

cuts["SR_ele_WjetsCR"] = 'abs(Lepton_pdgId[0])==11 \
                        && Lepton_pt[0] >= 40 \
                        && mjj_vbs >=600    \
                        && deltaeta_vbs >= 3.5  \
                        && bVeto   \
                        && PuppiMET_pt > 30 \
                        && (CleanFatJet_mass[0] < 65 || CleanFatJet_mass[0] > 105) \
                        '

cuts["SR_mu_WjetsCR"] = 'abs(Lepton_pdgId[0])==13 \
                        && Lepton_pt[0] >= 30 \
                        && mjj_vbs >= 600    \
                        && deltaeta_vbs >= 3.5  \
                        && bVeto    \
                        && PuppiMET_pt > 30 \
                        && (CleanFatJet_mass[0] < 65 || CleanFatJet_mass[0] > 105) \
                        '