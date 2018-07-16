#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:58:57 2018

@author: daywalker
"""
import sys
var1 = sys.argv[1]
var2 = sys.argv[2]
print(var1)


dictlist = {}
with open( var1, 'r') as data:
        next(data) 
        for line in data:
            elements = line.rstrip().split(",")
            
            
            if(len(elements)>5):
            
                try:
                    if(isinstance(float(elements[-2]), float)):
                        drug_name = elements[-3] + ',' + elements[-2]
                except ValueError as e:
                    sep_value=elements[-2].split("\"")
                    #print(sep_value)           
                    if(len(sep_value)>1):
                        d_n=elements[-3].split("\"")
                        
                        drug_name = d_n[1] + ',' + sep_value[0]
                        #print(drug_name)       
                        
                    
                    
                    
            else:
                drug_name = elements[-2]
                
                
            if (drug_name in dictlist):
                values = dictlist[drug_name]
                values[0].add(elements[0])  #id of the line
                init_cost = values[1]
                try:
                    updated_cost = init_cost + float(elements[-1])
                    dictlist[drug_name] = [values[0],updated_cost]  
              
                except ValueError as e:
                    print ("error on line",elements[4])
          
            else:
                id_set = set()
                cost = float(elements[-1])
                id_set.add(elements[0])
                dictlist[drug_name] = [id_set,cost]
                

sorted_data = sorted(dictlist.items(), key=lambda e: e[1][1], reverse=True)

f = open( var2, 'w')
f.write ("drug_name,num_prescriber,total_cost\n")

for item in sorted_data:
    line=( item[0]+','+str(len(item[1][0]))+','+ str(item[1][1]) +'\n')
    
    f.write(line)
f.close()
    
                