# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:31:33 2020

@author: admin
"""


def calculate(distance_in_km, g):
    co2e=(distance_in_km*g)/1000
    print ("\nYour trip caused ",co2e,"kg of CO2-equivalent.")

print("                            CO2 EMISSION CALCULATOR")
print("********************************************************************************")
print("\nSmall Cars:")
print("|small-diesel-car          | 142g |\n|small-petrol-car          | 154g |\n|small-plugin-hybrid-car   | 73g  |\n|small-electric-car        | 50g  |")
print("\nMedium Cars:")
print("|medium-diesel-car         | 171g |\n|medium-petrol-car         | 192g |\n|medium-plugin-hybrid-car  | 110g |\n|medium-electric-car       | 58g  |")
print("\nLarge Cars:")
print("|large-diesel-car          | 209g |\n|large-petrol-car          | 282g |\n|large-plugin-hybrid-car   | 126g |\n|large-electric-car        | 73g  |")
print("\nBus: 27g")
print("\nTrain: 6g")
distance_in_km=float(input("\nEnter the distance want to be travelled in kms: "))
s=input("Enter the transportation mode you want to travel: ")
if s =="small-diesel-car":
    calculate(distance_in_km,142)
elif s=="small-petrol-car":
    calculate(distance_in_km,154)
elif s =="small-plugin-hybrid-car":
    calculate(distance_in_km,73)
elif s =="small-electric-car":
    calculate(distance_in_km,50)
elif s =="medium-diesel-car":
    calculate(distance_in_km,171)
elif s =="medium-petrol-car":
    calculate(distance_in_km,192)
elif s =="medium-plugin-hybrid-car":
    calculate(distance_in_km,110)
elif s =="medium-electric-car":
    calculate(distance_in_km,58)
elif s =="large-diesel-car":
    calculate(distance_in_km,209)
elif s =="large-petrol-car":
    calculate(distance_in_km,282)
elif s =="large-plugin-hybrid-car":
    calculate(distance_in_km,126)
elif s =="large-electric-car":
    calculate(distance_in_km,73)
elif s =="bus":
    calculate(distance_in_km,27)
elif s =="train":
    calculate(distance_in_km,6)
else :
    print("\n It was invalid transportation mode")
