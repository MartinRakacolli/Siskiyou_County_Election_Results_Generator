def get_Offices(data_sheet, list_of_offices):
    
    return data_sheet.iat[0, 0].split(" (")[0]