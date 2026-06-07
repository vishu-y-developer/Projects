"""Ek Contact Book banao jisme:

1. Contact Add karo
   - Name, Phone (10 digit), Email, City lo
   - Duplicate name na ho

2. Sab Contacts dekho
   - Sab contacts achhe se print karo

3. Contact Dhundho
   - Name se search karo
   - Case insensitive ho (ALI ya ali dono kaam karein)

4. Contact Update karo
   - Phone ya Email badlo

5. Contact Delete karo
   - Delete se pehle confirm karo y/n

6. Exit"""

contact = {}
while True:
    print("""
        1. Contact Add karo

        2. Sab Contacts dekho

        3. Contact Dhundho

        4. Contact Update karo

        5. Contact Delete karo
                
        6. Exit""")
    choice = int(input("Enter the choice: "))
    match choice:

        case 1:
            Name = input("Enter the name: ")
            City = input("Enter the city: ")
            Emuail = input("Enter the email: ")
            Phone_no = int(input("Enter the phone no: "))
            if(len(str(Phone_no))!=10):
                print("Invalid Phone no")
                
            elif(Name in contact):
                 print("Contact already present")
                
            else:
                contact[Name] = {
                    "City" : City,
                    "Email" : Emuail,
                    "Phone_no" : Phone_no
                }
                print("Phone no added")
        case 2:
            for name, details in contact.items():
                print(f"Name: {name}")
                print(f"City: {details['City']}")
                print(f"Email: {details['Email']}")
                print(f"Phone: +91-{details['Phone_no']}")
                print("---")
        case 3:
            print("Case Sensitive")
            s = input("Enter name to search: ")
            if s in contact:
                print("Found")
                print(f"Name: {s}")
                print(f"City: {contact[s]['City']}")
                print(f"Email: {contact[s]['Email']}")
                print(f"Phone_no: {contact[s]['Phone_no']}")   
            else:
                print("Not found")
        case 4:
            s = input("Enter the name of the contact: ")
            if s in contact:
                em = input("Enter the new email: ")
                Phone = input("Enter the new Phone no: ")
                if(len(str(Phone))!=10):
                    print("Invalid Phone no")
                else:
                    contact[s]["Phone_no"] = Phone
                    print("Contact Updated")
                    contact[s]["Emuail"] = em
                    print(contact[s])
            else: 
                print("Contact not reg")
        case 5:
            sd = input("Enter the contact detail to deletd: ")
            del contact[sd]
            print("contact is deleted")
        case 6:
            print("")
            break