import os
import csv
from collections import Counter
from collections import defaultdict

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

profit_list = []
profit_month = []

with open(csvpath) as csvfile:

    total_profitlosses_change = 0
    total_profitlosses= 0
    total_months = 0
    max_profit = 0
    min_profit = 0


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        date = row[0]
        profitlosses = int(row[1])

        profit_list.append(profitlosses)
        profit_month.append(date)
        total_profitlosses += profitlosses 
    

    
    profit_change = [y-x for x, y in zip(profit_list, profit_list[1:])]
    
    for i, x in enumerate(profit_change): #utilize this for getting min and max
        
        if x > max_profit:
            max_profit = x
            max_profit_month = i+1
        if x < min_profit:
            min_profit = x
            min_profit_month = i+1
        
        total_profitlosses_change += x
    

    # Average Change 

    average_change = round((total_profitlosses_change/85),2) 

    #Greatest Increase and Decrease months

    for i, x in enumerate(profit_month):
        if i == max_profit_month:
            final_max_profit = x, max_profit
        if i == min_profit_month:
            final_min_profit = x, min_profit



    # Final Output

    print('Financial Analysis')
    print('------------------------------------------')
    print('Total Months: ' + str(total_months))
    print('Total: $' + str(total_profitlosses))
    print('Average Change: $' + str(average_change))
    print('Greatest Increase in Profits: ' + str(final_max_profit))
    print('Greates Decrease in Profits: ' + str(final_min_profit))

    output_path = os.path.join('..', 'analysis', 'PyBank_Analysis.txt')
    with open(output_path, "w") as text_file:
        print('Financial Analysis', file=text_file,)
        print('------------------------------------------', file=text_file,)
        print('Total Months: ' + str(total_months), file=text_file,)
        print('Total: $' + str(total_profitlosses), file=text_file,)
        print('Average Change: $' + str(average_change), file=text_file,)
        print('Greatest Increase in Profits: ' + str(final_max_profit), file=text_file,)
        print('Greates Decrease in Profits: ' + str(final_min_profit), file=text_file,)

