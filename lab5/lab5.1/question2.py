# 2. E-Commerce Cart System 
# Given a list of product prices in a cart: 
# • Remove duplicate items 
# • Apply 10% discount if total > ₹5000 
# • Add GST 18% 
# • Display final payable amount. 

cart = [1000, 2000, 1500, 1000, 500]

# Remove duplicates
cart = list(set(cart))

# Total amount
total = sum(cart)

# Apply 10% discount if total > 5000
if total > 5000:
    total *= 0.9

# Add GST 18%
total *= 1.18

print("Final payable amount: ₹", round(total,2))

# //output-----
# Final payable amount: ₹ 5900.0 ---------//