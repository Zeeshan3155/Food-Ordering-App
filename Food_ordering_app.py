import json
import re
from datetime import datetime as dt
from json import JSONDecodeError


class Admin:

    def add_item(self):
        
        name = input("Enter the name of the food item\n")
        quantity = input("Enter the quantity of the food item\n")
        price = int(input("Enter the price of the food item\n"))
        discount = input("Enter the discount on the food item\n")
        try:
            file1 = open("food_items.json","r+")
            content = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            content = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(content,file1,indent=4)
        except JSONDecodeError:
            content = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(content,file1,indent=4)  
        
        content[len(content)+1] = {"Name":name,"Quantity":quantity,"Price":price,"Discount":discount}
        file1.seek(0)
        file1.truncate()
        json.dump(content,file1,indent=4)
        file1.close()
        return "sucess"
    
    def edit_food_items(self,id):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
        except JSONDecodeError:
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)  
        para = input("What do you want to edit? (Name, Quantity, Price, Discount)\n")
        if para.lower() == "name":
            new = input("Enter the new name\n")
            if new == food_items[id]["Name"]:
                print("You have entered the same name\n")
            else:
                food_items[id]["Name"] = new

        elif para.lower() == "quantity":
            new = input("Enter the new quantity\n")
            if new == food_items[id]["Quantity"]:
                print("You have entered the same quantity\n")
            else:
                food_items[id]["Quantity"] = new

        elif para.lower() == "price":
            new = int(input("Enter the new price\n"))
            if new == food_items[id]["Price"]:
                print("You have entered the same price\n")
            else:
                food_items[id]["Price"] = new

        elif para.lower() == "discount":
            new = int(input("Enter the new discount.\n"))
            if new == food_items[id]["Discount"]:
                print("You have entered the same discount.\n")
            else:
                food_items[id]["Discount"] = new

        else:
            print("You have entered wrong detail\n")

        file1.seek(0)
        file1.truncate()
        json.dump(food_items,file1,indent=4)
        file1.close()
        return "sucess"

    
    def list_of_items(self):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
            
        except JSONDecodeError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
            file1.close()
        
        for key,value in food_items.items():
            print(f"\nFoodID: {key}")
            for j,k in value.items():
                if j.lower()=="price":
                    print(f"{j}:- INR {k}")   
                else:
                    print(f"{j}:- {k}")            
        
    
    def remove_items(self,id):
        file1 = open("food_items.json","r+")
        food_items = json.load(file1) 
        if id in food_items:
            food_items.pop(id)
            file1.seek(0)
            file1.truncate()
            json.dump(food_items,file1,indent=4)
            print("Food item has been removed")
        else:
            print("Food ID not found.")
        file1.close()

    def stock(self):
        print("Stock Left:\n Tandoori chicken : 10kg\nVegan Burger : 50 pieces\nTuffle Cake : 50 pieces\n")
        

