# 10. Sports Tournament Points Table 
# Given list of team points: 
# • Find winner and runner-up 
# • Replace negative points with 0 
# • Sort leaderboard. 


points = [20, -5, 15, 30, 25]

# Replace negative points with 0
points = [p if p>=0 else 0 for p in points]

# Sort leaderboard descending
points.sort(reverse=True)

# Winner and runner-up
winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner:", winner)
print("Runner-up:", runner_up)

# //output------------
# Leaderboard: [30, 25, 20, 15, 0]
# Winner: 30
# Runner-up: 25 --------//


#