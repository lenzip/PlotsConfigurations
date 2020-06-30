# nuisances

#nuisances = {}

eleWP='mva_90p_Iso2016'
#'cut_WP_Tight80X'
#'cut_WP_Tight80X_SS'
#'mva_80p_Iso2015'
#'mva_80p_Iso2016'
#'mva_90p_Iso2015'
#'mva_90p_Iso2016'
muWP='cut_Tight80x'

upDownPath = "/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_summer16/"


# name of samples here must match keys in samples.py
#

nuisances['lumi']  = {
        'name'  : 'lumi_13TeV',
        'samples'  : {
            'WH_hww'    : '1.025',
            'ZH_hww'    : '1.025',
            'ggZH_hww'  : '1.025',
            'WH_htt'    : '1.025',
            'ZH_htt'    : '1.025',
            'ggH_hzz'   : '1.025',
            'WWW'       : '1.025',
            'VVZ'       : '1.025',
            # 'ZZ'        : '1.025', # This should *not* appear in samples whose normalization is taken care by rateParam nuisance.
            'WZ'        : '1.025',
            'WW'        : '1.025',
            'ggWW'      : '1.025',
            'Vg'        : '1.025',
            'DY'        : '1.025',
            'ttW'       : '1.025',
            'ttZ'       : '1.025',
            'top'       : '1.025',
            },
        'type'  : 'lnN',
        }




# Theoritical Systematics

from LatinoAnalysis.Tools.HiggsXSection import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_VH']  = {
        'name' : 'QCDscale_VH',
        'samples' : {
            'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','scale','sm'),
            'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH','125.0','scale','sm'),
            },
        'type' : 'lnN',
        }

nuisances['QCDscale_ggZH']  = {
        'name' : 'QCDscale_ggZH',
        'samples'  : {
            'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','scale','sm'),
            },
        'type' : 'lnN',
        }

# pdf uncertainty

nuisances['pdf_Higgs_gg']  = {
        'name' : 'pdf_Higgs_gg',
        'samples' : {
            'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ggZH','125.0','pdf','sm'),
            },
        'type' : 'lnN',
        }

nuisances['pdf_Higgs_qqbar']  = {
        'name'  : 'pdf_Higgs_qqbar',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH' ,'125.0','pdf','sm'),
            'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4prel','13TeV','ZH' ,'125.0','pdf','sm'),
            },
        }


##acceptance
nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'ZH_hww'  : '1.013',
                   'ZH_htt'  : '1.009',
                   },
              }

nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'ggZH_hww'  : '1.012',
                   },
              }

nuisances['QCDscale_qqbar_ACCEPT']  = {
               'name'  : 'QCDscale_qqbar_ACCEPT', 
               'type'  : 'lnN',
               'samples'  : {
                   'ZH_hww'  : '1.016',
                   'ZH_htt'  : '1.004',
                   # 'ZZ'      : '1.048',
                   },
              }


nuisances['QCDscale_gg_ACCEPT']  = {
               'name'  : 'QCDscale_gg_ACCEPT', 
               'samples'  : {
                   'ggZH_hww': '1.003',                   
                   },
               'type'  : 'lnN',
              }



## PS/UE
#
## PS
#
nuisances['PS_zh4l']  = {
        'name'  : 'PS_zh4l',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'   : '1.037',
            'ZH_htt'   : '1.037',
            'ggZH_hww'  : '1.037',
            },
        }

nuisances['UE_zh4l']  = {
        'name'  : 'UE_zh4l',
        'type'  : 'lnN',
        'samples'  : {
            'ZH_hww'   : '1.010',
            'ZH_htt'   : '1.010',
            'ggZH_hww'  : '1.010',
            },
        }


nuisances['CMS_hww_ZZ4lnorm']  = {
        'name'  : 'CMS_hww_ZZ4lnorm',
        'samples'  : {
            'ZZ' : '1.00',
            },
        'type'  : 'rateParam',
        'cuts'  : [
            'zh4l_ZZ_13TeV',
            'zh4l_XSF_13TeV',
            'zh4l_XDF_13TeV',
            ]
        }
# Other Systematics


nuisances['btag_heavy']  = {
        'name'  : 'btag_heavy',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
            'ggH_hww' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'qqH_hww' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZH_hww'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZH_htt'  : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggZH_hww': ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'H_htt'   : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'H_hww'   : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggH_hzz' : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'DY'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ttZ'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ttW'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WWW'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VVZ'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VZ'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ZZ'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggZZ'    : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'WW'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'ggWW'    : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'top'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'Vg'      : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            'VgS'     : ['(bPogSF_CMVAL_bc_up)/(bPogSF)', '(bPogSF_CMVAL_bc_down)/(bPogSF)'],
            }
        }

nuisances['btag_light']  = {
        'name'  : 'btag_light',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
            'ggH_hww' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'qqH_hww' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZH_htt'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggZH_hww': ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'H_htt'   : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'H_hww'   : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WH_hww'  : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggH_hzz' : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'DY'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ttZ'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ttW'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WWW'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VVZ'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VZ'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ZZ'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggZZ'    : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'WW'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'ggWW'    : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'top'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'Vg'      : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            'VgS'     : ['(bPogSF_CMVAL_udsg_up)/(bPogSF)', '(bPogSF_CMVAL_udsg_down)/(bPogSF)'],
            }
        }


nuisances['hww_trigger']  = {
        'name'  : 'hww_trigger',
        'kind'  : 'weight',
        #'kind'  : 'tree', #'weight',
        'type'  : 'shape',
        'samples'  : {
            'WH_hww'   : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ZH_hww'   : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ZH_htt'   : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ggZH_hww' : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'WH_htt'   : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ggH_hzz'  : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'WWW'      : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'VVZ'      : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'WZ'       : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'DY'       : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ttW'      : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ttZ'      : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ZZ'       : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'ggZZ'     : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'WW'       : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'Vg'       : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            'top'      : ['(effTrigW4l_Up)/(effTrigW4l)', '(effTrigW4l_Down)/(effTrigW4l)'],
            },
        }


