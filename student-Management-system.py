students = []

while True:
    
    print("=====Student Management System=====")
    print("1. Add students")
    print("2. View all students")
    print("3. search students")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice(1-4): "))
    
    except ValueError:
        print("Invalid input! Please enter a number")
        continue
        
    if choice == 4:
        print("Program ended. Goodbye!")
        break
    
    elif choice < 1 or choice > 4:
        print("Invalid choice")
        continue

    elif choice == 1:
        students_name = input("Enter student name: ")
        
        try:
            python_marks = int(input("Enter python marks: "))
            maths_marks = int(input("Enter math marks: "))
            english_marks = int(input("Enter English marks: "))
            
        except ValueError:
            print("Invalid input! Please enter a numeric marks.")
            continue
            
        if (python_marks < 0 or python_marks > 100 or
            maths_marks < 0 or maths_marks > 100 or
            english_marks < 0 or english_marks > 100):
               
            print("Marks must be between 0 to 100")
            continue

        total_marks = python_marks + maths_marks + english_marks
        print("Total Marks: ",total_marks)
        
        percentage = (total_marks * 100) / 300
        print("Percentage: ",percentage)
        
        if percentage >= 80:
            Grade = "A"
            print("Grade: ",Grade)
            
        elif percentage >= 70:
            Grade = "B"
            print("Grade: ",Grade)
            
        elif percentage >= 60:
            Grade = "C"
            print("Grade: ",Grade)

        elif percentage >= 50:
            Grade = "D"
            print("Grade: ",Grade)
            
        else:
            Grade = "Fail"
            print("Grade: ",Grade)

        student = {
            "name" : students_name , 
            "python" : python_marks , 
            "math" : maths_marks , 
            "english" : english_marks ,
            "total" : total_marks , 
            "Percentage" : percentage , 
            "grade" : Grade
        }
 
        students.append(student) 
        print("student added successfully")
        
    elif choice == 2:
        if len(students) == 0:
            print("No student record found")
        
        else:
            for student in students:
                print("Name: " ,student["name"])
                print("Python marks: " , student["python"])
                print("Math marks: " ,student["math"])
                print("English marks: ",student["english"])
                print("Total Marks: " ,student["total"])
                print("Percentage: " ,student["Percentage"])
                print("Grade: " ,student["grade"])
            
    elif choice == 3:
        search_name = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"] == search_name:
                print("Name:", student["name"])
                print("Python marks:", student["python"])
                print("Math marks:", student["math"])
                print("English marks:", student["english"])
                print("Total Marks:", student["total"])
                print("Percentage:", student["Percentage"])
                print("Grade:", student["grade"])

                found = True

        if found == False:
            print("Student not found!")
               