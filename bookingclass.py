#### ========= Configure ========= ####
ROOM_NUMBER = "roomnumber.txt"
STUDENT = "student.txt"

#### ========= Load & Save =========####
def load_rooms(room_file):
    room_number = {}
    try:
        with open(room_file, 'r', encoding='utf-8') as booking:
            for line in booking:
                num, owner = line.strip().split(',')
                room_number[int(num)] = owner 
                if owner != "None":
                    room_number[int(num)] = {
                        'num': num,
                        'owner': owner,
                        'status': False
                    } 
                
                else:
                    None
    
    except FileNotFoundError:
        print(f"⚠️ ไม่พบไฟล์ {room_file}")
    return room_number

def load_students(student_file):
    student_list = {}
    try:
        with open(student_file, 'r', encoding='utf-8') as students:
            for line in students:
                fname, lname = line.strip().split(',')
                student_list[f"{fname} {lname}"] = {
                    'fname': fname,
                    'lname': lname
                }
    except FileNotFoundError:
        print(f"⚠️ ไม่พบไฟล์ {student_file}")
    return student_list
                
#### ========= Booking System ========= ####

class room:
    def __init__(self, num, owner):
        self.num = num
        self.owner = owner
        self.status = True

class student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

def booking_room(num, fname, lname) -> bool:
    global room_list, student_list
    for room in room_list:
        if room.num == num and room.status:
            for student in student_list:
                if student.fname == fname and student.lname == lname:
                    room.status = False
                    return True
        return False

##### ========= Main Program ========= ####

room_list = [room(room_num, owner) for room_num, owner in load_rooms(ROOM_NUMBER).items()]
student_list = [student(fname, lname) for fname, lname in load_students(STUDENT).items()]

while True:
    try:
        input_num = int(input("Enter room number to book: "))
        input_fname = input("Enter first name: ")
        input_lname = input("Enter last name: ")
        is_sussess = booking_room(input_num, input_fname, input_lname)
        print("Booking successful" if is_sussess else "Booking failed")
        
        if is_sussess:
            break
    
    except ValueError:
        print("Invalid input. Please enter a valid room number.")

