# Author: Faith Elledge
# Githubuser:elledgef
# Date: 11/4/22
# Description: This code takes a list of numbers and returns the maximum value of the list

def list_max(num_list):
    """ This function takes a list of numbers as a parameter and outputs the maximum value in the list """
    if len(num_list) <= 1:
            return num_list[0]
    else:
        return_value = list_max(num_list[1:])
        return return_value\
            if return_value >= num_list[0]\
                else num_list [0]



















