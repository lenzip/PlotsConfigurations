
supercut = '    mll>12 \
            && Lepton_pt[0]>20 \
            && Lepton_pt[1]>10 \
            && (abs(Lepton_pdgId[0])==13 || Lepton_pt[0]>25) \
            && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
           '

# Some cuts

dymva0jetee = 'hww_DYmvaDNN_0j(Entry$) > 0.965'
dymva0jetmm = 'hww_DYmvaDNN_0j(Entry$) > 0.965'
dymva1jetee = 'hww_DYmvaDNN_1j(Entry$) > 0.885'
dymva1jetmm = 'hww_DYmvaDNN_1j(Entry$) > 0.885'
dymva2jetee = 'hww_DYmvaDNN_2j(Entry$) > 0.970'
dymva2jetmm = 'hww_DYmvaDNN_2j(Entry$) > 0.970'
dymvaVBFee  = 'hww_DYmvaDNN_VBF(Entry$)> 0.965'
dymvaVBFmm  = 'hww_DYmvaDNN_VBF(Entry$)> 0.965'

# Higgs Signal Regions: ee/uu * 0/1 jet

cuts['hww2l2v_13TeV_2017_0jee_pt2ge20'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Lepton_pt[1]>=20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetee \
                             && '+dymva0jetee+' \
                             '

cuts['hww2l2v_13TeV_2017_0jee_pt2lt20'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Lepton_pt[1]<20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetee \
                             && '+dymva0jetee+' \
                             '

cuts['hww2l2v_13TeV_2017_1jee'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs1jetee \
                             && '+dymva1jetee+' \
                             '

cuts['hww2l2v_13TeV_2017_0jmm_pt2ge20'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Lepton_pt[1]>=20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetmm \
                             && '+dymva0jetmm+' \
                             '

cuts['hww2l2v_13TeV_2017_0jmm_pt2lt20'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Lepton_pt[1]<20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetmm \
                             && '+dymva0jetmm+' \
                             '

cuts['hww2l2v_13TeV_2017_1jmm'] = ' (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs1jetmm \
                             && '+dymva1jetmm+' \
                             '

## Loose dymva + H sel for DY Acc
cuts['hww2l2v_13TeV_2017_0jee_HAccNum_pt2ge20'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Lepton_pt[1]>=20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetee \
                             && hww_DYmvaDNN_0j(Entry$)>0.8 \
                             '

cuts['hww2l2v_13TeV_2017_0jee_HAccNum_pt2lt20'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Lepton_pt[1]<20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetee \
                             && hww_DYmvaDNN_0j(Entry$)>0.8 \
                             '

cuts['hww2l2v_13TeV_2017_1jee_HAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs1jetee \
                             && hww_DYmvaDNN_1j(Entry$)>0.8 \
                             '

cuts['hww2l2v_13TeV_2017_0jmm_HAccNum_pt2ge20'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Lepton_pt[1]>=20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetmm \
                             && hww_DYmvaDNN_0j(Entry$)>0.8 \
                             '

cuts['hww2l2v_13TeV_2017_0jmm_HAccNum_pt2lt20'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Lepton_pt[1]<20 \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs0jetmm \
                             && hww_DYmvaDNN_0j(Entry$)>0.8 \
                             '

cuts['hww2l2v_13TeV_2017_1jmm_HAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && Higgs1jetmm \
                             && hww_DYmvaDNN_1j(Entry$)>0.8 \
                             '

## Top CR: No H sel , bTag , tight DYmva

cuts['hww2l2v_13TeV_2017_top_0jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && topcr \
                             && ZVeto \
                             && '+dymva0jetee+' \
                             '

cuts['hww2l2v_13TeV_2017_top_1jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && topcr \
                             && ZVeto \
                             && '+dymva1jetee+' \
                             '

cuts['hww2l2v_13TeV_2017_top_0jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && topcr \
                             && ZVeto \
                             && '+dymva0jetmm+' \
                             '

cuts['hww2l2v_13TeV_2017_top_1jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && topcr \
                             && ZVeto \
                             && '+dymva1jetmm+' \
                             '

## WW CR: No H Sel , mll>80, tight DYMva

cuts['hww2l2v_13TeV_2017_WW_0jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && '+dymva0jetee+' \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_1jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && '+dymva1jetee+' \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_0jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && '+dymva0jetmm+' \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_1jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && '+dymva1jetmm+' \
                             && wwcr \
                             '

## DY Background IN with DYMVA>0.9X : Split ee/mm , No H cut !

cuts['hww2l2v_13TeV_2017_DYin_0jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && '+dymva0jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_1jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && '+dymva1jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_0jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && '+dymva0jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_1jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && '+dymva1jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_0jdf_ee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && '+dymva0jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_1jdf_ee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && '+dymva1jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_0jdf_mm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && '+dymva0jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_1jdf_mm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && '+dymva1jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

## DY Background IN with btag : Split ee/mm , No H cut !
#  0jet only: Negligible DY background in 1jet bTag region

cuts['hww2l2v_13TeV_2017_DYin_btag_0jee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && topcr \
                             && '+dymva0jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_btag_0jmm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && topcr \
                             && '+dymva0jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_btag_0jdf_ee'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && topcr \
                             && ((zeroJet && !bVeto) || bReq)  \
                             && '+dymva0jetee+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

cuts['hww2l2v_13TeV_2017_DYin_btag_0jdf_mm'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && topcr \
                             && '+dymva0jetmm+' \
                             && fabs(91.1876 - mll) < 7.5  \
                             '

## DY CR for Acc Denominator

cuts['hww2l2v_13TeV_2017_0jee_AccDen'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && hww_DYmvaDNN_0j(Entry$) > 0.8 \
                             '

cuts['hww2l2v_13TeV_2017_1jee_AccDen'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && hww_DYmvaDNN_1j(Entry$) > 0.8 \
                             '

cuts['hww2l2v_13TeV_2017_0jmm_AccDen'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && hww_DYmvaDNN_0j(Entry$) > 0.8 \
                             '

cuts['hww2l2v_13TeV_2017_1jmm_AccDen'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && bVeto \
                             && ZVeto \
                             && hww_DYmvaDNN_1j(Entry$) > 0.8 \
                             '

## Loose dymva + WW sel for DY Acc


cuts['hww2l2v_13TeV_2017_WW_0jee_WWAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && hww_DYmvaDNN_0j(Entry$) > 0.8 \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_1jee_WWAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && hww_DYmvaDNN_1j(Entry$) > 0.8 \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_0jmm_WWAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)<30 \
                             && hww_DYmvaDNN_0j(Entry$) > 0.8 \
                             && wwcr \
                             '

cuts['hww2l2v_13TeV_2017_WW_1jmm_WWAccNum'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                             && Alt$(CleanJet_pt[0],0)>=30 \
                             && Alt$(CleanJet_pt[1],0)<30 \
                             && hww_DYmvaDNN_1j(Entry$) > 0.8 \
                             && wwcr \
                             '
