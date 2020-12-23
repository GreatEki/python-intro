import time
import os
import pandas


# Reading froma csv file in python
def readFile():
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read_csv('files/temps_today.csv')
        # print(data.mean()['st2'])
        return data.mean()['st2']
    else:
        # print('File does not exist')
        return 'File does not exist'

print(readFile())

# while True:
#     if os.path.exists('files/temps_today.csv'):
#         data = pandas.read_csv('files/temps_today.csv')
#         print(data.mean())
#     else:
#         print('File Does Not Exist')
#     time.sleep(10)