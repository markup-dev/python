grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
students.sort()

result = dict()

result[students[0]] = sum(grades[0]) / len(grades[0])
result[students[1]] = sum(grades[1]) / len(grades[1])
result[students[2]] = sum(grades[2]) / len(grades[2])
result[students[3]] = sum(grades[3]) / len(grades[3])
result[students[4]] = sum(grades[4]) / len(grades[4])

print(result)

# ----------------

# for i in range(len(students)):
# 	result[students[i]] = sum(grades[i]) / len(grades[i])
#
# print(result)
