#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill = float(input("How much is the bill?\n"))
people = int(input("How many people would you like to split the bill between?\n"))
tip = int(input("How much would you like to tip?(just type the number without the percentage i.e 12)\n"))
tip2 = (tip / 100) + 1 

id_bill = (bill / people) * tip2 
format_bill = "{:.2f}".format(id_bill)
print(format_bill)