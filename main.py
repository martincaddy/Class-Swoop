import csv
import random
import time
import os

#import class list of names from a csv file
#user selection of number of names and run in loop swoop is the variable for class list choice
swoop = int(input("Which list do you want to use \n1 Full Class \n2 Year 4 \n3 Year 5 \n4 Define your own list \n5 Target \n \n"))

#user defined time delay
delay = int(input("How many seconds do you want to wait for each name picked? "))

if swoop == 1:
  with open('clss.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)
    
elif swoop == 2:
  with open('Year4.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)
elif swoop == 3:
  with open('Year5.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)

elif swoop == 4:
# creating an empty list
  stc = [] 
# number of elements as input
  n = int(input("How many names do you want to add? : ")) 
# iterating till the range
  for i in range(0, n):
      ele = str(input('Name: ')) 
      stc.append(ele) # adding the element
      
#print(lst)    
else:
  with open('clss2.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)
  
chosen = int(input("How many names do you want to choose: "))

#main loop (stc it the name of the list used)
while chosen != 0 :
  sampled_stc = random.sample(stc, chosen)
  print(sampled_stc)
  time.sleep(delay)
  os.system('clear')
  chosen = int(input("How many names do you want to choose: "))
if chosen == 0:
  print("Thanks bye!")

  