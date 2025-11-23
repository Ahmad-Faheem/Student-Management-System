
import Database         # Accessing the Database in this File

#  --- Defining a Class - that classify student object data ---

class StudentClass :
    college_name = "Superior College"       # class-attr
    section = "CSBA"                        # class-attr

    def __init__(self,student_details):        # instructor ---- 
        self.name = student_details[0]         # separating name form list 
        self.mark_list = student_details[1:]   # separating marks as a separate list

    def all_details(self):       # printing all the details of student  ---- 
        print(f'Name : {self.name}')
        print(f'College Name = {self.college_name}')
        print(f'Section = {self.section}')
        self.__marks()
        print(f'Total Marks : {self.total_marks()}')
        print(f'Percentage : {int((self.total)*100/600)}%')
        print(f'Grade : {self.grade()}')
        print(f'Status : {self.status()}')
        print(f'Fine : {self.fine()}')
        
    def __marks(self):    # marks of each subject : ( private method )
        print(f'English : {self.mark_list[0]}, Math : {self.mark_list[1]}, Computer : {self.mark_list[2]}, Physics : {self.mark_list[3]}, Chemistry : {self.mark_list[4]}, Statistics : {self.mark_list[5]}')
    
    def total_marks(self):      # calculating total marks of student  ---- 
        self.total = 0
        for val in self.mark_list:      # calulating using a for loop
            self.total += int(val)      # adding all the marks
        return self.total   # method returns total-marks

    def percentage(self):       # calculating percentage of student  ---- 
        self.total_marks()
        return round((self.total)*100/600,2)      # method returns percentage

    def grade(self):            # calculating grade of student   ---- 
        self.total_marks()
        if(((self.total)*100/600)>=90):
            return "A"
        elif(((self.total)*100/600)>=80):
            return "B"
        elif(((self.total)*100/600)>=70):
            return "C"
        elif(((self.total)*100/600)>=60):
            return "D"
        else:
            return "F"

    def status(self):           # calculating status of student  ---- 
        self.total_marks()
        if(((self.total)*100/600)>=60):
            return "Pass"
        else:
            return "Fail"   # method returns status

    def fine(self):             # calculating fine of student
        self.total_marks()
        if(((self.total)*100/600)<60 and ((self.total)*100/600)>=40):
            return "10 Dollars"
        elif(((self.total)*100/600)<40 and ((self.total)*100/600)>=0):
            return "30 Dollars"
        else : 
            return None     # method returns fine
        
   
# --- Fuctions Defined for Adding / Removing / show Details  ---

def show_details():
    roll_no = int(input("Enter the roll_no of Student : "))     # inputing roll-no 
    student_info = Database.students_database[roll_no-1]    # Calculating the index from roll-no
    student = StudentClass(student_info)  # creating as an object of that student
    print("Enter =>  name, college, section, marks, total marks, percentage, grade, status, fine, all details")
    show = input("Enter what to show ? : ")     # taking input what to show
    if(show=="name"):
        print(f'Name : {student.name}') 
    elif(show=="college"):
        print(f'College : {student.college_name}')
    elif(show=="section"):
        print(f'Section : {student.section}')
    elif(show=="marks"):
        print("Subjects =>  english, math, computer, physics, chemistry, statistics")
        subject = input("Marks of which Subject? : ")   # taking subject as input
        if(subject=="english"):
            print(f'English : {student.mark_list[0]}')
        elif(subject=="math"):
            print(f'Math : {student.mark_list[1]}')
        elif(subject=="computer"):
            print(f'Computer : {student.mark_list[2]}')
        elif(subject=="physics"):
            print(f'Physics : {student.mark_list[3]}')
        elif(subject=="chemistry"):
            print(f'Chemistry : {student.mark_list[4]}')
        elif(subject=="statistics"):
            print(f'Statistics : {student.mark_list[5]}')
        else:
            print("Student not enrolled in this Subject...")
    elif(show=="total marks"):
        print(f'Total Marks : {student.total_marks()}')
    elif(show=="percentage"):
        print(f'Percentage : {int(student.percentage())}%')
    elif(show=="grade"):
        print(f'Grade : {student.grade()}')
    elif(show=="status"):
        print(f'Status : {student.status()}')
    elif(show=="fine"):
        print(f'Fine : {student.fine()}')
    elif(show=="all details"):
        student.all_details()
    else : 
        print("Trying to access Invalid data...")

def add_student():
    print("Enter data separated by Comma in this order =>  Student_Name,English,Math,Computer,Physics,Chemistry,Statistics")
    new_student = input("Enter details : ")
    new_student_data = new_student.split(",")
    Database.students_database.append(new_student_data)
    print('Successfully added at the last of database. ')

def remove_student():
    roll_number = int(input("Enter Roll No. of student that want to remove : "))
    name = input("Enter Name of that student : ")
    student_info = Database.students_database[(roll_number-1)]
    if(student_info[0] == name):
        print('Student information matched successfully...')
        Database.students_database.__delitem__(roll_number)
        print(f'{name} Removed from database  {len(Database.students_database)} students are remaining.')
    else:
        print("Student Data not matched, Try again...")

# --- Fuctions Defined for Adding / Removing / show Details  ---

# Showing the student details from students Database : 
choice = input("\nWant to see the student information | yes or no : ")
while(choice == "yes"):
    show_details()
    choice = input("Want to see the student information | yes or no : ")
    
# Adding a new student at the last of students Database : 
choice1 = input("\nWant to add a new Student in Database | yes or no : ")
while(choice1 == "yes"):
    add_student()
    choice1 = input("Want to add a more Students in Database | yes or no : ")

# Removing a student from students Database : 
choice2 = input("\nWant to remove a Student from Database | yes or no : ")
while(choice2 == "yes"):
    remove_student()
    choice2 = input("Want to remove more Students from Database | yes or no : ")

#------------------------------------------------------------------------------------
