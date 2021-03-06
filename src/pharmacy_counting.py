#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:58:57 2018

@author: daywalker
"""
import sys

# parameters  from the shell script

parameter1 = sys.argv[1]
parameter2 = sys.argv[2]

# dictionary for drugs
dictlist = {}


def drugs_name(sep_data):

    # check if the size of the elements are five or not
    global drug_name_

    if(len(sep_data) > 5):

        try:
            """ 

            If the size of comma seperated data more than five
            then check the last but one element in the seperated 
            data. If the element is a number then append it 
            with the element from the thrid last for drug name
            
            Example : Panc 5,00 this would be split into
            Panc 5 and 00 . So we append them both together

            """

            if(isinstance(float(sep_data[-2]), float)):
                drug_name_ = sep_data[-3] + ',' + sep_data[-2]

        except ValueError as e:
            """ 
            
            For Drugs name followed by value eg: "Panc 5,000". 
            For these split them with " and append the value to name 
            
            """
            sep_value = sep_data[-2].split("\"")
            if(len(sep_value) > 1):
                d_n = sep_data[-3].split("\"")
                drug_name_ = d_n[1] + ',' + sep_value[0]
            else :
                drug_name_ = sep_data[-2]  # drug name
            
            pass
                

    # elements size is 5 or less
    else:
        drug_name_ = sep_data[-2]  # drug name

    return drug_name_


def drug_insertion(dictlist, elements, drug_name):

    # check the drug name already present in the dictionary

    if (drug_name in dictlist):
        values = dictlist[drug_name]  # values of the drug
        values[0].add(elements[0])  # id of the patients for that drug
        init_cost = values[1]  # cost of the drug
        try:
            # increment the drug cost
            updated_cost = init_cost + float(elements[-1])
            dictlist[drug_name] = [values[0],
                                   updated_cost]  # updating drug data

        except ValueError as e:
            print("error on line", elements)
            pass

    # if the drug is not present in the dictionary
    else:
        id_set = set()  # creating set for the id's of patient
        cost = float(elements[-1])  # cost of the drug
        id_set.add(elements[0])  # adding id's to the set
        dictlist[drug_name] = [id_set, cost]  # updating


with open(parameter1, 'r') as data:
    next(data)  # skipping the header
    for line in data:
        elements = line.rstrip().split(",")  # splitting the line by ,
        dname = drugs_name(elements)  # getting drug name
        drug_insertion(dictlist, elements, dname)  # creating drug,cost data

# sorting the data by cost
sorted_data = sorted(dictlist.items(), key=lambda e: e[1][1], reverse=True)

out_file = open(parameter2, 'w')  # outputfile
out_file.write("drug_name,num_prescriber,total_cost\n")  # header

# adding data the output file
for item in sorted_data:
    line = (item[0]+','+str(len(item[1][0]))+',' + str(int(item[1][1])) + '\n')
    out_file.write(line)
out_file.close()