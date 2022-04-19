#!/usr/env/bin/ python3

'''
Script for solving fibonacci number sequence positional request.
Inputs include the position of sequence requested for value return (mandatory),
and the first two digits of the sequence (optional).
If first two digits are not provided defaults of n1=0 and n2=1 will be used (so n3=1, n4=2, etc.)
'''

import sys
#import argparse


###
### Import arguments
###

#Using argparse if desired
#argparser = argparse.ArgumentParser(
#        description="Program for solving fibonacci sequence with custom start values.")
#argparser.add_argument("-p", "--position", action="store", type=int,
#		help="Provide position of desired return value.")
#argparser.add_argument("-f", "--first", action="store", type=int,
#		help="Provide value of first digit in sequence.")
#argparser.add_argument("-s", "--second", action="store", type=int,
#		help="Provide value of second digit in sequence.")

#args = argparser.parse_args(sys.argv[1:])
#Verify how to make first and second values optional
#pos_out = args.position
#first_num = args.first
#second_num = args.second

#Using interactive inputs

#FIX: 
# Add qualification to ensure that second digit input is greater than first digit

alt_start = input("Would you like to change the default start values of n1=0 and n2=1? (y/n) ")
if alt_start.lower() == "y":
    first_num = input("Provide value of first digit in sequence: ")
    second_num = input("Provide value of second digit in sequence: ")
else:
    first_num = 0
    second_num = 1

pos_out = int(input("Position of sequence output: "))

###
### Calculate Answer
###

n0 = int(first_num)
n1 = int(second_num)
#Calculate out value using iterative addition
for i in range(3,pos_out+1):
    ni = n0 + n1
    n0 = n1
    n1 = ni

#FIX:
# If n0=0 and n1=1, then the golden ratio can be used to mathematically calculate the value at any out position without iteration
# Mathematically calculating the out value will be more efficient for large position numbers
#ratio = (1+5**(1/2))/2
#value_out = (ratio^(pos_out-1) - (1-ratio)^(pos_out-1)) / 5**(1/2)
# Python doesn't like using float numbers as the base for an exponent, so figure out how to fix, or don't use


###
### Return answer to user
###

print("Using starting digits of " + str(first_num) + " and " + str(second_num) + ", the output value of the Fibonacci sequence at position " + str(pos_out) + " is: " + str(ni))