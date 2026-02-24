#shopping bill claculation
notebook = 3
notebook_price = 45
pens = 2
pen_price = 20
total_bill = (notebook * notebook_price)+(pens*pen_price)
print(f"total bill amount : {total_bill}")
cash_given = 500
balance = cash_given -total_bill
print(f"remaing balance :{balance}")

# salary calculation
basic_salary =  250000
bonus = 5000
HRA= (basic_salary * 20)/100
print(f"HRA: {HRA}")
total_salary = basic_salary + HRA + bonus
print(f"total Motnthly salary : {total_salary}")






# Classroom student distribution
total_student = 125
class_capacity = 30
full_classes = total_student // class_capacity
print(f"full classes: {full_classes}")
remining_student = total_student % class_capacity
print(f"Remaing student: {remining_student}")