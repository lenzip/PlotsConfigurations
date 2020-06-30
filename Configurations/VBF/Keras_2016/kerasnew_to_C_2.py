from loader_2016 import *
import ROOT 
import numpy as np  
import pandas as pd
import root_numpy 
import sys

from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dense, Convolution2D, MaxPooling2D, Dropout, Flatten
from keras.utils import np_utils
from keras.constraints import max_norm
from keras import initializers
from keras.regularizers import l2
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.utils import plot_model

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc

#DATA LOAD#

VARS = ['mjj','mll','ptll','detajj', 'dphill', 'PuppiMET_pt', 'PuppiMET_phi', 'mTi', 'dphilljet', 'dphillmet', 'drll', 'dphilmet', 'mR', 'Lepton_pt[0]', 'Lepton_pt[1]', 'Lepton_eta[0]', 'Lepton_eta[1]', 'Lepton_phi[0]', 'Lepton_phi[1]', 'CleanJet_pt[0]', 'CleanJet_pt[1]', 'CleanJet_eta[0]', 'CleanJet_eta[1]', 'CleanJet_phi[0]', 'CleanJet_phi[1]']


NDIM = len(VARS)+5

df = {}

dataset_vbf = load_dataset_vbf ( max_entries=-1 ) 
dataset_top = load_dataset_top ( max_entries=-1 ) 
dataset_ww = load_dataset_ww ( max_entries=-1 ) 
dataset_ggh = load_dataset_ggh ( max_entries=-1 ) 


jetidx0_vbf = dataset_vbf ["CleanJet_jetIdx[0]"]
jetidx1_vbf = dataset_vbf ["CleanJet_jetIdx[1]"]
jetqgl_vbf = dataset_vbf ["Jet_qgl"]
jetpt_vbf = dataset_vbf ["CleanJet_pt"]
jeteta_vbf = dataset_vbf ["CleanJet_eta"]
jetphi_vbf = dataset_vbf ["CleanJet_phi"]

jetqgl0_vbf = []
jetqgl1_vbf = [] 
#jetbtag0_vbf = []
#jetbtag1_vbf = []
jetpt2_vbf = []
jeteta2_vbf = []
jetphi2_vbf = []

jetidx0_top = dataset_top ["CleanJet_jetIdx[0]"]
jetidx1_top = dataset_top ["CleanJet_jetIdx[1]"]
jetqgl_top = dataset_top ["Jet_qgl"]
jetpt_top = dataset_top ["CleanJet_pt"]
jeteta_top = dataset_top ["CleanJet_eta"]
jetphi_top = dataset_top ["CleanJet_phi"]

jetqgl0_top = []
jetqgl1_top = [] 
#jetbtag0_top = []
#jetbtag1_top = []
jetpt2_top = []
jeteta2_top = []
jetphi2_top = []


jetidx0_ww = dataset_ww ["CleanJet_jetIdx[0]"]
jetidx1_ww = dataset_ww ["CleanJet_jetIdx[1]"]
jetqgl_ww = dataset_ww ["Jet_qgl"]
jetpt_ww = dataset_ww ["CleanJet_pt"]
jeteta_ww = dataset_ww ["CleanJet_eta"]
jetphi_ww = dataset_ww ["CleanJet_phi"]

jetqgl0_ww = []
jetqgl1_ww = [] 
#jetbtag0_ww = []
#jetbtag1_ww = []
jetpt2_ww = []
jeteta2_ww = []
jetphi2_ww = []

jetidx0_ggh = dataset_ggh ["CleanJet_jetIdx[0]"]
jetidx1_ggh = dataset_ggh ["CleanJet_jetIdx[1]"]
jetqgl_ggh = dataset_ggh ["Jet_qgl"]
jetpt_ggh = dataset_ggh ["CleanJet_pt"]
jeteta_ggh = dataset_ggh ["CleanJet_eta"]
jetphi_ggh = dataset_ggh ["CleanJet_phi"]

