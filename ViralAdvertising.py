# no. of days ad is continued
ad_days = 3

day = 1
shares = 5
likes = shares // 2
total_likes = likes

day = 2

while day <= ad_days:

    shares = likes * 3

    likes = shares // 2

    total_likes += likes

    day += 1

print(total_likes)