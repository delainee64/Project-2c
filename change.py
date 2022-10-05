# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/04/2022
# Description: Write a program that asks the user for a (integer) number of cents, from 0 to 99
# using the fewest number of coins.

print("Please enter an amount in cents less than a dollar.")
cents = int(input())
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

result_q = cents // QUARTER
result_d = (cents % QUARTER) // DIME
result_n = result_d // NICKEL
result_p = (cents % NICKEL) // PENNY

print("Your change will be:")
print("Q:", result_q)
print("D:", result_d)
print("N:", result_n)
print("P:", result_p)
