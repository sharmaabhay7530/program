# 6. Inventory Management 
# Given a list of product stock quantities: 
# • Remove items with 0 stock 
# • Add restock (add 50 units) to items below 10 
# • Find total inventory count. 

stock = [0, 5, 12, 8, 0, 15, 2]

# Remove items with 0 stock
stock = [s for s in stock if s>0]

# Add restock of 50 to items < 10
stock = [s+50 if s<10 else s for s in stock]

# Total inventory
total_inventory = sum(stock)

print("Updated stock:", stock)
print("Total inventory count:", total_inventory)

# //output-------
# Updated stock: [55, 12, 58, 15, 52]
# Total inventory count: 192 ----------//