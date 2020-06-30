# variables

#variables = {}
    


'''
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }
   
variables['pt1VSeta1'] = {   'name': 'Lepton_pt[0]:Lepton_eta[0]',            #   variable name    
                        'range' : (20,-2.5,2.5, 20,0,80),            #   variable range
                        'xaxis' : 'p_{T1} : #eta_{1}',      #   x axis name
                        'fold' : 0 ,
                        }

variables['pt2VSeta2'] = {   'name': 'Lepton_pt[1]:Lepton_eta[1]',            #   variable name    
                        'range' : (20,-2.5,2.5, 20,0,80),            #   variable range
                        'xaxis' : 'p_{T2} : #eta_{2}',      #   x axis name
                        'fold' : 0 ,
                        }

variables['eta1VSpt1'] = {   'name': 'Lepton_eta[0]:Lepton_pt[0]',            #   variable name    
                        'range' : (20,0,80, 20,-2.5,2.5),            #   variable range
                        'xaxis' : '#eta_{1} : p_{T1}',      #   x axis name
                        'fold' : 0 ,
                        }

variables['eta2VSpt2'] = {   'name': 'Lepton_eta[1]:Lepton_pt[1]',            #   variable name    
                        'range' : (20,0,80, 20,-2.5,2.5),            #   variable range
                        'xaxis' : '#eta_{2} : p_{T2}',      #   x axis name
                        'fold' : 0 ,
                        }

'''                        
variables['nvtx']  = {   'name': 'PV_npvsGood',      
                        'range' : (40,0,60),  
                        'xaxis' : 'nvtx', 
                         'fold' : 3
                      }
variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (40, 0,300),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['mllpeak'] = {   'name': 'mll',            #   variable name
                           'range' : (20,80,100),    #   variable range
                           'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                           'fold' : 0
                        }

'''
variables['mth']  = {   'name': 'mth',            #   variable name    
                        'range' : (40,0,200),    #   variable range
                        'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['dphill']  = {   'name': 'abs(dphill)',     
                        'range' : (20,0,3.14),   
                        'xaxis' : '#Delta#phi_{ll}',
                        'fold' : 3
                        }

'''
variables['ptll']  = {   'name': 'ptll',     
                        'range' : (40, 0,200),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }
'''

variables['ptll_low']  = {   'name': 'ptll',
                        'range' : (100,0,50),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }

variables['ptll_more']  = {   'name': 'ptll',
                        'range' : (60, 0,300),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }


'''
variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (40,0,300),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3                         
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',     
                        'range' : (40,0,200),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3                         
                        }
'''

#variables['pt3']  = {   'name': 'Lepton_pt[2]',     
                        #'range' : (10,0,50),   
                        #'xaxis' : 'p_{T} 3rd lep',
                        #'fold'  : 3                         
                        #}
'''

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3                         
                        }

                        
'''
variables['eta1large']  = {  'name': 'Lepton_eta[0]',
                       'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       'xaxis' : '#eta 1st lep',
                       'fold'  : 3
                       }

variables['eta2large']  = {  'name': 'Lepton_eta[1]',
                       'range' : ([-2.4, -2.1, -1.6, -1.2, -0.8, -0.3, -0.2, 0.2, 0.3, 0.8, 1.2, 1.6, 2.1, 2.4,],),
                       'xaxis' : '#eta 2nd lep',
                       'fold'  : 3
                       }
'''

variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }

variables['phi2']  = {  'name': 'Lepton_phi[1]',
                        'range' : (40,-3.2,3.2),
                        'xaxis' : '#phi 2nd lep',
                        'fold'  : 3
                        }

'''
##variables['taupt1']  = {'name': 'std_vector_tau_pt[0]',     
#                        #'range' : (100,0,200),   
#                        #'xaxis' : 'p_{T} 1st tau',
#                        #'fold'  : 3                         
#                        #}
#
#
#
#
variables['cmva_1']  = { 
                        'name': 'std_vector_jet_cmvav2[0]',     
                        'range' : (40,-1,1),   
                        'xaxis' : 'cmva jet 1st',
                        'fold'  : 3                         
                        }



variables['cmva_2']  = { 
                        'name': 'std_vector_jet_cmvav2[1]',     
                        'range' : (40,-1,1),   
                        'xaxis' : 'cmva  jet 2nd',
                        'fold'  : 3                         
                        }

'''
variables['pfmet']  = { 
                        'name': 'MET_pt',     
                        'range' : (40,0,200),   
                        'xaxis' : 'pfmet [GeV]',
                        'fold'  : 3                         
                        }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }


variables['njet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (5,0,5),   
                        'xaxis' : 'Number of jets',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }




variables['jetpt1']  = {
                        'name': 'CleanJet_pt[0]>30? CleanJet_pt[0]:-1',     
                        'range' : (40,0,200),   
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['jetpt1_0j']  = {
                        'name': 'CleanJet_pt[0]>20? CleanJet_pt[0]:-1',     
                        'range' : (10,20,30),   
                        'xaxis' : 'p_{T} 1st jet (20 < p_{T} < 30) ',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

# variables['jetpt2']  = {
#                         'name': 'CleanJet_pt[1]>30? CleanJet_pt[1]:-1',     
#                         'range' : (40,0,200),   
#                         'xaxis' : 'p_{T} 2nd jet',
#                         'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
#                         }

variables['jeteta1']  = {  'name': 'CleanJet_pt[0]>30? CleanJet_eta[0]:-999',
                        'range' : (80,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0
                        }

# variables['jeteta2']  = {  'name': 'CleanJet_pt[1]>30? CleanJet_eta[1]:-999',
#                         'range' : (80,-5.0,5.0),
#                         'xaxis' : '#eta 2nd jet',
#                         'fold'  : 0
#                         }

'''
variables['mtw1']  = {  'name': 'mtw1',
                        'range' : (40,0,200),
                        'xaxis' : 'm_{T}^{W_{1}} [GeV]',
                         'fold' : 3
                        }

variables['mtw2']  = {  'name': 'mtw2',
                        'range' : (40,0,200),
                        'xaxis' : 'm_{T}^{W_{2}} [GeV]',
                         'fold' : 3
                        }

variables['trkMet']  = {   'name': 'metTtrk',
                        'range' : (40,0,200),
                        'xaxis' : 'trk met [GeV]',
                         'fold' : 3
                        }

variables['mpmet']  = { 'name': 'mpmet',
                        'range' : (40,0,200),
                        'xaxis' : 'min proj met [GeV]',
                        'fold' : 3
                        }

variables['dymvaggh']  = { 'name': 'dymvaggh',
                        'range' : (40,-1,1),
                        'xaxis' : 'DY MVA',
                        'fold' : 3
                        }

'''
                        

