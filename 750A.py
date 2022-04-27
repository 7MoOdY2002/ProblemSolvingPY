number_of_problems,minutes_to_get_there = map(int, input().split())
total_time = 240
total_time -= minutes_to_get_there
problems_solved = 0
time_left = 0
for i in range(1,number_of_problems+1):
   # print("i= ",i)
    time_left += 5 * i
    if(time_left <= total_time):
       # print("time left = ",time_left)
        problems_solved+=1
    else:
        break
print(problems_solved)