class User:
    regex_name = "^[A-Za-z]+\s?[a-z]*"
    regex_phn = "^[0-9]{10}$"
    regex_email = "^[a-z0-9]+[\.\-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    regex_password = "^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$"
    regex_address = "[\w',-\\/.\s]"


    def __init__(self):    
        self.name = "XYZ"
        self.phn = "1234567890"
        self.email = "xyz@mail.com"
        self.address = "house no.,area,city,state"
        self.password = "$ampLePassword123"
        self.orders = []

    def add_name(self):
        while True:
            name = input("Enter your full name.\n")    
            if bool(re.search(User.regex_name,name)):
                self.name =name
                break
            else:
                print("Enter valid name.\n")
                

    def add_phn(self):
        while True:
            phn = input("Enter you phone number.\n")
            if bool(re.search(User.regex_phn,phn)):
                self.phn = phn
                break
            else:
                print("Enter correct phone number.\n")

    def add_email(self):
        while True:
            email = input("Enter your Email.\n")
            if bool(re.search(User.regex_email,email)):
                self.email = email
                break
            else:
                print("Enter valid email address.\n")

    def add_address(self):
        while True:
            address = input("Enter your full address.\n")
            if bool(re.search(User.regex_address,address)):
                self.address = address
                break
            else:
                print("Enter valid address.\n")

    def set_password(self):
        while True:
            password = input("Enter your password.\n")
            if bool(re.search(User.regex_password,password)):
                self.password = password
                break
            else:
                print('''Enter a valid password.
(Should contain one capital and small letter, one special character, one number and should be of minimum length 8.''')    


    

    def list_of_food(self):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            
        except JSONDecodeError:
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            
             
        for key,value in food_items.items():
            print(f"\nFoodID: {key}")
            for j,k in value.items():
                if j.lower()=="price":
                    print(f"{j}:- INR {k}") 
                
                elif j.lower()=="discount":
                    continue                  
                else:
                    print(f"{j}:- {k}")    
        json.dump(food_items,file1,indent=4)
        file1.close()

    def palce_order(self,food_id,user_mail):
        try:
            file = open("user_info.json","r+")
            content5 = json.load(file) 
        except JSONDecodeError:
            content5 = {}
    
        list_of_order = content5[user_mail]["orders"]
        now = dt.now()
        date_tm = now.strftime("%m/%d/%Y, %H:%M:%S")
        dictt = {date_tm:food_id}
        list_of_order.append(dictt) 
        content5[user_mail]["orders"] = list_of_order
        file.seek(0)
        file.truncate()
        json.dump(content5,file,indent=4)
        file.close()
        return "sucess"         


def admin():
    b2 = Admin()
    admin_name = "Zeeshan"
    admin_password = "1234"
    input_name = input("Enter admin name:(Zeeshan)\n")
    input_password = input("Enter admin password:(1234)\n")
    if input_name == admin_name and input_password == admin_password:
        print("\nHey you have been loged in  as admin!")
        while True:
            option = input('''Select from the following options:
Enter 1 to add food item.
Enter 2 to check stock left.
Enter 3 to see list of food items.
Enter 4 to edit food item using food ID.
Enter 5 to remove food item using food ID.
Enter 6 to exit
''')
            if option == "1":
                response1 = b2.add_item()
                if response1 == "sucess":
                    print("Food item added successfully\n")
                else:
                    print("Unknown problem\n")
        
            elif option == "2":
                b2.stock()

            elif option == "3":
                b2.list_of_items()
        
            elif option == "4":
                id1 = input("Enter the food ID of food item which you want to edit:\n")
                response2 = b2.edit_food_items(id1)
                if response2 == "sucess":
                    print("Food item edited sucessfully.\n")
                else:
                    print("Error in editing food item\n")

            elif option == "5":
                id = input("Enter the food ID of food item you want to remove\n")
                b2.remove_items(id)
            
            elif option == "6":
                break
            else:
                print("Wrong option.\n")
    else:
        print("Wrong admin details.")
        return None
        

def update_profile(user_mail):
    file8 = open("user_info.json","r+")
    content8 = json.load(file8)
    user_in = input("What do you want to update.(Name, Phone, Address, Password)\n")
    if user_in.lower() == "name":
        new = input("Enter the new name\n")
        if new == content8[user_mail]["name"]:
            print("You have entered the same name\n")
        else:
            content8[user_mail]["name"] = new
    
    elif user_in.lower() == "phone":
        new = input("Enter the new phone number.\n")
        if new == content8[user_mail]["phn"]:
            print("You have entered the same phone number.\n")
        else:
            content8[user_mail]["phn"] = new

    elif user_in.lower() == "address":
        new = input("Enter the new address\n")
        if new == content8[user_mail]["address"]:
            print("You have entered the same address\n")
        else:
            content8[user_mail]["address"] = new    

    elif user_in.lower() == "password":
        new = input("Enter the new password\n")
        if new == content8[user_mail]["password"]:
            print("You have entered the same password\n")
        else:
            content8[user_mail]["password"] = new
    
    else:
        print("Invalid option.\n")

    file8.seek(0)
    file8.truncate()
    json.dump(content8,file8,indent=4)
    file8.close()
    return "sucess"