jetqgl0_ggh = []
jetqgl1_ggh = [] 
#jetbtag0_ggh = []
#jetbtag1_ggh = []
jetpt2_ggh = []
jeteta2_ggh = []
jetphi2_ggh = []

print len(jetqgl_vbf)
print len(jetqgl_top)
print len(jetqgl_ww)
print len(jetqgl_ggh)

for i in range (0,len(jetqgl_vbf)):

    if not len(jetidx0_vbf[i]) == 0:
        jetqgl0_vbf.append(jetqgl_vbf[i][jetidx0_vbf[i][0]])
    else:   
        jetqgl0_vbf.append(-1)
    if not len(jetidx1_vbf[i]) == 0:
        jetqgl1_vbf.append(jetqgl_vbf[i][jetidx1_vbf[i][0]])
    else:
        jetqgl1_vbf.append(-1)

    if  (len(jetpt_vbf[i])>2):
        if ( jetpt_vbf[i][2]>30 ):
            jetpt2_vbf.append(jetpt_vbf[i][2])
            jeteta2_vbf.append(jeteta_vbf[i][2])
            jetphi2_vbf.append(jetphi_vbf[i][2])
        else:
            jetpt2_vbf.append(-1)
            jeteta2_vbf.append(-1)
            jetphi2_vbf.append(-1)
    else:
        jetpt2_vbf.append(-1)
        jeteta2_vbf.append(-1)
        jetphi2_vbf.append(-1)
        

for i in range (0,len(jetqgl_top)):

    if not len(jetidx0_top[i]) == 0:
        jetqgl0_top.append(jetqgl_top[i][jetidx0_top[i][0]])
    else:
        jetqgl0_top.append(-1)
    if not len(jetidx1_top[i]) == 0:
        jetqgl1_top.append(jetqgl_top[i][jetidx1_top[i][0]])
    else:
        jetqgl1_top.append(-1)

    if len(jetpt_top[i])>2: 
        if ( jetpt_top[i][2]>30 ):
            jetpt2_top.append(jetpt_top[i][2])
            jeteta2_top.append(jeteta_top[i][2])
            jetphi2_top.append(jetphi_top[i][2])
        else:
            jetpt2_top.append(-1.)
            jeteta2_top.append(-1.)
            jetphi2_top.append(-1.)
    else:
    
        jetpt2_top.append(-1.)
        jeteta2_top.append(-1.)
        jetphi2_top.append(-1.)


for i in range (0,len(jetqgl_ww)):

    if not len(jetidx0_ww[i]) == 0:
        jetqgl0_ww.append(jetqgl_ww[i][jetidx0_ww[i][0]])
    else:   
        jetqgl0_ww.append(-1)
    if not len(jetidx1_ww[i]) == 0:
        jetqgl1_ww.append(jetqgl_ww[i][jetidx1_ww[i][0]])
    else:
        jetqgl1_ww.append(-1)

    if len(jetpt_ww[i])>2:
        if ( jetpt_ww[i][2]>30 ):
            jetpt2_ww.append(jetpt_ww[i][2])
            jeteta2_ww.append(jeteta_ww[i][2])
            jetphi2_ww.append(jetphi_ww[i][2])
        else: 
            jetpt2_ww.append(-1)
            jeteta2_ww.append(-1)
            jetphi2_ww.append(-1)
    else:
        jetpt2_ww.append(-1)
        jeteta2_ww.append(-1)
        jetphi2_ww.append(-1)

for i in range (0,len(jetqgl_ggh)):
    if not len(jetidx0_ggh[i]) == 0:
                jetqgl0_ggh.append(jetqgl_ggh[i][jetidx0_ggh[i][0]])
    else:   
        jetqgl0_ggh.append(-1)
    if not len(jetidx1_ggh[i]) == 0:
                jetqgl1_ggh.append(jetqgl_ggh[i][jetidx1_ggh[i][0]])
    else:
        jetqgl1_ggh.append(-1)

    if len(jetpt_ggh[i])>2: 
        if ( jetpt_ggh[i][2]>30 ):
            jetpt2_ggh.append(jetpt_ggh[i][2])
            jeteta2_ggh.append(jeteta_ggh[i][2])
            jetphi2_ggh.append(jetphi_ggh[i][2])
        else:
            jetpt2_ggh.append(-1.)
            jeteta2_ggh.append(-1.)
            jetphi2_ggh.append(-1.)
    else:
        jetpt2_ggh.append(-1.)
        jeteta2_ggh.append(-1.)
        jetphi2_ggh.append(-1.)


del dataset_vbf["CleanJet_pt"]
del dataset_vbf["CleanJet_eta"]
del dataset_vbf["CleanJet_phi"]
del dataset_vbf["CleanJet_jetIdx[0]"]
del dataset_vbf["CleanJet_jetIdx[1]"]
del dataset_vbf["Jet_qgl"]

del dataset_top["CleanJet_pt"]
del dataset_top["CleanJet_eta"]
del dataset_top["CleanJet_phi"]
del dataset_top["CleanJet_jetIdx[0]"]
del dataset_top["CleanJet_jetIdx[1]"]
del dataset_top["Jet_qgl"]

del dataset_ww["CleanJet_pt"]
del dataset_ww["CleanJet_eta"]
del dataset_ww["CleanJet_phi"]
del dataset_ww["CleanJet_jetIdx[0]"]
del dataset_ww["CleanJet_jetIdx[1]"]
del dataset_ww["Jet_qgl"]

del dataset_ggh["CleanJet_pt"]
del dataset_ggh["CleanJet_eta"]
del dataset_ggh["CleanJet_phi"]
del dataset_ggh["CleanJet_jetIdx[0]"]
del dataset_ggh["CleanJet_jetIdx[1]"]
del dataset_ggh["Jet_qgl"]


df['vbf'] = pd.DataFrame(dataset_vbf,columns=VARS)
df['top'] = pd.DataFrame(dataset_top,columns=VARS)
df['ww'] = pd.DataFrame(dataset_ww,columns=VARS)
df['ggh'] = pd.DataFrame(dataset_ggh,columns=VARS)


df['vbf']['jetpt[2]']= np.asarray(jetpt2_vbf)
df['vbf']['jeteta[2]']= np.asarray(jeteta2_vbf)
df['vbf']['jetphi[2]']= np.asarray(jetphi2_vbf)
df['vbf']['jetqgl[0]']= np.asarray(jetqgl0_vbf)
df['vbf']['jetqgl[1]']= np.asarray(jetqgl1_vbf)

df['top']['jetpt[2]']= np.asarray(jetpt2_top)
df['top']['jeteta[2]']= np.asarray(jeteta2_top)
df['top']['jetphi[2]']= np.asarray(jetphi2_top)
df['top']['jetqgl[0]']= np.asarray(jetqgl0_top)
df['top']['jetqgl[1]']= np.asarray(jetqgl1_top)

df['ww']['jetpt[2]']= np.asarray(jetpt2_ww)
df['ww']['jeteta[2]']= np.asarray(jeteta2_ww)
df['ww']['jetphi[2]']= np.asarray(jetphi2_ww)
df['ww']['jetqgl[0]']= np.asarray(jetqgl0_ww)
df['ww']['jetqgl[1]']= np.asarray(jetqgl1_ww)

df['ggh']['jetpt[2]']= np.asarray(jetpt2_ggh)
df['ggh']['jeteta[2]']= np.asarray(jeteta2_ggh)
df['ggh']['jetphi[2]']= np.asarray(jetphi2_ggh)
df['ggh']['jetqgl[0]']= np.asarray(jetqgl0_ggh)
df['ggh']['jetqgl[1]']= np.asarray(jetqgl1_ggh)

df['vbf']['isVBF'] = np.ones(len(df['vbf']))
df['top']['isVBF'] = np.zeros(len(df['top']))
df['ww']['isVBF'] = np.zeros(len(df['ww']))
df['ggh']['isVBF'] = np.zeros(len(df['ggh']))

df['vbf']['isTOP'] = np.zeros(len(df['vbf']))
df['top']['isTOP'] = np.ones(len(df['top']))
df['ww']['isTOP'] = np.zeros(len(df['ww']))
df['ggh']['isTOP'] = np.zeros(len(df['ggh']))

df['vbf']['isWW'] = np.zeros(len(df['vbf']))
df['top']['isWW'] = np.zeros(len(df['top']))
df['ww']['isWW'] = np.ones(len(df['ww']))
df['ggh']['isWW'] = np.zeros(len(df['ggh']))

df['vbf']['isGGH'] = np.zeros(len(df['vbf']))
df['top']['isGGH'] = np.zeros(len(df['top']))
df['ww']['isGGH'] = np.zeros(len(df['ww']))
df['ggh']['isGGH'] = np.ones(len(df['ggh']))


#KERAS#

model = Sequential()

model.add(Dense(240, kernel_initializer='glorot_normal', activation='relu', input_dim=NDIM))
model.add(Dense(120, kernel_initializer='glorot_normal', activation='relu', kernel_constraint=max_norm(1.)))
model.add(Dense(60, kernel_initializer='glorot_normal', activation='relu', kernel_constraint=max_norm(1.)))
model.add(Dense(4, kernel_initializer='glorot_normal', activation='softmax'))




model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.summary()


df_all = pd.concat([df['vbf'],df['top'],df['ww'],df['ggh']])
dataset = df_all.values
X = dataset[:,0:NDIM]
Y = dataset[:,NDIM:NDIM+4]

X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.2, random_state=7)

'''
scaler = StandardScaler().fit(X_train_val)
X_train_val = scaler.transform(X_train_val)
X_test = scaler.transform(X_test)
'''

early_stopping = EarlyStopping(monitor='val_loss', patience=100)

model_checkpoint = ModelCheckpoint('dense_model.h5', monitor='val_loss',
                                   verbose=0, save_best_only=True,
                                   save_weights_only=False, mode='auto',
                                   period=1)

history = model.fit(X_train_val,
                    Y_train_val,
                    epochs=500,
                    batch_size=500,
                    verbose=1,
                    callbacks=[early_stopping, model_checkpoint],
                    validation_split=0.25)


#CONVERT TO C++


print ("""
// Select all (Ctrl+A), Copy (Ctrl+C), paste to an empty text file (Ctrl+V) and save that file as 'generated_code.h'
// 
// Auto-generated header file. Assumes img to be a floating point array
// of 64 elements (corresponding to an 8x8 b&w image)

#include <math.h>

""")

for iLayer, layer in enumerate(model.layers):
  kernel, bias = layer.get_weights()
  print ("inline float activation_%d (float x, float n) " % iLayer);
  activation =  layer.get_config()['activation'] 
  if activation == 'sigmoid':
    print ("{ return 1./(1 + exp(-x)); }")
  elif activation == 'tanh':
    print ("{ return tanh(x);}")
  elif activation == 'relu':
    print ("{ return x > 0 ? x : 0;}")
  elif activation == 'linear':
    print ("{ return x;}")
  elif activation == 'softmax':
    print ("{ return exp(x)/n ; }")
  else:
    raise KeyError ("Unexpected activation %s"%activation)
  

  
print ("""

float guess_digit (const float *img, int flag)
{

float norma=0;
""")

max_out = 100
for iLayer, layer in enumerate(model.layers):
  print ("  // Declare the arrays in the stack")
  kernel, bias = layer.get_weights()
   
  max_out = max(kernel.shape[1], max_out)
  #print ("  //",bias.shape)
  kernel_values = "{%s}"%(',\n   '.join(["{%s}"%(','.join(["%18.13f"%x for x in row])) for row in kernel]))
  bias_values   = "{%s}"% ( ",".join(["%18.13f"%x for x in bias]))
  print ("  const float kernel_%d[%d][%d] = \n  %s;" % (iLayer, kernel.shape[0], kernel.shape[1],kernel_values))
  print ("  const float bias_%d[%d] = %s;" % (iLayer, bias.shape[0], bias_values))
  
print ("  float buffer_in[%d];" % max_out)
print ("  float buffer_out[%d];" % max_out)

print ("  unsigned int i,j,c; ")

print ("\n\n\n")
print ("  // Load the input in the buffer")
print ("  for (c = 0; c < 64; ++c) \n  buffer_in[c] = img[c];")

for iLayer, layer in enumerate(model.layers):
  kernel, bias = layer.get_weights()

  print ( "  // Processing layer %i " % iLayer )
  print ( """
  for (c = 0; c < {n_out}; ++c ) 
    buffer_out[c] = bias_{iLayer}[c];
    
  for (c = 0; c < {n_out}; ++c )
    for (i = 0; i < {n_in}; ++i)
      buffer_out[c] += buffer_in[i] * kernel_{iLayer}[i][c];
 
  norma=0;
  for(c=0;c<4;++c)
    norma+=exp(buffer_out[c]); 

  // Prepares for next layer 
  for (c = 0; c < {n_out}; ++c )
    buffer_in[c] = activation_{iLayer}(buffer_out[c], norma);
    
  """.format (
      n_in = kernel.shape[0],
      n_out = kernel.shape[1],
      iLayer = iLayer,
  ))
  
last_kernel, last_bias = model.layers[-1].get_weights()
print ("""
  //i = 0;
  //for (c = 0; c < {n_out}; ++c)
  //  if (buffer_in[c] > buffer_in[i])
  //    i = c;
  
  if (flag==0)
    return buffer_in[0];
  else if (flag==1)
    return buffer_in[1];
  else if (flag==2)
    return buffer_in[2];
  else if (flag==3)
    return buffer_in[3];
  else
    return -1;
  //return i;
""".format(n_out = last_kernel.shape[1]))

print ("}")


#PLOTS#

g_loss = ROOT.TGraph(len(history.history['loss']))
for i,val in enumerate(history.history['loss']):
  g_loss.SetPoint(i,i,val)

c1 = ROOT.TCanvas()
c1.cd()

g_loss.SetTitle('Loss Function')
g_loss.GetXaxis().SetTitle('Epoch')
g_loss.GetYaxis().SetTitle('Loss')
g_loss.SetLineColor(ROOT.kRed)
g_loss.SetLineWidth(3)
g_loss.Draw()

g_val_loss = ROOT.TGraph(len(history.history['val_loss']))
for i,val in enumerate(history.history['val_loss']):
  g_val_loss.SetPoint(i,i,val)

g_val_loss.SetLineColor(ROOT.kBlue)
g_val_loss.SetLineWidth(3)
g_val_loss.Draw('same')

leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg.AddEntry(g_loss,'Training sample')
leg.AddEntry(g_val_loss,'Validation sample')
leg.Draw('same')

c1.Draw()

Y_predict = model.predict(X_test)

vbf_pred_vbf = ROOT.TH1F('vbf_pred_vbf','vbf prediction',20,0,1)
vbf_pred_top  = ROOT.TH1F('vbf_pred_top','vbf prediction',20,0,1)
vbf_pred_ww  = ROOT.TH1F('vbf_pred_ww','vbf prediction',20,0,1)
vbf_pred_ggh  = ROOT.TH1F('vbf_pred_ggh','vbf prediction',20,0,1)


top_pred_vbf = ROOT.TH1F('top_pred_vbf','top prediction',20,0,1)
top_pred_top  = ROOT.TH1F('top_pred_top','top prediction',20,0,1)
top_pred_ww  = ROOT.TH1F('top_pred_ww','top prediction',20,0,1)
top_pred_ggh  = ROOT.TH1F('top_pred_ggh','top prediction',20,0,1)

