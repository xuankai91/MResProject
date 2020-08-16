#!/usr/bin/env python
# coding: utf-8

##DEFINE NUMBER OF CPU CORES TO USE###
cores_to_use = 3


import hddm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


#define functions
def within_subjects_modelling(flag):

  #load data
  url = 'https://raw.githubusercontent.com/xuankai91/MResProject/master/tofit_HDDM.csv'
  data = hddm.load_csv(url)
  print('data loaded')
  
  samples = 5000
  savepath = './'

  print('starting...')

  if flag == 'all':
    #within subjects model, vary all (Rem reference)
    ws_all = hddm.HDDMRegressor(data, ["a ~ C(stim, Treatment('Rem'))", 
                                      "v ~ C(stim, Treatment('Rem'))", 
                                      "t ~ C(stim, Treatment('Rem'))"], p_outlier=.05)

    ws_all.find_starting_values()

    ws_all.sample(samples*3, burn=samples, thin=2, dbname=savepath + '/models/ws_all_traces.db', db='pickle')
    ws_all.save(savepath + '/models/ws_all')
    #hddm.HDDM.savePatch(m_fixed, './models/WS_all/ws_all')

    ws_all.gen_stats().to_csv(savepath + '/stats/data_WS_all.csv', sep = ',', encoding='utf-8')
    ws_all.get_group_traces().to_csv(savepath + '/traces/data_WS_all_traces.csv', sep = ',', encoding='utf-8')

    print('\n')
    print(ws_all.dic)
    print(ws_all.mc.BPIC)

  elif flag == 'PM':
    #within subjects model, Uad/Rem vs Con (Rem reference)
    ws_pm = hddm.HDDMRegressor(data, ["a ~ C(stim_PM, Treatment('PM'))", 
                                      "v ~ C(stim_PM, Treatment('PM'))", 
                                      "t ~ C(stim_PM, Treatment('PM'))"], p_outlier=.05)

    ws_pm.find_starting_values()

    ws_pm.sample(samples*3, burn=samples, thin=2, dbname=savepath + '/models/ws_pm_traces.db', db='pickle')
    ws_pm.save(savepath + '/models/ws_pm')
    #hddm.HDDM.savePatch(m_fixed, './models/WS_all/ws_all')

    ws_pm.gen_stats().to_csv(savepath + '/stats/data_WS_PM.csv', sep = ',', encoding='utf-8')
    ws_pm.get_group_traces().to_csv(savepath + '/traces/data_WS_PM_traces.csv', sep = ',', encoding='utf-8')

    print('\n')
    print(ws_pm.dic)

  elif flag == 'noPM':
    #within subjects model, Uad vs Rem/Con (Rem reference)
    ws_nopm = hddm.HDDMRegressor(data, ["a ~ C(stim_noPM, Treatment('noPM'))", 
                                      "v ~ C(stim_noPM, Treatment('noPM'))", 
                                      "t ~ C(stim_noPM, Treatment('noPM'))"], p_outlier=.05)

    ws_nopm.find_starting_values()

    ws_nopm.sample(samples*3, burn=samples, thin=2, dbname=savepath + '/models/ws_nopm_traces.db', db='pickle')
    ws_nopm.save(savepath + '/models/ws_nopm')
    #hddm.HDDM.savePatch(m_fixed, './models/WS_all/ws_all')

    ws_nopm.gen_stats().to_csv(savepath + '/stats/data_WS_noPM.csv', sep = ',', encoding='utf-8')
    ws_nopm.get_group_traces().to_csv(savepath + '/traces/data_WS_noPM_traces.csv', sep = ',', encoding='utf-8')

    print('\n')
    print(ws_nopm.dic)
    print(ws_nopm.mc.BPIC)


#start run
from multiprocessing import Pool

if __name__ == '__main__':

  pool = Pool(cores_to_use)

  _ = pool.map(within_subjects_modelling, iterable=['all','PM','noPM'])
 
