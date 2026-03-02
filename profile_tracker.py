
student_name = input("Enter the student's name: ")
grade_input = input("Enter the student's current grade (e.g., 10): ") 
current_grade = int(grade_input) 

header_boarder = "-"  * 20 

print(header_boarder)
print("Student: " + student_name + "  | Grade: " + str(current_grade))
print(header_boarder)


hobbies = [] 

first_hobby = input("Enter a hobby: ") 
hobbies.append(first_hobby) 

second_hobby = input("Enter another hobby: ") 
hobbies.append(second_hobby) 

hobbies.insert(0, "coding") 
hobbies.remove(first_hobby) 

print("Updated Hobbies:" , hobbies)

hobbies[1] = "Advanced Python" 
top_two = hobbies[0:2]
hobbies_count = len(hobbies) 
print("\nFinal Student Profile Stats:")
print("Total Hobbies: {0}".format(hobbies_count)) 
print("Top Picks: {0}".format(top_two))
