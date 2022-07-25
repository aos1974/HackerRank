# Nested Lists
# Task: Students and scores
#
# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

# Main programm module
if __name__ == '__main__':
    
    students_list = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])
        
    scores = set(map(lambda sc: sc[1], students_list))
    scores = list(scores)
    scores.sort()
    
    names = [sc[0] for sc in students_list if sc[1] == scores[1]]
    names.sort()
    
    for n in names:
        print(n)
    