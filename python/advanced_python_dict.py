import csv
import urllib2
import pandas as pd

url = 'https://raw.githubusercontent.com/jdubson/dsp/master/python/faculty.csv'
data = urllib2.urlopen(url)

def read_data(data):
    faculty_csv = csv.reader(data)

    faculty_data = []

    for row in faculty_csv:
        faculty_data.append(row)

    header = faculty_data[0]
    faculty_data.pop(0)
    faculty_df = pd.DataFrame(faculty_data, columns = header)

    return faculty_df


def dict_last(parsed_data):
    loc_df = parsed_data.copy()
    # Keep only last names
    loc_df[loc_df.columns[0]] = loc_df[loc_df.columns[0]].str.replace('^.{1,10}(\s.{0,10})?\s', '')
    dict_ln = dict()
    for i in range(len(loc_df)):
        if loc_df[loc_df.columns[0]][i] in dict_ln:
            dict_ln[loc_df[loc_df.columns[0]][i]].append([loc_df[loc_df.columns[1]][i],
                                                          loc_df[loc_df.columns[2]][i],
                                                          loc_df[loc_df.columns[3]][i]])
        else:
            dict_ln[loc_df[loc_df.columns[0]][i]] = [[loc_df[loc_df.columns[1]][i],
                                                      loc_df[loc_df.columns[2]][i],
                                                      loc_df[loc_df.columns[3]][i]]]
    return dict_ln



def dict_full(parsed_data):
    loc_df_2 = parsed_data.copy()
    # Keep only first and last names
    loc_df_2[loc_df_2.columns[0]] = loc_df_2[loc_df_2.columns[0]].str.replace('^[A-Z][.]\s', '')
    loc_df_2[loc_df_2.columns[0]] = loc_df_2[loc_df_2.columns[0]].str.replace('\s.{1,10}\s', ' ')

    dict_fn = dict()

    for i in range(len(loc_df_2)):
        split_name = loc_df_2[loc_df_2.columns[0]][i].split()
        dict_fn[(split_name[0], split_name[1])] = [loc_df_2[loc_df_2.columns[1]][i],
                                                   loc_df_2[loc_df_2.columns[2]][i],
                                                   loc_df_2[loc_df_2.columns[3]][i]]

    return dict_fn


def dict_sort(parsed_data):
    dict_sorted = dict_full(parsed_data)
    return sorted(dict_sorted.items(), key=lambda (x, y): (x[1], y))



df = read_data(data)
print dict_last(df)
print dict_full(df)
print dict_sort(df)
