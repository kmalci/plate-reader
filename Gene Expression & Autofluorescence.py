#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:28:00 2021

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

# apply the corrections for OD and autofluorescence

p= om.platereader('Data.xlsx', wdir= 'user/results/', ODfname= 'ODcorrection_Glucose_Haploid.txt')
p.correctOD()
p.correctmedia(['GFP', 'AutoFL'])
p.correctauto(['GFP', 'AutoFL'], refstrain= 'WT')

#%%

# in order to reorganise the order of the strains, the hue_order argument can be used with an order list
# this is especially very useful if different conditions contain the same strain list

strain_order = ['strain-1', 'strain-2', 'strain-3','strain-4', 'strain-5', 'WT', 'Null']

#to change the color palette on the plots
sns.set_palette("tab10")

#plotting corrected GFP per OD 
#the noshow=True should be used if the figures are not saved without this argument
p.plot(y= 'c-GFPperOD', conditionincludes='YPD', noshow=True, hue='strain', hue_order =strain_order)
p.savefigs(fname='figureGFP1.pdf')

#plotting for a particular strain
p.plot(y= 'c-GFPperOD', conditions=['YPD', 'CSM'], hue= 'strain', 
       style= 'condition', nonull= True, strainincludes= ['strain-1'])
p.savefigs(fname='figureGFP2.pdf')

#comparing different conditions instead of the strains 
media=['YPD', 'CSM']
p.plot(y= 'c-GFPperOD', hue='condition', style='condition', style_order=media, hue_order =media, noshow=True)
p.savefigs(fname='figureGFP3.pdf')

#%%

#finding time-derivate fluorescences 

p.getstats('c-GFPperOD', conditions= ['YPD'], strains= ['strain-1'], logs= False, findareas= False)
#%%