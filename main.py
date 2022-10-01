import csv
import random

#import class list of names from a csv file
#user selection of number of names and run in loop
swoop = int(input("Which list do you want to use 1 for full 2 for short "))

if swoop == 1:
  with open('clss.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)
else:
  with open('clss2.csv', newline='') as f:
      reader = csv.reader(f)
      stc = list(reader)
  
chosen = int(input("How many names do you want to choose: "))
#chosen = 1
while chosen != 0 :
  #print(data)
  sampled_stc = random.sample(stc, chosen)
  print(sampled_stc)
  #print(random.choice(stc))
  chosen = int(input("How many names do you want to choose: "))
  if chosen == 0:
    print("Thanks bye!")