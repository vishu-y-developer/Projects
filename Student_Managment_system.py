"""
=== Student Management System ===
1. Student Add karo
2. Sab Students dekho
3. Student Dhundho
4. Student Delete karo
5. Average Marks
6. Exit

Choice: 1
Name: Ali
Roll no: 1
Marks: 85
Ali add ho gaya! ✅

Choice: 1
Name: Raj
Roll no: 2
Marks: 90
Raj add ho gaya! ✅

Choice: 1
Name: Priya
Roll no: 3
Marks: 78
Priya add ho gaya! ✅

Choice: 2
--- Sab Students ---
Roll: 1 | Name: Ali   | Marks: 85.0
Roll: 2 | Name: Raj   | Marks: 90.0
Roll: 3 | Name: Priya | Marks: 78.0

Choice: 3
Naam likho: ali
Mila! Roll: 1 | Marks: 85.0

Choice: 5
Average marks: 84.33

Choice: 4
Roll no likho: 2
Delete ho gaya! ✅

Choice: 2
--- Sab Students ---
Roll: 1 | Name: Ali   | Marks: 85.0
Roll: 3 | Name: Priya | Marks: 78.0

Choice: 6
Bye! 👋
"""


students_data = {}
while True:
        print("Welcome to the student managent system")
        print("""
        1. Student Add karo
        2. Sab Students dekho
        3. Student Dhundho
        4. Student Delete karo
        5. Average Marks
        6. Exit""")

        choice=int(input("Enter the choice :"))

        

        match choice:
                case 1:
                    Student=input("Enter the name of the student :")
                    Roll_No = int(input("Enter the roll_no of the student :"))
                    Marks = int(input("Enter the marks :"))
                    print(f"{Student} is added in the list")

                    students_data[Roll_No] = {
                    "Name": Student,
                    "Marks": Marks }
                    print(students_data[Roll_No])
                    

                case 2:
                    print(students_data)
                    
                case 3:
                    search_roll_no = int(input("Enter the roll to seached :"))
                    if search_roll_no in students_data:
                        print("Student found")
                        print(f"{students_data[search_roll_no]}")
                    else:
                        print("Student no exist")
                    
                case 4:
                    search_roll_no = int(input("Enter the roll to be deleted :"))
                    if search_roll_no in students_data:
                        print("Student found and deleted")
                        del students_data[search_roll_no]
                        Value = int(input("Enter 1 to show list :"))
                        if(Value==1):
                            print(f"{students_data}")

                case 5:
                    avg = total_marks = sum(details["Marks"] for details in students_data.values())
                    if len(students_data) > 0:
                     print(avg/(len(students_data)))

                case 6:
                    print("👍")