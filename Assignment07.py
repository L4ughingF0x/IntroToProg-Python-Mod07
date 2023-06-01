# ------------------------------------------------- #
# Title: Assignment 07
# Description: Storing data with the pickle module with some error exception handling on the side
# ChangeLog: (Who, When, What)
# SLockwood,31.5.2023,Created Script
# ------------------------------------------------- #
import pickle  # Importing the pickle module for use here

data = input('Enter some data to be pickled: ')  # Asking user for data to throw into pickle

try:
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)
    print('Data saved successfully.')
except Exception as e:
    print(f'An error occurred while saving data: {e}')
# Pickling the provided data to a .pkl file by opening the file and using the pickle.dump() function

try:
    with open('data.pkl', 'rb') as f:
        loaded_data = pickle.load(f)
    print(f'Loaded data: {loaded_data}')
except Exception as e:
    print(f'An error occurred while loading data: {e}')
# Retrieving data in readable format by loading it with pickle using the pickle.load function
