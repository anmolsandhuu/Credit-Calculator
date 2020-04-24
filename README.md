# Credit-Calculator
A simple credit calculator, takes in input from user via command line

Objectives

the calculation of differentiated payment and annuity payments. To do this, the user may run the program specifying interest, count of periods and credit principal.

A capacity to calculate the same values as in the previous stage for annuity payment (principal, count of periods and value of the payment). 
A user specifies all known parameters with command-line arguments, while a single parameter will be unknown. 
This is the value the user wants to calculate.

To use:
usage: credit_calculator.py [-h] [-t TYPE] [-c PRINCIPAL] [-p PAYMENT]
                            [-P PERIODS] [-i INTEREST]

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  --type=[diff] | [annuity]
  -c PRINCIPAL, --principal PRINCIPAL
                        Total credit principal
  -p PAYMENT, --payment PAYMENT
                        Total payment
  -P PERIODS, --periods PERIODS
                        Period in months
  -i INTEREST, --interest INTEREST
                        Interest
