#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:39:21 2020

@author: shihyu
"""
import pandas as pd
from scipy.stats import hypergeom
import numpy as np


C=pd.read_excel("dataC.xlsx")#Include informations of Gene name and recurrence
C['sample_size']=31
C['ratio']=dataC['recurrence']/dataC['sample_size']


#Merge data from 2 references and calculate pmf/cdf
P=pd.read_excel('dataP.xlsx')[['Gene','Counts', 'Sample Size', 'Ratio']]
L=pd.read_excel('dataL.xlsx')[['Gene','Counts', 'Sample Size', 'Ratio']]

ary=pd.merge(dataC,P, on='Gene', how='outer')
finaldf=pd.merge(ary,L,on='Gene',how='outer',suffixes=('_P','_L')).fillna(0)
finaldf['Sample Size_P']=428
finaldf['Sample Size_L']=538
finaldf['Sample size_C']=31

finaldf['pmf_P']=hypergeom(finaldf['Sample Size_P'],finaldf['Counts_P'],finaldf['Sample size_C']).pmf(finaldf['recurrence']).round(decimals=7)
finaldf['cdf_P']=hypergeom.cdf(finaldf['recurrence'],finaldf['Sample Size_P'],finaldf['Counts_P'],finaldf['Sample size_C']).round(decimals=3)

finaldf['pmf_L']=hypergeom(finaldf['Sample Size_L'],finaldf['Counts_L'],finaldf['Sample size_C']).pmf(finaldf['recurrence']).round(decimals=7)
finaldf['cdf_L']=hypergeom.cdf(finaldf['recurrence'],finaldf['Sample Size_L'],finaldf['Counts_L'],finaldf['Sample size_C']).round(decimals=3)

finaldf.to_excel('hypergeometric_test.xlsx')

