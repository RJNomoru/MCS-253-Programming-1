#LAB2-LAMBDA LOVE LETTER

#QUESTION 3
"""1. Ask user for input in kilogram."""
"""2. Use a lambda function, to convert kilograms to tonnes and print its output."""

#_____________________________________
#solution_code

#Q1. user input in km

userinput = float(input("Question:\nYou are asked to convert kilograms to tonnes.\nEnter value in kilogram:\n"))
# I used float function because the user can enter values as decimal numbers.

#Q2. Lambda Function
kg_to_tonnes = lambda x: x/1000
tonnes = kg_to_tonnes(userinput)
print(f"ANSWER:\n{userinput} kilograms is equal to {tonnes} tonnes.")