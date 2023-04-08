#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:30:16 2022

@author: Alexander Mikhailov
"""

# =============================================================================
# TODO: CHECK IT
# =============================================================================
# =============================================================================
# SERIES_IDS = {
#     # 'CDT2S1': ('cobbdouglas.csv', 1, 'nominal, millions'),
#     # 'P0107': ('uscb.csv', 1000, 'nominal, billions'),
#     'CDT2S3': ('cobbdouglas.csv', 1, '1880=100, millions'),
#     'P0119': ('uscb.csv', 1000, '1958=100, billions'),
# }
# =============================================================================


SERIES_IDS = """'i3ptotl1es00': 'Investment in Fixed Assets and Consumer Durable Goods, Private'
'icptotl1es00': 'Chain-Type Quantity Indexes for Investment in Fixed Assets and Consumer Durable Goods, Private'
'k1n31gd1es00': 'Table 3.1ESI. Current-Cost Net Stock of Private Fixed Assets by Industry'
'k1ntotl1si00': 'Table 4.1. Current-Cost Net Stock of Private Nonresidential Fixed Assets by Industry Group and Legal Form of Organization'
'k1ptotl1es00': 'Current-Cost Net Stock of Fixed Assets, Private'
'k3n31gd1eq00': 'None'
'k3n31gd1es00': 'OK'
'k3n31gd1ip00': 'None'
'k3n31gd1st00': 'None'
'k3ntotl1si00': 'OK'
'k3ptotl1es00': 'Historical-Cost Net Stock of Private Fixed Assets, Private Fixed Assets'
'kcn31gd1es00': 'None'
'kcntotl1si00': 'None'
'kcptotl1es00': 'Chain-Type Quantity Indexes for Net Stock of Fixed Assets, Private'
'mcn31gd1es00': 'None'
'mcntotl1si00': 'None'"""

# =============================================================================
# =============================================================================
# annotations.py
# =============================================================================

# =============================================================================

{
    "collect_usa_capital": {
        # =========================================================================
        # Used
        # =========================================================================
        'k1n31gd1es00': 'https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
        # =========================================================================
        # Not Used
        # =========================================================================
        # =========================================================================
        # Nominal Fixed Assets, k3n31gd1es00, Billions of Dollars
        # =========================================================================
        'k3n31gd1es00': 'https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
        # =========================================================================
        # Not Used
        # =========================================================================
        # =========================================================================
        # Used Elsewhere
        # =========================================================================
        # =========================================================================
        # Nominal Fixed Assets, k3ntotl1si00, Billions of Dollars
        # =========================================================================
        'k3ntotl1si00': 'https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt',
    }
}
# =============================================================================
# project_usa_bea.py
# =============================================================================
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:17:48 2020
@author: Alexander Mikhailov
"""
# =============================================================================
# collect_usa_general
# INITIAL
# (
#     "i3ptotl1es00",
#     "icptotl1es00",
#     "k1ptotl1es00",
#     "k3ptotl1es00",
#     "kcptotl1es00",
# )
# FINAL
# (
#     "k1n31gd1es00",
#     "i3ptotl1es00",
#     "icptotl1es00",
#     "k3ptotl1es00",
# )
# =============================================================================
