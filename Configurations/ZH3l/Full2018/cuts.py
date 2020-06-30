# cuts

supercut = 'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
            && Alt$(Lepton_pt[0],0)>25 \
            && Alt$(Lepton_pt[1],0)>20 \
            && Alt$(Lepton_pt[2],0)>15 \
            && Alt$(Lepton_pt[3],0)<10 \
            && abs(WH3l_chlll) == 1 \
           '

cuts['preselection']   = '1'

cuts['zmass_cut'] = ' WH3l_ZVeto < 25 '

cuts['jet_cut_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) >= 30 \
                    && WH3l_ZVeto < 25 \
                    '

cuts['bveto_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                  && Alt$( CleanJet_pt[1], 0) >= 30 \
                  && WH3l_ZVeto < 25 \
                  && bVeto \
                  '

cuts['z4lveto_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) >= 30 \
                    && WH3l_ZVeto < 25 \
                    && bVeto \
                    && ZH3l_Z4lveto > 20 \
                    '

cuts['zh3l_Zg_CR_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                       && Alt$( CleanJet_pt[1], 0) >= 30 \
                       && WH3l_ZVeto < 25 \
                       && bVeto \
                       && ZH3l_Z4lveto < 10 \
                       '

cuts['zh3l_SR_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) >= 30 \
                    && WH3l_ZVeto < 25 \
                    && bVeto \
                    && ZH3l_Z4lveto > 20 \
                    && ZH3l_dphilmetjj < 3.14159/2 \
                    '

cuts['zh3l_WZ_CR_2j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                       && Alt$( CleanJet_pt[1], 0) >= 30 \
                       && WH3l_ZVeto < 25 \
                       && bVeto \
                       && ZH3l_Z4lveto > 20 \
                       && ZH3l_dphilmetjj > 3.14159/2 \
                       '

cuts['jet_cut_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) < 30 \
                    && WH3l_ZVeto < 25 \
                    '

cuts['bveto_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                  && Alt$( CleanJet_pt[1], 0) < 30 \
                  && WH3l_ZVeto < 25 \
                  && bVeto \
                  '

cuts['z4lveto_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) < 30 \
                    && WH3l_ZVeto < 25 \
                    && bVeto \
                    && ZH3l_Z4lveto > 20 \
                    '

cuts['zh3l_Zg_CR_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                       && Alt$( CleanJet_pt[1], 0) < 30 \
                       && WH3l_ZVeto < 25 \
                       && bVeto \
                       && ZH3l_Z4lveto < 10 \
                       '

cuts['zh3l_SR_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                    && Alt$( CleanJet_pt[1], 0) < 30 \
                    && WH3l_ZVeto < 25 \
                    && bVeto \
                    && ZH3l_Z4lveto > 20 \
                    && ZH3l_dphilmetj < 3.14159/2 \
                    '

cuts['zh3l_WZ_CR_1j'] = ' Alt$( CleanJet_pt[0], 0) >= 30 \
                       && Alt$( CleanJet_pt[1], 0) < 30 \
                       && WH3l_ZVeto < 25 \
                       && bVeto \
                       && ZH3l_Z4lveto > 20 \
                       && ZH3l_dphilmetj > 3.14159/2 \
                       '

'''
 #11 = e
# 13 = mu
# 15 = tau
'''
