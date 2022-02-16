# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:25:08 2022

@author: Tejaswi
"""

import sys
import subprocess
import json

#subprocess.check_call([sys.executable, '-m', 'pip', 'install','<packagename>'])


with open ('bmi.json','r') as openfile:
    data = json.load(openfile)
    
def category_risk(row):
    if row['BMI'] <=18.4 :
        return 'Underweight', 'Malnutrition Risk'
    elif row['BMI'] <=24.9:
        return 'Normal Weight', 'Low Risk'
    elif row['BMI'] <=29.9:
        return 'Over weight', 'Enhanced Risk'
    elif row['BMI'] <=34.9:
        return 'Moderately Obese', 'Medium Risk'
    elif row['BMI'] <=39.9:
        return 'Severely Obese', 'Hight Risk'
    elif row['BMI'] >= 40 :
        return 'Very Severaly Obese', 'Very High Risk'
    
i = 0  
count_of_overweight_people = 0  
for i in range(len(data)):
    data[i]['BMI'] = round((data[i]['WeightKg']*10000/data[i]['HeightCm']**2),2)
    data[i]['BMI Category'] = category_risk(data[i])[0]
    data[i]['Health Risk'] = category_risk(data[i])[1]
    if data[i]['BMI']>=30:
        count_of_overweight_people+=1   
    i+=1

print(data)
print("No. of overweight people is:",count_of_overweight_people)
json_file = json.dumps(data)
with open('output.json','w') as output_file:
            output_file.write(json_file)
            

            





