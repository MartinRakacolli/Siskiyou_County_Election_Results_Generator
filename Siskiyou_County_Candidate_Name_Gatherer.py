import pandas as pd

def get_Candidate_Names(data_sheet, list_of_candidates):
    
    index = 7
    
    while index < data_sheet.shape[1]:
        
        cell_contents = data_sheet.iat[2, index]
        
        if pd.notna(cell_contents):
            
            cell_contents = cell_contents
            
            if "Total Votes" not in cell_contents and cell_contents != "":

#                print(cell_contents)
                
                list_of_candidates.append(cell_contents)
        
        index += 1
        