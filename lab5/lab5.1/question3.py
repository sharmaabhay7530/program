# 3. Attendance Tracker 
# Given a list of student attendance (1 for present, 0 for absent): 
# • Calculate attendance percentage 
# • Identify students below 75% 
# • Replace consecutive absences with a warning flag. 


attendance = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1]

# Attendance percentage
percentage = attendance.count(1)/len(attendance)*100

# Identify students below 75%
if percentage < 75:
    status = "Below 75% attendance"
else:
    status = "Satisfactory"

# Replace consecutive absences with warning
warned = attendance[:]
for i in range(len(attendance)-2):
    if attendance[i]==0 and attendance[i+1]==0:
        warned[i] = warned[i+1] = "Warn"

print("Attendance %:", percentage)
print("Status:", status)
print("Attendance with warnings:", warned)


# //output--------
# Attendance %: 50.0
# Status: Below 75% attendance
# Attendance with warnings: [1, 1, 'Warn', 'Warn', 1, 1, 'Warn', 'Warn', 'Warn', 1] ----------------//