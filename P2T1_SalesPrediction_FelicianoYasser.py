# Yasser Feliciano
#P2T1_SalesPrediction_FelicianoYasser
# This program will provide sales prediction

# Pseudocode
# 1.) Declare variables
# total_sales = 0 float
# profit = 0 float
# annual_profit = .23 float
# 2.) Promt the user for total sales
# 3.) Calculate the profit using the following
#  profit = total_sales * annual profit 
# 4.) Display projected profit

#Variables
total_sales = 0.0 
profit = 0.0
annual_profit = 0.23

#prompt user for total sales
total_sales = float(input (" Enter the projected total sales: "))

# calculations
profit = total_sales * annual_profit

#display profit
print("The projected profit is $", format (profit, ' ,.2f'))
