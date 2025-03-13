print('Welcome to tip calcultor')

bill = float(input('what was the total bills ? $' ))

tip_percentage = int(input("How much would you like to give? 10, 12, or 15"))

num_people = int(input("how many people need to split bills? "))

tip_amount = (tip_percentage/100 ) * bill

total_bill = bill - tip_amount

amount_paid =total_bill/num_people

print("each person should pay: " ,amount_paid)