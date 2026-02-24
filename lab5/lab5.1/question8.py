# 8. Temperature Monitoring System 
# Given daily temperatures of a month: 
# • Find hottest and coldest day 
# • Replace temperatures above 45°C with “Heat Alert” 
# • Count number of extreme days (> 40°C). 

temps = [35, 42, 47, 38, 46, 41, 30]

# Hottest and coldest day
hottest = max(temps)
coldest = min(temps)

# Replace temps above 45°C with 'Heat Alert'
temps_alert = ["Heat Alert" if t>45 else t for t in temps]

# Count extreme days >40°C
extreme_days = sum(1 for t in temps if t>40)

print("Hottest:", hottest, "Coldest:", coldest)
print("Temperatures with alerts:", temps_alert)
print("Number of extreme days:", extreme_days)


# //output--------------
# Hottest: 47 Coldest: 30
# Temperatures with alerts: [35, 42, 'Heat Alert', 38, 'Heat Alert', 41, 30]
# Number of extreme days: 4 ---------------//