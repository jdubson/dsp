# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import urllib2

url = 'https://raw.githubusercontent.com/jdubson/dsp/master/python/football.csv'
data = urllib2.urlopen(url)

def read_data(data):
    football_csv = csv.reader(data)
    football_data = []

    for row in football_csv:
        football_data.append(row)

    return football_data


def get_min_score_difference(parsed_data):
    header = parsed_data[0]
    parsed_data.pop(0)
    header.append("Goal Difference")

    for i in range(len(parsed_data)):
        diff = abs(int(parsed_data[i][5]) - int(parsed_data[i][6]))
        parsed_data[i].append(diff)

    parsed_data.sort(key = lambda x: x[-1])

    return parsed_data


def get_team(index_value, parsed_data):
    team = parsed_data[index_value][0]
    return team

football = read_data(data)
min_score = get_min_score_difference(football)
print get_team(0, min_score)