id_syst_ele = [ 'LepSF4l__ele_'+eleWP+'__Up' , 'LepSF4l__ele_'+eleWP+'__Do' ]
id_syst_mu  = [ 'LepSF4l__mu_'+muWP+'__Up' , 'LepSF4l__mu_'+muWP+'__Do' ]


nuisances['eff_e']  = {
        'name'  : 'eff_e',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
              'WH_hww'   : id_syst_ele,
              'ZH_hww'   : id_syst_ele,
              'ZH_htt'   : id_syst_ele,
              'ggZH_hww' : id_syst_ele,
              'WH_htt'   : id_syst_ele,
              'ggH_hzz'  : id_syst_ele,
              'WW'       : id_syst_ele,
              'Vg'       : id_syst_ele,
              'WZ'       : id_syst_ele,
              'ZZ'       : id_syst_ele,
              'ggZZ'     : id_syst_ele,
              'WWW'      : id_syst_ele,
              'VVZ'      : id_syst_ele,
              'ttZ'      : id_syst_ele,
              'ttW'      : id_syst_ele,
            },
        }


nuisances['eff_m']  = {
        'name'  : 'eff_m',
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  : {
              'WH_hww'   : id_syst_mu,
              'ZH_hww'   : id_syst_mu,
              'ZH_htt'   : id_syst_mu,
              'ggZH_hww' : id_syst_mu,
              'WH_htt'   : id_syst_mu,
              'ggH_hzz'  : id_syst_mu,
              'WW'       : id_syst_mu,
              'Vg'       : id_syst_mu,
              'WZ'       : id_syst_mu,
              'ZZ'       : id_syst_mu,
              'ggZZ'     : id_syst_mu,
              'WWW'      : id_syst_mu,
              'VVZ'      : id_syst_mu,
              'ttZ'      : id_syst_mu,
              'ttW'      : id_syst_mu,
            },
        }

# # # nuisances handled by means of a different set of trees


nuisances['scale_j']  = {
        'name'  : 'scale_j',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESup__vh3lSel',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__JESdo__vh3lSel'
        }


nuisances['scale_e']  = {
        'name'  : 'scale_e',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepElepTup__vh3lSel',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepElepTdo__vh3lSel'
        }

nuisances['scale_m']  = {
        'name'  : 'scale_m',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepMpTup__vh3lSel',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__LepMupTdo__vh3lSel'
        }

nuisances['scale_met']  = {
        'name'  : 'scale_met',
        'kind'  : 'tree',
        'type'  : 'shape',
        'samples'  : {
            'WW'       : ['1', '1'],
            'WZ'       : ['1', '1'],
            'ZZ'       : ['1', '1'],
            'DY'       : ['1', '1'],
            'ttW'      : ['1', '1'],
            'ttZ'      : ['1', '1'],
            'ggZZ'     : ['1', '1'],
            'WWW'      : ['1', '1'],
            'VVZ'      : ['1', '1'],
            'WH_hww'   : ['1', '1'],
            'ZH_hww'   : ['1', '1'],
            'ggZH_hww' : ['1', '1'],
            'ZH_htt'   : ['1', '1'],
            'ggH_hzz'  : ['1', '1'],
            'WH_htt'   : ['1', '1'],
            'Vg'       : ['1', '1'],
            },
        'folderUp'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METup__vh3lSel',
        'folderDown'   : upDownPath+'lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__METdo__vh3lSel'
        }


elePtCor_Syst = [ 'electron_ptW_4l_Up / electron_ptW_4l', 'electron_ptW_4l_Down / electron_ptW_4l']
nuisances['elePtCor']  = {
                'name'  : 'hww_elePtCor',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'       :elePtCor_Syst ,
                'WZ'       :elePtCor_Syst ,
                'ZZ'       :elePtCor_Syst ,
                'DY'       :elePtCor_Syst ,
                'ttW'      :elePtCor_Syst ,
                'ttZ'      :elePtCor_Syst ,
                'WWW'      :elePtCor_Syst ,
                'VVZ'      :elePtCor_Syst ,
                'ZH_hww'   :elePtCor_Syst ,
                'ggZH_hww' :elePtCor_Syst ,
                'ZH_htt'   :elePtCor_Syst ,
                'ggH_hzz'  :elePtCor_Syst ,
                'Vg'       :elePtCor_Syst ,
                }
}

eleEtaCor_Syst = [ 'electron_etaW_4l_Up / electron_etaW_4l', 'electron_etaW_4l_Down / electron_etaW_4l']

nuisances['eleEtaCor']  = {
                'name'  : 'hww_eleEtaCor',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                'WW'       :eleEtaCor_Syst ,
                'WZ'       :eleEtaCor_Syst ,
                'ZZ'       :eleEtaCor_Syst ,
                'DY'       :eleEtaCor_Syst ,
                'ttW'      :eleEtaCor_Syst ,
                'ttZ'      :eleEtaCor_Syst ,
                'WWW'      :eleEtaCor_Syst ,
                'VVZ'      :eleEtaCor_Syst ,
                'ZH_hww'   :eleEtaCor_Syst ,
                'ggZH_hww' :eleEtaCor_Syst ,
                'ZH_htt'   :eleEtaCor_Syst ,
                'ggH_hzz'  :eleEtaCor_Syst ,
                'Vg'       :eleEtaCor_Syst ,
                }
}


nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',       #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              'includeSignal'  : '1',   #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }
