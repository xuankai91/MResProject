#!/usr/bin/env python
# coding: utf-8


##DEFINE NUMBER OF CPU CORES TO USE###
cores_to_use = 3

#core function script
def PPC(samples,n=None):
  import hddm

  import pandas as pd
  import pickle
  import os
 
  #set filepath
  filepath = './models/'
  
  #import model
  m = hddm.load(filepath + 'm_all')
  print('model loaded')

  #set savepath
  savepath = './ppc/'

  if not os.path.exists(savepath):
    os.makedirs(savepath)

  #start PP sampling
  print('starting...')
  ppc = hddm.utils.post_pred_gen(m,samples=samples)
  ppc.reset_index(inplace=True)

  print('\nsaving...')
  ppc.to_csv('%s/ppc_%d.csv' % (savepath,n), sep = ',', encoding='utf-8')
  
  print('PP samples saved')

#start run
if __name__ == '__main__':

  from multiprocessing import Pool
  
  from itertools import product
  
  with Pool(cores_to_use) as pool:
    _ = pool.starmap(PPC, product([100],[4,5]))
 


