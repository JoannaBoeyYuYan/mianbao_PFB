from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd() / 'csv_reports' / "cash_on_hand.csv"

coh = []

# read the csv file to append days and cash on hand from the csv
with fp.open(mode='r', encoding='UTF-8', newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        coh.append([row[0], row[1]])

# create a function to calculate difference to determine whether it is deficits or surplus
def coh_diff(coh):
    flag_list = []
    prev = int(coh[0][1])

    for days in range(1, len(coh)):
        cash = int(coh[days][1])
        diff = cash - prev
        prev = cash

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

coh_results = coh_diff(coh)

highest_cash_surplus = 0
highest_cash_day = ""
cash_deficit_amount = 0
cash_deficit_day = ""

for result in coh_results:
    if result[0] == "SURPLUS":
        if result[2] > highest_cash_surplus:
            highest_cash_surplus = result[2]
            highest_cash_day = result[1]
    elif result[0] == "DEFICITS":
        if result[2] > cash_deficit_amount:
            cash_deficit_amount = result[2]
            cash_deficit_day = result[1]

for result in coh_results:
    print(f"[CASH {result[0]}] DAY: {result[1]} , AMOUNT: USD {result[2]}")

