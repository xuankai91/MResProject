#!/usr/bin/env python
# coding: utf-8

##DEFINE NUMBER OF CPU CORES TO USE###
cores_to_use = 2

#core function script
def gelman_rubin_models(n):

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
  if not os.path.exists(savepath + 'gelman_rubin'):
    os.makedirs(savepath + 'gelman_rubin')

  #start modelling
  print('starting...')

  #instantiate model object
  model = hddm.HDDM(data,depends_on={'v':'stim','a':'stim','t':'stim'},include=('sv', 'st', 'sz'),p_outlier=.05)
 
  #start model fitting
  model.find_starting_values()
  model.sample(samples, burn=int(samples/10), dbname='%s/gelman_rubin/m_grs_%d_traces.db' % (savepath,n), db='pickle')
  model.save('%s/gelman_rubin/m_grs_%d' % (savepath,n))

  #model.gen_stats().to_csv('%s/stats/data_grs_%d.csv' % (savepath,n), sep = ',', encoding='utf-8')
  #model.get_group_traces().to_csv('%s/traces/data_grs_%d_traces.csv' % (savepath,n), sep = ',', encoding='utf-8')
  

#start run
if __name__ == '__main__':

  from multiprocessing import Pool

  pool = Pool(cores_to_use)
  _ = pool.map(gelman_rubin_models, iterable=list(range(1,6)))
  

 
