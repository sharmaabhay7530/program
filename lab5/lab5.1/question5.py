# 5. Online Exam Result Processor 
# Given a list of student scores: 
# • Remove lowest 2 scores 
# • Add grace marks of 5 to those scoring between 30–35 
# • Count number of students passed (≥ 40). 


scores = [25, 32, 34, 40, 38, 50, 29]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add 5 grace marks to scores between 30–35
scores = [s+5 if 30<=s<=35 else s for s in scores]

# Count students passed (>=40)
passed = sum(1 for s in scores if s>=40)

print("Processed scores:", scores)
print("Number of students passed:", passed)



# //output--------
# Processed scores: [37, 39, 38, 40, 50]
# Number of students passed: 2  -------//