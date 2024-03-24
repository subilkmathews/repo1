#Input student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height is : {total_height}")
total_players = 0
for player in student_heights:
    total_players += 1
print(f"Total number of players is : {total_players}")

average_height = round(total_height/total_players)
print(f"average height is: {average_height}")