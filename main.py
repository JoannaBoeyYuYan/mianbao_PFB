from pathlib import Path
import csv 
import overheads 
import cash_on_hand 
# import profit_and_loss 

def main(): 
    highest_category, max_overhead  = overheads.overheads_function() 
    cash_on_hand_output = cash_on_hand.cash_on_hand_function() 
    # profit_and_loss.profit_and_Loss_function()
    
    # if cash_on_hand_output:
    #     for flag, day, amount in cash_on_hand_output:
    #         file.write(f"[CASH {flag}] DAY: {day} , AMOUNT: USD {amount}")
     # Create a path object for summary_report.txt
    fp = Path.cwd() / "summary_report.txt" 
    fp.touch()   
    # Open the file for writing    
    with fp.open(mode='w', encoding='UTF-8', newline="") as file:
        if cash_on_hand_output:            
            for flag, day, amount in cash_on_hand_output:
                file.write(f"[CASH {flag}] DAY: {day}, AMOUNT: USD {amount}\n")

main()
# cash_on_hand_output = main()
# # create a path object for summary_report.txt
# fp = Path.cwd()/"summary_report.txt"
# # create new file in folder
# fp.touch()
# # check file path of this new file
# print(fp)
# # check if file path exists
# print(fp.exists())

# with fp.open(mode='w', encoding ='UTF-8', newline = "") as file:
# # Create a writer object: 'writer' with 'csv.writer()'
#     file.write('hello')
#     file.write()






# ------------------------------------------------------------------------------------------