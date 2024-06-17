import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from src.utils import payoff_table

number_of_options=int(input("Enter the number of options in your combination stratergy: "))

option_parameter_table=payoff_table.option_info_df(number_of_options)   #Collects all the parameters about the options of the stratergy

k = sp.symbols('k')    # Define the symbolic variable

payoff_headers_df=payoff_table.payoff_table_headers(option_parameter_table)  

sp_temp=payoff_table.psuedo_header_list(option_parameter_table)

payoff_table_fnl=payoff_table.table_entries(option_parameter_table,sp_temp,payoff_headers_df,number_of_options)

print(payoff_table_fnl)

breakeven_values =payoff_table.breakeven_points(payoff_table_fnl,sp_temp,number_of_options)
print(f'breakeven points are:{breakeven_values}')

profit=payoff_table.fnl_profit(option_parameter_table,payoff_table_fnl,sp_temp,number_of_options)
print(f'profit is:{profit}')

payoff_table.plot_graph(option_parameter_table)
