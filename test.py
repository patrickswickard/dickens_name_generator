import csv
import random

first_syllable_array = []
second_syllable_array = []

with open("name1.csv",'r') as name_file_1:
  reader1 = csv.reader(name_file_1)
  for row1 in reader1:
     entry = {}      
     entry['syllable'] = row1[0]
     entry['fit'] = row1[1]
     entry['funnydirty'] = row1[2]
     first_syllable_array.append(entry)
with open("name2.csv",'r') as name_file_2:
  reader2 = csv.reader(name_file_2)
  for row2 in reader2:
     entry = {}      
     entry['syllable'] = row2[0]
     entry['fit'] = row2[1]
     entry['funnydirty'] = row2[2]
     second_syllable_array.append(entry)
name_file_1.close()
name_file_2.close()


valid_name_array = []

for entry1 in first_syllable_array:
  syllable1 = entry1['syllable']
  fit1 = entry1['fit']
  funnydirty1 = entry1['funnydirty']
  for entry2 in second_syllable_array:
    syllable2 = entry2['syllable']
    fit2 = entry2['fit']
    funnydirty2 = entry2['funnydirty']
    if float(fit1) + float(fit2) >= 1.25 and float(funnydirty1) + float(funnydirty2) >= 1.25:
      goofy_name = syllable1 + syllable2
      valid_name_array.append(goofy_name)

random.shuffle(valid_name_array)

print(len(valid_name_array))
#print(valid_name_array)
