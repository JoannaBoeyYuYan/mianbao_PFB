# team members text file
from pathlib import Path
import csv

# create a path object for team_members.txt
fp = Path.cwd()/"team_members.txt"
# create new file in folder
fp.touch()
# check file path of this new file
print(fp)
# check if file path exists
print(fp.exists())

# create a list to put names and student ID
members_list = ['Bradley Matthias Ganesh (S10255891H)', 
                'Joanna Boey Yu Yan (S10258045H)',
                'Yee Jia Ying (S10261025F)',
                'Evangelyn Siau Yi Xuen (S10257334K)',
                'Lim Jing En (S10255896C)']

# writing results to text file
with fp.open(mode='w', encoding ='UTF-8', newline = "") as file:
    # Create a writer object: 'writer' with 'csv.writer()'
    writer = csv.writer(file)
    # write header
    writer.writerow(['Name (Student ID)'])
    # write data
    for member in members_list:
        writer.writerow([member])

# print the results to read here
# with fp.open(mode='r', encoding ='UTF-8', newline = "") as file:
#     reader = csv.reader(file)
#     next(reader) # skip header
#     for line in reader:
#         print(line)