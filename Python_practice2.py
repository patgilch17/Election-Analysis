#temperature = float(input("What is the temperature outside? "))


#if temperature > 80:
#    print(f"Turn on the AC.")
#else:
#    print("Open the windows.")

#x = 0
#while x <= 5:
#    print(x)
#    x = x + 1

#counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

#for county in counties_dict:
#    print(county)

#for i in counties_dict.values():
#    print(i)

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")
#    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# Prints each dictionary at a time on a new line
#for county_dict in voting_data:
#    print(county_dict)

#prints each county name using the range method
#for i in range(len(voting_data)):
#    print(voting_data[i]['county'])

#prints each county name without range
#for county_dict in voting_data:
#    print(county_dict['county'])

#prings each of the registered voters for each county
#for county_dict in voting_data:
#    print(county_dict['registered_voters'])

#prints the county name value on one line then the # of registered voters for that county on the next line then moves on
# to the next county (dictionary) since there are only 2 data points per dictionary
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes/total_votes*100}% of the total votes.")
#done without the fstring with concatanation and casting

for county_dict in voting_data:
    countyname = county_dict['county']
    regvote = county_dict['registered_voters']

    print(f"{countyname} county has {regvote:,} registered voters.")
