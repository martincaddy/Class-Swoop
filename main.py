import csv
import random

#import class list of names from a csv file

with open('clss.csv', newline='') as f:
    reader = csv.reader(f)
    stc = list(reader)

#user selection of number of names and run in loop

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