ww_pred_vbf = ROOT.TH1F('ww_pred_vbf','ww prediction',20,0,1)
ww_pred_top  = ROOT.TH1F('ww_pred_top','ww prediction',20,0,1)
ww_pred_ww  = ROOT.TH1F('ww_pred_ww','ww prediction',20,0,1)
ww_pred_ggh  = ROOT.TH1F('ww_pred_ggh','ww prediction',20,0,1)

ggh_pred_vbf = ROOT.TH1F('ggh_pred_vbf','ggh prediction',20,0,1)
ggh_pred_top  = ROOT.TH1F('ggh_pred_top','ggh prediction',20,0,1)
ggh_pred_ww  = ROOT.TH1F('ggh_pred_ww','ggh prediction',20,0,1)
ggh_pred_ggh  = ROOT.TH1F('ggh_pred_ggh','ggh prediction',20,0,1)


for i in range (0, len(Y_predict)):
    if(Y_test[i][0]==1.):
        vbf_pred_vbf.Fill(Y_predict[i][0])
        top_pred_vbf.Fill(Y_predict[i][1]) 
        ww_pred_vbf.Fill(Y_predict[i][2])
        ggh_pred_vbf.Fill(Y_predict[i][3])
    elif(Y_test[i][1]==1.): 
        vbf_pred_top.Fill(Y_predict[i][0])
        top_pred_top.Fill(Y_predict[i][1])
        ww_pred_top.Fill(Y_predict[i][2])
        ggh_pred_top.Fill(Y_predict[i][3])
    elif(Y_test[i][2]==1.):
        vbf_pred_ww.Fill(Y_predict[i][0])
        top_pred_ww.Fill(Y_predict[i][1])
        ww_pred_ww.Fill(Y_predict[i][2])
        ggh_pred_ww.Fill(Y_predict[i][3])
    elif(Y_test[i][3]==1.): 
        vbf_pred_ggh.Fill(Y_predict[i][0])
        top_pred_ggh.Fill(Y_predict[i][1])
        ww_pred_ggh.Fill(Y_predict[i][2])
        ggh_pred_ggh.Fill(Y_predict[i][3])



count=0.
norm=0.

for i in range (0, len(Y_predict)):
    if(Y_test[i][0]==1.):
        norm=norm+1.        
        if (Y_predict[i][0] > Y_predict[i][1] and Y_predict[i][0] > Y_predict[i][2] and Y_predict[i][0] > Y_predict[i][3]):
            count=count+1.

eff = count / norm

print norm
print count
print eff

count=0.
countvbf=0.

for i in range (0, len(Y_predict)):
    if(Y_test[i][0]==1.):
        if (Y_predict[i][0] > Y_predict[i][1] and Y_predict[i][0] > Y_predict[i][2] and Y_predict[i][0] > Y_predict[i][3]):
            countvbf=countvbf+1.
            count=count+1.
    if(Y_test[i][1]==1.):
        if (Y_predict[i][0] > Y_predict[i][1] and Y_predict[i][0] > Y_predict[i][2] and Y_predict[i][0] > Y_predict[i][3]):
            count=count+1.
    if(Y_test[i][2]==1.):
        if (Y_predict[i][0] > Y_predict[i][1] and Y_predict[i][0] > Y_predict[i][2] and Y_predict[i][0] > Y_predict[i][3]):
            count=count+1.
    if(Y_test[i][3]==1.):
        if (Y_predict[i][0] > Y_predict[i][1] and Y_predict[i][0] > Y_predict[i][2] and Y_predict[i][0] > Y_predict[i][3]):
            count=count+1.

purezza = countvbf / count

print purezza

