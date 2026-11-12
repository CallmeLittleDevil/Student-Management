import os

FILENAME = "students.txt"
VALID_MAJORS = ["Ce", "F", "M"]

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", encoding="utf-8") as file:
        pass

def get_next_id():
    max_id = 0
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 6:
                try:
                    current_id = int(data[0])
                    if current_id > max_id:
                        max_id = current_id
                except ValueError:
                    pass
    return max_id + 1

while True:
    print("\n" + "="*40)
    print("           Student Management           ")
    print("="*40)
    print("1. Add")
    print("2. Show (Find by Code)")
    print("3. Show All (Table view)")
    print("4. Search (Find by Name)")
    print("5. Delete")
    print("6. Exit")
    print("="*40)
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        s_id = get_next_id()
        print(f"[*] Generated ID for new student: {s_id}")
        
        s_code = input("Enter Student Code: ")
        f_name = input("Enter Firstname: ")
        l_name = input("Enter Lastname: ")
        
        while True:
            major_input = input("Enter Major (Ce, F, M): ").strip()
            
            if major_input.lower() == "ce":
                major = "Ce"
            else:
                major = major_input.upper()
                
            if major in VALID_MAJORS:
                break
            else:
                print("Invalid Major! You must choose from Ce, F, or M.")
                
        city = input("Enter City: ")
        
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.write(f"{s_id},{s_code},{f_name},{l_name},{major},{city}\n")
        print("Student added successfully!")
        
    elif choice == '2':
        show_code = input("Enter Student Code to show: ")
        found = False
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6 and data[1] == show_code:
                    print("\n👤 Student Details:")
                    print(f"ID: {data[0]}\nCode: {data[1]}\nName: {data[2]} {data[3]}\nMajor: {data[4]}\nCity: {data[5]}")
                    found = True
                    break
        if not found:
            print("Student not found.")

    elif choice == '3':
        print("\n" + "-"*82)
        print(f"| {'ID':<5} | {'Code':<10} | {'Firstname':<12} | {'Lastname':<12} | {'Major':<12} | {'City':<10} |")
        print("-" * 82)
        
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print(f"| {'No students found in the database.':<78} |")
            else:
                for line in lines:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        print(f"| {data[0]:<5} | {data[1]:<10} | {data[2]:<12} | {data[3]:<12} | {data[4]:<12} | {data[5]:<10} |")
        print("-" * 82)

    elif choice == '4':
        search_name = input("Enter Firstname to search: ").lower()
        found = False
        print("\nSearch Results:")
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6 and data[2].lower() == search_name:
                    print(f"- {data[2]} {data[3]} (Code: {data[1]}, Major: {data[4]})")
                    found = True
        if not found:
            print("No student found with that name.")

    elif choice == '5':
        del_code = input("Enter Student Code to delete: ")
        deleted = False
        
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            
        with open(FILENAME, "w", encoding="utf-8") as file:
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 6 and data[1] == del_code:
                    deleted = True
                    continue
                file.write(line)
                
        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")