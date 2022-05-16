# link: https://codeforces.com/problemset/problem/155/A
number_of_contests = int(input())
max_points = -1
min_points = -1
amazing_performances = 0
points = [int(points) for points in input().split()]
for point in points:
    if max_points == -1 and min_points == -1:
        max_points = point
        min_points = point
    elif point > max_points:
        max_points = point
        amazing_performances += 1
    elif point < min_points:
        min_points = point
        amazing_performances += 1
print(amazing_performances)
