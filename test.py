# import pandas as pd
#
# test_csv = pd.read_csv(filepath_or_buffer='./50_states.csv')
# print(test_csv)
# print(test_csv[['x', 'y']])
# print(test_csv[test_csv['state'] == 'Ohio'])
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']])
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].index)
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].index == 34)
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].to_dict())
# # print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].tolist())
# print(type(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']]))
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].iloc[0])
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].loc[34])
# print(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].loc[34].tolist())
# print(tuple(test_csv[test_csv['state'] == 'Ohio'][['x', 'y']].loc[34]))

# a_dict = {'a': 1, 'b': 4, 'c': 8, 'd': 9, 'e': 3, 'f': 2, 'g': 6, 'h': 5}
# print(a_dict)
# print(a_dict.items())
# # func = lambda x: x[0]  # <--- learned something new; do not assign a lambda expression - PEP8
# print(sorted(a_dict.items(), key=lambda x: x[1]))
