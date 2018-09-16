import pandas as pd
import matplotlib.pyplot as plt


#Read in the data from USDA provided data

USDA_full = pd.DataFrame()

def read_USDA_file(df):

    USDA_dict = pd.read_excel('disaster_summary_USDA.xls', sheet_name=None, ignore_index=True)
    for sheet in USDA_dict:
        df = df.append(USDA_dict[sheet])
        print(df.tail())
    return df

read_USDA_file(USDA_full)

print(USDA_full[-1:-5].tail())


"""
index_yr_num_loc = ['CROP DISASTER YEAR', 'State', 'County']
index_sdate_loc = ['Begin Date', 'State']


def event_by_year_geo(df):
    # show classified events occurring each crop year by location
    df = df.set_index(index_yr_num_loc)
    df = df.sort_index()
    return df

def time_series_by_loc(df):
    # show events occurring over time by location
    df = df.set_index(index_sdate_loc)
    df = df.sort_index()
    return df

event_by_year_geo(USDA_full)



print(USDA_full)
"""


"""

#Read in the data from FEMA provided data
#FEMA = pd.read_csv('DisasterDeclarationsSummariesFEMA.csv')

##time_series_by_loc(USDA_full)
print(USDA_full.index)
"""