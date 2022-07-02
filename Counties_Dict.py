counties_dict = {'Arapahoe county has': 42289, 'Denver county has': 463353, 'Jefferson county has': 432438}

for key, value in counties_dict.items():
    print(key, value) 

voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
{'county':'Denver', 'registered_voters': 463353},
{'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print (value)


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")