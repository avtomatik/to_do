#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:09:16 2022

@author: Alexander Mikhailov
"""

import numpy as np
from pandas import DataFrame

df = DataFrame()
k, b = 0, 0
polyfit_linear = np.polyfit(
    df.iloc[:, -2].astype(float),
    df.iloc[:, -1].astype(float),
    deg=1
)
polyfit_quadrt = np.polyfit(
    df.iloc[:, -2].astype(float),
    df.iloc[:, -1].astype(float),
    deg=2
)
_p3 = np.polyfit(
    df.iloc[:, -2].astype(float),
    df.iloc[:, -1].astype(float),
    deg=3
)
_p4 = np.polyfit(
    df.iloc[:, -2].astype(float),
    df.iloc[:, -1].astype(float),
    deg=4
)
# =========================================================================
# DataFrame for Approximation Results
# =========================================================================
_df = DataFrame()
_df['pow'] = df.iloc[:, -2].pow(k).mul(np.exp(b))
_df['p_1'] = np.poly1d(polyfit_linear)(df.iloc[:, -2])
_df['p_2'] = df.iloc[:, -2].pow(2).mul(polyfit_quadrt[0]).add(df.iloc[:, -2].mul(polyfit_quadrt[1])).add(polyfit_quadrt[2])
_df['p_3'] = df.iloc[:, -2].pow(3).mul(_p3[0]).add(df.iloc[:, -2].pow(2).mul(_p3[1])).add(df.iloc[:, -2].mul(_p3[2])).add(_p3[3])
_df['p_4'] = df.iloc[:, -2].pow(4).mul(_p4[0]).add(df.iloc[:, -2].pow(3).mul(_p4[1])).add(df.iloc[:, -2].pow(2).mul(_p4[2])).add(df.iloc[:, -2].mul(_p4[3])).add(_p4[4])
