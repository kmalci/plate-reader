#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:58:00 2021

@author: Koray Malci
"""

#%%
#import the necessary packages 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# makes figures look better in Jupyter
sns.set_context('talk')
import omniplate as om

#%%
#load the data and its content from the corresponding directory 

p= om.platereader(wdir= 'user/results/')
p.load('Data.xlsx', 'DataContents.xlsx')

#%%

# perform the OD correction using the calibration curve for haploid cells in glucose

p= om.platereader('Data.xlsx', wdir= 'user/results/', ODfname= 'ODcorrection_Glucose_Haploid.txt')
p.correctOD()

#%%

# in order to reorganise the order of the strains, the hue_order argument can be used with an order list
# this is especially very useful if different conditions contain the same strain list

strain_order = ['strain-1', 'strain-2', 'strain-3','strain-4', 'strain-5', 'WT', 'Null']

#biomass for all conditions
#the noshow=True should be used if the figures are not saved without this argument
p.plot(y= 'OD', hue='strain', noshow=True, hue_order=strain_order)

#biomass for a specific condition
p.plot(y= 'OD', conditionincludes='YPD', noshow=True, hue='strain', hue_order =strain_order)
p.plot(y= 'OD', conditionincludes='CSM', noshow=True, hue='strain', hue_order =strain_order)

#to compare different conditions instead of the strains
p.plot(y= 'OD', noshow=True, hue='condition')

p.savefigs(fname='figure.pdf')

#%%

#to find the growth rate estimations
p.getstats(strainincludes='strain-1', conditionincludes= 'YPD')
plt.savefig(fname='figure.pdf')
plt.show()

#%%