vbf_pred_vbf.SetStats(0)
vbf_pred_top.SetStats(0)
vbf_pred_ww.SetStats(0)
vbf_pred_top.SetStats(0)
top_pred_vbf.SetStats(0)
top_pred_vbf.SetStats(0)
top_pred_top.SetStats(0)
top_pred_ww.SetStats(0)
ww_pred_vbf.SetStats(0)
ww_pred_top.SetStats(0)
ww_pred_ww.SetStats(0)
ww_pred_top.SetStats(0)
ggh_pred_vbf.SetStats(0)
ggh_pred_top.SetStats(0)
ggh_pred_ww.SetStats(0)
ggh_pred_top.SetStats(0)



vbf_pred_vbf.GetXaxis().SetTitle('vbf output')
vbf_pred_vbf.GetYaxis().SetTitle('A.U.')
vbf_pred_vbf.SetLineColor(ROOT.kBlue)
vbf_pred_top.SetLineColor(ROOT.kRed)
vbf_pred_ww.SetLineColor(ROOT.kGreen)
vbf_pred_ggh.SetLineColor(ROOT.kBlack)

top_pred_vbf.GetXaxis().SetTitle('top output')
top_pred_vbf.GetYaxis().SetTitle('A.U.')
top_pred_vbf.SetLineColor(ROOT.kBlue)
top_pred_top.SetLineColor(ROOT.kRed)
top_pred_ww.SetLineColor(ROOT.kGreen)
top_pred_ggh.SetLineColor(ROOT.kBlack)

ww_pred_vbf.GetXaxis().SetTitle('ww output')
ww_pred_vbf.GetYaxis().SetTitle('A.U.')
ww_pred_vbf.SetLineColor(ROOT.kBlue)
ww_pred_top.SetLineColor(ROOT.kRed)
ww_pred_ww.SetLineColor(ROOT.kGreen)
ww_pred_ggh.SetLineColor(ROOT.kBlack)

ggh_pred_vbf.GetXaxis().SetTitle('ggh output')
ggh_pred_vbf.GetYaxis().SetTitle('A.U.')
ggh_pred_vbf.SetLineColor(ROOT.kBlue)
ggh_pred_top.SetLineColor(ROOT.kRed)
ggh_pred_ww.SetLineColor(ROOT.kGreen)
ggh_pred_ggh.SetLineColor(ROOT.kBlack)


leg_pred = ROOT.TLegend(0.6,0.7,0.9,0.9)
leg_pred.AddEntry(vbf_pred_vbf,'vbf')
leg_pred.AddEntry(vbf_pred_top,'top')
leg_pred.AddEntry(vbf_pred_ww,'ww')
leg_pred.AddEntry(vbf_pred_ggh,'ggh')

c_vbf = ROOT.TCanvas()
c_vbf.cd()

vbf_pred_vbf.Draw()
vbf_pred_top.Draw('same')
vbf_pred_ww.Draw('same')
vbf_pred_ggh.Draw('same')
leg_pred.Draw('same')

c_vbf.Draw()


c_top = ROOT.TCanvas()
c_top.cd()

top_pred_vbf.Draw()
top_pred_top.Draw('same')
top_pred_ww.Draw('same')
top_pred_ggh.Draw('same')
leg_pred.Draw('same')

c_top.Draw()


c_ww = ROOT.TCanvas()
c_ww.cd()

ww_pred_vbf.Draw()
ww_pred_top.Draw('same')
ww_pred_ww.Draw('same')
ww_pred_ggh.Draw('same')
leg_pred.Draw('same')


c_ww.Draw()


c_ggh = ROOT.TCanvas()
c_ggh.cd()

ggh_pred_vbf.Draw()
ggh_pred_top.Draw('same')
ggh_pred_ww.Draw('same')
ggh_pred_ggh.Draw('same')
leg_pred.Draw('same')


c_ggh.Draw()

#plot_model(model, to_file='model.png', show_shapes=True)

f = ROOT.TFile("dnn_plots.root","RECREATE")
c1.Write()
c_vbf.Write()
c_top.Write()
c_ww.Write()
c_ggh.Write()
f.Close()

del f




input()
