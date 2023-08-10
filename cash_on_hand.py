from pathlib import Path
import csv

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

    aList = []

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
    prev = int(coh[0][1])  # prev figure = first figure in coh list

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
            
    return flag_list

# print to see the results
coh_results = coh_diff(coh)

# iterate the results so it will print for each day 
for result in coh_results:
    print(f"[CASH {result[0]}] DAY: {result[1]} , AMOUNT: USD {result[2]}")

# Compute the difference in cash column
previous_cash = 0
highest_surplus_day = None
highest_surplus_amount = 0
cash_deficit_day = None
cash_deficit_amount = 0
# Initialize a counter for the days with higher cash amount than the previous day
higher_cash_days = 0

for record in coh:
    day, cash = record

    # Convert cash amount to a numeric value
    cash = int(cash)

    # Compute the difference between current cash amount and previous cash amount
    cash_difference = cash - previous_cash
    previous_cash = cash

    # Check if the cash is higher, lower, or the same as the previous day
    if cash_difference > 0:
        comparison = "SURPLUS"
        # Increment the counter for higher cash days
        higher_cash_days += 1
    elif cash_difference < 0:
        comparison = "DEFICIT"
    else:
        comparison = "-"

    # print the day, Cash, and difference, along with whether there is higher or lower cash than the previous day
    print(f"Day: {day}, Cash: USD{cash}, Difference: USD {abs(cash_difference)}, "
          f"[CASH]: {comparison}")

    # Check if the current surplus is the highest so far
    if cash_difference > highest_surplus_amount:
        highest_surplus_day = day
        highest_surplus_amount = cash_difference

# Print the cash deficit information from the list
for result in coh_results:
    deficit_day, deficit_amount = result
    print(f"[CASH DEFICIT] DAY: {deficit_day}, AMOUNT: USD {abs(int(deficit_amount))}")

# print out the cash surplus, highest cash surplus [day and amount], and cash deficit [day and amount]
print("\n")
print(f"[CASH SURPLUS]: NET PROFIT ON {higher_cash_days} DAYS ARE HIGHER THAN PREVIOUS DAY")
print(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: USD{int(highest_surplus_amount)}")
print(f"[CASH DEFICIT] DAY: {cash_deficit_day}, AMOUNT: USD{abs(int(cash_deficit_amount))}")
