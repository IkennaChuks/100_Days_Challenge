# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

Sum = 0
count = 0
for num in student_heights:
  Sum += num
  count += 1
Average = (Sum/count)
print(f'Average is equal to {Average}')



