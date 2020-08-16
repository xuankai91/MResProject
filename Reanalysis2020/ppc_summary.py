#!/usr/bin/env python
# coding: utf-8

import hddm
import pandas as pd

FILEPATH ="D:/Documents/MRes Project/Reanalysis2020/"
data = hddm.load_csv('https://raw.githubusercontent.com/xuankai91/MResProject/master/tofit_HDDM.csv')


#load PPCs
ppc = []

for i in range(1,6):
    ppc.append(pd.read_csv(FILEPATH + 'ppc/ppc_%d.csv' % i))
    
for i,n in enumerate(list(range(0,500,100))):
    ppc[i]['sample'] = ppc[i]['sample']+n

print('pp samples loaded.\n')

ppc_data = pd.concat([ppc[i] for i in range(5)]).drop('Unnamed: 0',axis=1)

ppc_data = ppc_data.set_index(['node','sample','level_2']).rename_axis(index=['node','sample',None])

#summary stats
ppc_compare = hddm.utils.post_pred_stats(data, ppc_data)
ppc_compare.to_csv('ppc/summary_stats.csv')

#invidual stats
ppc_compare_ind = hddm.utils.post_pred_stats(data, ppc_data,call_compare=False)
ppc_compare_ind = ppc_compare_ind.groupby(['node']).mean().drop('sample',axis=1) #groupby condition x subject
ppc_compare_in.to_csv('ppc/individual_stats.csv')

print('summary stats saved.')