def register_user():
    b1 = User()
    try:
        file = open("user_info.json","r+")
        content = json.load(file) 
    except FileNotFoundError:
        file = open("user_info.json","w+")
        content = {}
    except JSONDecodeError:
        content = {}  
    b1.add_name()
    b1.add_phn()
    b1.add_email()
    b1.add_address()
    b1.set_password()
    try:
        if b1.__dict__["email"] not in content.keys():
            content[b1.__dict__["email"]] = b1.__dict__
            file.seek(0)
            file.truncate()
            json.dump(content,file,indent=4)
            file.close()
            return "sucess"

        elif b1.__dict__["email"] in content.keys():
            file.close()
            return "already"
    except KeyError:    
        content["email"] = b1.__dict__
        file.seek(0)
        file.truncate()
        json.dump(content,file,indent=4)
        file.close()    
        return "sucess"

def user_login():
    try:
        file = open("user_info.json","r+")
        content4 = json.load(file) 
    except FileNotFoundError:
        file = open("user_info.json","w+")
        file.close()
        return ["not_registered"]
    except JSONDecodeError:
        file.close()
        return ["not_registered"]
    login_email = input("Enter your email.\n")
    login_password = input("Enter password.\n")

    if login_email in content4:
        if login_password == content4[login_email]["password"]:
            print(f"\nHey {content4[login_email]['name']}!")
            file.close()
            return ["sucess",login_email]
        else:
            file.close()
            return ["wrong_password"]
    else:
        file.close()
        return ["not_found"]
    
    
def user_menu(user_mail):
    b1 = User()
    while True: 
        print('''What do you wanna do?
Enter 1 to place new order.
Enter 2 to see order history.
Enter 3 to update profile
Enter 4 to exit   
    ''')
        option_user = input("Enter here: ")
        if option_user == "1":
            file1 = open("food_items.json","r+")
            content5 = json.load(file1)
            for i in content5:
                print(f"{i}. {content5[i]['Name']} ({content5[i]['Quantity']}) [INR {content5[i]['Price']}]")
                file1.close()
            user_optn = input("Enter your order (give fooID seperated by commas)\n").split(",")
            reponse7 = b1.palce_order(user_optn,user_mail)
            if reponse7 == "sucess":
                print("Your order is sucessfully palced!\n")
            else:
                print("Unable to place order currently\n")

        elif option_user == "2":
            file9 = open("user_info.json")
            content9 = json.load(file9)
            print("Here's your order history:")
            for i in content9[user_mail]["orders"]:
                for key,value in i.items():
                    print(f"{key} : {value}")
            file9.close()
        
        elif option_user == "3":
            response8 = update_profile(user_mail)
            if response8 == "sucess":
                print("Your profile has been sucessfully updated\n")
            else:
                print("Unable to update profile\n")

        elif option_user == "4":
            break
        
        else:
            print("Wrong option!\n")


while True:
    print('''Hey welcome to my food odering app!
Please select from the followiing options:
Enter 1 for admin.
Enter 2 for new user.
Enter 3 for existing user.
Enter 4 to exit.
''')
    user_option = input("Enter here: ")
    if user_option == "1":
        while True:
            admin_input = input("Login as admin y/n.\n")
            if admin_input.lower()=="y":    
                admin()
            elif admin_input.lower()=="n":
                print("Logged Out.\n")
                break
            else:
                print("Wrong option.\n")
    elif user_option == "2":
        result = register_user()
        if result == "sucess":
            print("You have been sucessfully registered.\n")
        if result == "already":
            print("Already a user.\n")
    elif user_option == "3":
        while True:
            user_input = input("Continue login y/n.\n")
            if user_input.lower()=="y":    
                res = user_login()
                if res[0] == "sucess":
                    user_menu(res[1])
                elif res[0] == "wrong_password":
                    print("Wrong password")
                elif res[0] == "not_found":
                    print("User not found")
                elif res[0] == "not_registered":
                    print("No user info available, first register to the app\n")
            elif user_input.lower()=="n":
                print("Logged Out.\n")
                break
            else:
                print("Wrong option\n")
            
    elif user_option== "4":
        print("Thank you for choosing us.\n")
        break
    else:
        print("Please enter correct option.\n")