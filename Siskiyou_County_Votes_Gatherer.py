def get_Votes_For_Candidate(organized_results, candidate, data_sheet, county, list_of_precincts, office, district, party):
    
    y_depth = 5
    index = 7
    
    cell_contents = data_sheet.iat[2, index]
    
    while cell_contents != candidate:
        
        index += 1
        
        cell_contents = data_sheet.iat[2, index]
    
    precinct = data_sheet.iat[y_depth, 0]
    
    while precinct in list_of_precincts:
        
        election_day_vote = data_sheet.iat[y_depth + 1, index]
        vote_by_mail_vote = data_sheet.iat[y_depth + 2, index]
        provisional_vote = data_sheet.iat[y_depth + 3, index]
        total_vote = data_sheet.iat[y_depth + 4, index]
        early_voting = vote_by_mail_vote + provisional_vote
        
        organized_results = organized_results.append({'county' : county, 'precinct' : precinct, 'office' : office, 'district' : district, 'party' : party, 'candidate' : candidate, 'votes' : total_vote, 'early voting' : early_voting, 'election day' : election_day_vote, 'provisional' : provisional_vote, 'mail' : vote_by_mail_vote}, ignore_index = True)
        
        y_depth += 5
        precinct = data_sheet.iat[y_depth, 0]
    
    return organized_results