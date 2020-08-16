#!/usr/bin/env python
# coding: utf-8

##DEFINE NUMBER OF CPU CORES TO USE###
cores_to_use = 2

#core function script
def between_subjects_modelling(flag,n=None):

  import hddm

  import pandas as pd
  import pickle
  import os

  #load data
  data = hddm.load_csv('https://raw.githubusercontent.com/xuankai91/MResProject/master/tofit_HDDM.csv')
  print('data loaded')
  
  #setup
  samples = 5000
  savepath = './'

  #create save folders
  fdrs = ['models', 'stats', 'traces']

  for i in range(len(fdrs)):
    if not os.path.exists(savepath + fdrs[i]):
      os.makedirs(savepath + fdrs[i])
            
  del fdrs #clear variable
  
  #start modelling
  print('starting...')

  #instantiate model object
  if flag == 'all':
    model = hddm.HDDM(data, 
                      depends_on={'v':'stim','a':'stim','t':'stim'},
                      include=('sv', 'st', 'sz'),
                      p_outlier=.05)
  elif flag == 'PM':
    model = hddm.HDDM(data, 
                      depends_on={'v':'stim_PM','a':'stim_PM','t':'stim_PM'},
                      include=('sv', 'st', 'sz'),
                      p_outlier=.05)
  elif flag == 'noPM':
    model = hddm.HDDM(data, 
                      depends_on={'v':'stim_noPM','a':'stim_noPM','t':'stim_noPM'},
                      include=('sv', 'st', 'sz'),
                      p_outlier=.05)
  elif flag == 'null':
    model = hddm.HDDM(data, 
                      include=('sv', 'st', 'sz'),
                      p_outlier=.05)
  elif flag == 'grs':
    model = hddm.HDDM(data, 
                      depends_on={'v':'stim','a':'stim','t':'stim'},
                      include=('sv', 'st', 'sz'),
                      p_outlier=.05)
    flag = '%s_%d' % (flag,n)
 
  #start model fitting
  model.find_starting_values()
  model.sample(samples, burn=int(samples/10), dbname='%s/models/m_%s_traces.db' % (savepath,flag), db='pickle')
  model.save('%s/models/m_%s' % (savepath,flag))

  model.gen_stats().to_csv('%s/stats/data_%s.csv' % (savepath,flag), sep = ',', encoding='utf-8')
  model.get_group_traces().to_csv('%s/traces/data_%s_traces.csv' % (savepath,flag), sep = ',', encoding='utf-8')
  
  #print('\n')
  #print(model.dic)
  #print(model.mc.BPIC)


#start run
from multiprocessing import Pool

if __name__ == '__main__':

  #pool = Pool(cores_to_use)
  #_ = pool.map(between_subjects_modelling, iterable=['all','PM','noPM','null'])
  
  from itertools import product
  
  with Pool(cores_to_use) as pool:
    _ = pool.starmap(between_subjects_modelling, product(['grs'],[4,5]))
 
