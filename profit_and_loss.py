from pathlib import Path
import csv

# Set the file path to "Profit_And_Loss.csv"
file_path = Path.cwd()/'csv_reports'/"Profit_And_Loss.csv"

# Convert the file path to a Path object
fp = Path(file_path)

# Read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # Skip header
    next(reader) 

    # Create an empty list to store profit and loss
    Profit_And_Loss = [] 

    # Append Profit_And_Loss record into the Profit_And_Loss list
    for row in reader:
        # Get the Day, Sales, Trading Profit, Operating Expense, and Net Profit for each record
        # and append the Profit_And_Loss list
        Profit_And_Loss.append([row[0], row[1], row[2], row[3], row[4]])   
    
    aList = []

# Compute the difference in net profit column
previous_net_profit = 0
highest_surplus_day = None
highest_surplus_amount = 0
profit_deficit_day = None
profit_deficit_amount = 0
# Initialize a counter for the days with higher net profit than the previous day
higher_net_profit_days = 0
for record in Profit_And_Loss:
    day, sales, trading_profit, operating_expense, net_profit = record

    # Convert net profit to a numeric value (remove commas and convert to float)
    net_profit = float(net_profit.replace(",", ""))

    # Compute the difference between current net profit and previous net profit
    profit_difference = net_profit - previous_net_profit
    previous_net_profit = net_profit

    # Check if the net profit is higher, lower, or the same as the previous day
    if profit_difference > 0:
        comparison = "HIGHER"
        # Increment the counter for higher net profit days
        higher_net_profit_days += 1  
    #Check if net profit is negative(indicating a deficit)
    elif profit_difference < 0:
        comparison = "LOWER"
        # Append the deficit day and amount to the list
        aList.append([day, profit_difference])
    else:
        comparison = "-"

    # Check if the current surplus is the highest so far
    if profit_difference > highest_surplus_amount:
        highest_surplus_day = day
        highest_surplus_amount = profit_difference
    # Check if the current deficit is the lowest so far
    if profit_difference < profit_deficit_amount:
        profit_deficit_day = day
        profit_deficit_amount = profit_difference

# Print the profit deficit information from the list
for result in aList:
    deficit_day, deficit_amount = result
    print(f"[PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{abs(int(deficit_amount))}")




# print out the net profit surplus, highest net profit surplus [day and amount], and profit deficit [day and amount]
#print("\n")
#print(f"[NET PROFIT SURPLUS]: NET PROFIT ON {higher_net_profit_days} DAYS ARE HIGHER THAN PREVIOUS DAY")
#print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_surplus_day}, AMOUNT: USD{int(highest_surplus_amount)}")
#print(f"[PROFIT DEFICIT] DAY: {profit_deficit_day}, AMOUNT: USD{abs(int(profit_deficit_amount))}")