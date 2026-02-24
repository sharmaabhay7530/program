# 9. Movie Rating System 
# Given list of ratings (1–5): 
# • Remove invalid ratings 
# • Find average rating 
# • Count how many 5-star ratings 
# • Sort ratings in ascending order. 


ratings = [5, 4, 3, 6, 2, 5, 0, 5]

# Remove invalid ratings
ratings = [r for r in ratings if 1<=r<=5]

# Average rating
avg_rating = sum(ratings)/len(ratings)

# Count 5-star ratings
five_star = ratings.count(5)

# Sort ascending
ratings.sort()

print("Valid ratings:", ratings)
print("Average rating:", avg_rating)
print("Number of 5-star ratings:", five_star)


# //output----------------
# Valid ratings: [2, 3, 4, 5, 5, 5]
# Average rating: 4.0
# Number of 5-star ratings: 3 -----------------//