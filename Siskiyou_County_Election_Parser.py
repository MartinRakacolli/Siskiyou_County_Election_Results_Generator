import pandas as pd
from Siskiyou_County_Election_Precinct_Name_Gatherer import get_Precinct_Names
from Siskiyou_County_Office_Name_Gatherer import get_Offices
from Siskiyou_County_Candidate_Name_Gatherer import get_Candidate_Names
from Siskiyou_County_Votes_Gatherer import get_Votes_For_Candidate

def main():

    county = "Siskiyou"
    list_of_precincts = []
    list_of_offices = []
    district = ""
    party = ""
    
    sheet_1 = pd.read_excel('Siskiyou_County_Results_2020.xlsx', sheet_name = 'Sheet1')
    get_Precinct_Names(sheet_1, list_of_precincts)
    
    organized_results = pd.DataFrame(columns = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes', 'early_voting', 'election_day', 'provisional', 'mail'])
    
    pd.options.display.float_format = '{:,.0f}'.format
    pd.set_option('display.max_columns', None)
    
    for x in range(2, 17):
        
        data_sheet = pd.read_excel('Siskiyou_County_Results_2020.xlsx', sheet_name = 'Sheet{}'.format(x))
        
        office = get_Offices(data_sheet, list_of_offices)
        
        list_of_candidates_for_office = []
        
        if "DISTRICT ONE" in office:
            district = "DISTRICT ONE"
        elif "ASSEMBLY DISTRICT ONE" in office:
            district = "ASSEMBLY DISTRICT ONE"
        elif "UNITED STATES REPRESENTATIVE" in office:
            district = "CALIFORNIA 1ST CONGRESSIONAL DISTRICT"
        elif "STATE SENATOR DISTRICT ONE" in office:
            district = "CALIFORNIA STATE SENATE DISTRICT ONE"
        elif "SUPERVISOR DISTRICT 1" in office:
            district = "SUPERVISOR DISTRICT ONE"
        elif "SUPERVISOR DISTRICT 2" in office:
            district = "SUPERVISOR DISTRICT TWO"
        elif "SUPERVISOR DISTRICT 4" in office:
            district = "SUPERVISOR DISTRICT FOUR"
            
        if "DEMOCRATIC" in office:
            party = "DEMOCRAT"
        elif "REPUBLICAN" in office:
            party = "REPUBLICAN"
        elif "AMERICAN INDEPENDENT" in office:
            party = "AMERICAN INDEPENDENT"
        elif "GREEN" in office:
            party = "GREEN PARTY"
        elif "LIBERTARIAN" in office:
            party = "LIBERTARIAN"
        elif "PEACE AND FREEDOM" in office:
            party = "PEACE AND FREEDOM"
        else:
            party = "NONPARTISAN"
        
        get_Candidate_Names(data_sheet, list_of_candidates_for_office)

        for candidate in list_of_candidates_for_office:
            
            if 'GREGORY EDWARD CHEADLE' in candidate or 'JOSEPH LETOURNE AU IV' in candidate or 'LINDA KELLEHER' in candidate or 'PK "PAUL" DHANUKA' in candidate:
                party = "INDEPENDENT"
            elif 'KENNETH SWANSON' in candidate or 'DOUG LAMALFA' in candidate or 'BRIAN DAHLE' in candidate or 'MEGAN DAHLE' in candidate:
                party = "REPUBLICAN"
            elif 'ROB LYDON' in candidate or 'AUDREY DENNEY' in candidate or 'PAMELA DAWN SWARTZ' in candidate or 'ELIZABETH L BETANCOURT' in candidate:
                party = "DEMOCRAT"
            
            organized_results = get_Votes_For_Candidate(organized_results, candidate, data_sheet, county, list_of_precincts, office, district, party)
            
    organized_results.to_csv('20200303__ca__primary__siskiyou__precinct.csv', index = False)
            
main()