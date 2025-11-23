
# Students data list : ( Student database as Nested List ) 
students_data = [['Abu Talib', '44', '59', '98', '45', '85', '36'], ['Ahmad', '72', '55', '33', '77', '42', '47'], ['Akbar', '84', '39', '38', '47', '66', '82'], ['Ali', '88', '67', '58', '96', '99', '37'], ['Asghar', '75', '73', '47', '62', '34', '58'], ['Ashraf', '99', '55', '68', '69', '37', '72'], ['Bashir', '53', '59', '70', '45', '87', '59'], ['Bilal', '82', '67', '73', '75', '50', '57'], ['Faheem', '83', '67', '36', '92', '57', '74'], ['Farooq', '36', '44', '86', '76', '64', '54'], ['Haider', '86', '52', '87', '60', '54', '94'], ['Hammad', '96', '74', '73', '55', '59', '50'], ['Hamza', '47', '34', '69', '41', '83', '86'], ['Idrees', '47', '44', '93', '98', '52', '98'], ['Iftikhar', '80', '57', '97', '66', '82', '87'], ['Ikram', '48', '81', '41', '78', '48', '39'], ['Imran', '46', '77', '55', '93', '85', '97'], ['Ishfaq', '87', '35', '40', '44', '55', '68'], ['Jawad', '82', '50', '82', '42', '72', '55'], ['Kashaan', '82', '96', '50', '79', '63', '84'], ['Maqbool', '68', '69', '39', '76', '82', '84'], ['Mudassir', '62', '37', '87', '75', '36', '37'], ['Muneeb', '53', '82', '37', '94', '99', '93'], ['Mushtaq', '88', '59', '64', '78', '73', '52'], ['Naveed', '33', '45', '54', '52', '83', '51'], ['Nazir', '51', '50', '89', '64', '38', '54'], ['Qaiser', '85', '95', '37', '40', '61', '75'], ['Qasim', '90', '54', '94', '70', '78', '84'], ['Qayoom', '85', '93', '37', '76', '87', '39'], ['Rashid', '84', '36', '52', '69', '58', '80'], ['Riaz', '92', '54', '63', '45', '59', '45'], ['Roman', '74', '64', '76', '93', '93', '40'], ['Safwaan', '90', '54', '58', '94', '71', '79'], ['Salman', '58', '47', '91', '37', '35', '75'], ['Sameer', '42', '72', '67', '61', '95', '42'], ['Saqlain', '83', '89', '37', '75', '66', '95'], ['Shabir', '82', '74', '86', '57', '95', '42'], ['Shfique', '55', '96', '75', '44', '92', '76'], ['Siddique', '58', '49', '41', '35', '93', '68'], ['Sufyan', '59', '81', '40', '89', '35', '72'], ['Tanveer', '80', '97', '46', '83', '71', '56'], ['Ubaidullah', '67', '45', '82', '83', '63', '43'], ['Umar', '56', '66', '92', '93', '37', '44'], ['Usman', '44', '51', '57', '48', '83', '72'], ['Waseem', '58', '64', '43', '83', '52', '79'], ['Zaeem', '90', '95', '91', '42', '44', '35'], ['Zahid', '71', '33', '75', '46', '43', '99'], ['Zeshaan', '61', '92', '58', '89', '71', '70']]

# Calculate [ TOTAL MARKS, PERCENTAGE, STATE(Pass/Fail), GRADES(90>=A, 80>=B, 70>=C, 60>=D, 60<F), FINE(60<$10,40<$30) ]
class StudentClass :
    college_name = "Superior College"       # class-attr
    section = "CSBA"                        # class-attr
    incharge = "Sir Ubaid"                  # class-attr

    def __init__(self,student_details):  # instructor
        self.name = student_details[0]     # separating name form list 
        self.mark_list = student_details[1:]   # separating marks from list

    def all_details(self):       # printing all the details of student
        print(f'Name : {self.name}')
        print(f'College Name = {self.college_name}')
        print(f'Section = {self.section}')
        print(f'Incharge = {self.incharge}')
        self.__marks()
        print(f'Total Marks : {self.total_marks()}')
        print(f'Percentage : {int((self.total)*100/600)}%')
        print(f'Grade : {self.grade()}')
        print(f'Status : {self.status()}')
        print(f'Fine : {self.fine()}')
        
    def __marks(self):    # marks of each subject : ( private method )
        print(f'English : {self.mark_list[0]}, Math : {self.mark_list[1]}, Computer : {self.mark_list[2]}, Physics : {self.mark_list[3]}, Chemistry : {self.mark_list[4]}, Statistics : {self.mark_list[5]}')
    
    def total_marks(self):      # calculating total marks of student
        self.total = 0
        for val in self.mark_list:      # calulating using a for loop
            self.total += int(val)      # adding all the marks
        return self.total   # method returns total-marks

    def percentage(self):       # calculating percentage of student
        self.total_marks()
        return round((self.total)*100/600,2) # method returns percentage

    def grade(self):            # calculating grade of student
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
            return "F"   # method returns Grade

    def status(self):           #calculating status of student
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

# ------ Student details from Database on the base of input -----
roll_no = int(input("Enter the roll_no of Student : "))     # inputing roll-no 
student_details = students_data[roll_no-1]    # Calculating the index from roll-no
student = StudentClass(student_details)  # creating as an object of that student

# Showing the details of the student from using class methods : 
choice = input("Want to see the details of the student | yes or no : ")
while(choice=="yes"):       
    print("Enter =>  name, college, section, incharge, marks, total marks, percentage, grade, status, fine, all details")
    show = input("Enter what to show ? : ")     # taking input what to show
    if(show=="name"):
        print(f'Name : {student.name}') 
    elif(show=="college"):
        print(f'College : {student.college_name}')
    elif(show=="section"):
        print(f'Section : {student.section}')
    elif(show=="incharge"):
        print(f'Incharge : {student.incharge}')
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
            print("Student not pursuing this Subject...")
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
        print("Trying to access Invalid things...")

    choice = input("Want to Exit Enter ( yes | no ) : ")  # taking choice for exit

#  Adding a new student at the last of students datalist : 
choice1 = input("Want to add a new Student in Database | yes or no : ")
if(choice1 == "yes"):
    print("Enter values separated by Comma in this way =>  Name,English,Math,Computer,Physics,Chemistry,Statistics")
    new_student = input("Enter details as a list : ")
    new_student_data = new_student.split(",")
    students_data.append(new_student_data)
    choice1 = input("Want to add a more Students in Database | yes or no : ")

# Removing a student from students data list : 
choice2 = input("Want to remove a Student from Database | yes or no : ")
if(choice2 == "yes"):
    roll_number = int(input("Enter Roll No. of student that want to remove : "))
    name = input("Enter Name of that student : ")
    student = students_data[(roll_number-1)]
    if(student[0] == name):
        students_data.__delitem__(roll_number)
        print(f'Removed successfully..  {len(students_data)} students are remaining.')
    else:
        print("Student Data not matched, Try again later...")
    choice2 = input("Want to remove more Students from Database | yes or no : ")



