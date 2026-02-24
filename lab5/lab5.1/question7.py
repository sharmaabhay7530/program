# 7. Bank Transaction Analyzer 
# Given a list of transactions (positive = deposit, negative = withdrawal): 
# • Calculate total balance 
# • Find largest withdrawal 
# • Count number of deposits greater than ₹10,000. 


transactions = [20000, -5000, 15000, -20000, 8000]

# Total balance
balance = sum(transactions)

# Largest withdrawal
withdrawals = [t for t in transactions if t<0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

# Count deposits > 10000
large_deposits = sum(1 for t in transactions if t>10000)

print("Total balance:", balance)
print("Largest withdrawal:", largest_withdrawal)
print("Number of deposits > ₹10000:", large_deposits)

# //output ------------
# Total balance: 18000
# Largest withdrawal: -20000
# Number of deposits > ₹10000: 2 ----------//