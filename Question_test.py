voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
{'county':'Denver', 'registered_voters': 463353},
{'county':'Jefferson', 'registered_voters': 432438}]


for county_dict in voting_data:
 for county, voter in county_dict.items():
     print (county, voter)