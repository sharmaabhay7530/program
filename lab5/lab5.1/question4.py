# 4. Salary Processing System 
# Given list of employee salaries: 
# • Remove salaries below minimum wage 
# • Add 5% bonus to employees with salary > 50,000 
# • Sort salaries in descending order 
# • Display top 3 highest salaries. 

salaries = [40000, 55000, 60000, 30000, 70000, 45000]

# Remove salaries below minimum wage (assume 35000)
salaries = [s for s in salaries if s >= 35000]

# Add 5% bonus to salary > 50000
salaries = [int(s*1.05) if s>50000 else s for s in salaries]

# Sort descending
salaries.sort(reverse=True)

# Top 3 salaries
top3 = salaries[:3]

print("Processed salaries:", salaries)
print("Top 3 salaries:", top3)


# //output----------
# Processed salaries: [73500, 63000, 57750, 45000, 40000]
# Top 3 salaries: [73500, 63000, 57750] ---------------//