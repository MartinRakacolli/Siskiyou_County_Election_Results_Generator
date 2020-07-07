import pandas as pd
import numpy as np

def get_Precinct_Names(data_sheet, list_of_precincts):
    
    for index, row in data_sheet.iterrows():
        if row.ix[0] != "Provisional" and row.ix[0] != "Total" and row.ix[0] != "Election Day" and row.ix[0] != "Vote by Mail" and row.ix[0] != "Cumulative" and row.ix[0] != "Cumulative - Total" and row.ix[0] != "Countywide - Total" and row.ix[0] != "Electionwide - Total" and pd.notna(row.ix[0]) and row.ix[0] != "Precinct" and row.ix[0] != "Countywide" and row.ix[0] != "Electionwide":
            list_of_precincts.append(row.ix[0])