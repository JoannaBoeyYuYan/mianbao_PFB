from pathlib import Path
import csv
j

# create a file to csv file.
fp = Path.cwd()/'csv_reports'/"cash_on_hand.csv"
#print(fp.exists()) - To check if file exsists

# create an empty lists to store days and cash on hand
coh = []

# read the csv file to append days and cash on hand from the csv
with fp.open(mode='r', encoding ='UTF-8', newline = "") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    # append days and cash on hand into the cash_on_hand list 
    for row in reader:
        coh.append([row[0], row[1]])

# print to see the results
# print(coh)

# create a function to calculate difference to determine whether it is deficits or surplus
def coh_diff(coh):
    '''
    - calculate difference to determine whether it is deficits or surplus
    - parameters required : days, cash on hand 
    '''
    # create an empty list
    flag_list = []
    prev = int(coh[0][1]) # prev figure = first figure in coh list

    # iterate and get next figure from coh list
    for days in range(1, len(coh)):
            cash = int(coh[days][1])
            diff = cash - prev 
            prev = cash  # for next iteration 

            # check if the diff is deficit or surplus
            if diff < 0:
                flag = 'DEFICITS'
            elif diff > 0:
                flag = 'SURPLUS'
            else:
                flag = 'NO SURPLUS/DEFICITS'
            
            if diff < 0:
                diff = diff * (-1)
            
            if flag == 'DEFICITS':
                flag_list.append([flag, coh[days][0], diff])
            
            # append the decifits flag, days and difference into flag_list    
            

    return flag_list
   

# print to see the results
coh_results = coh_diff(coh)

# iterate the results so it will print for each day 
for result in coh_results:
    print(f"[CASH {result[0]}] DAY: {result[1]} , AMOUNT: USD {result[2]}")


# print('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
# print('[CASH DEFICITS] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY')