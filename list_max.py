# Author: Faith Elledge
# Githubuser:elledgef
# Date: 11/4/22
# Description: This code takes a list of numbers and returns the maximum value of the list

def list_max(num_list):
    """ This function takes a list of numbers as a parameter and outputs the maximum value in the list """
    if len(num_list) == 1:
        return num_list[0]
    else:
        return_result = list_max(num_list[1:])
        return return_result
        if return_result <= num_list[0]:
           return_result = num_list[0]







