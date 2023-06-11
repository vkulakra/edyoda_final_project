import csv


class User:
    def __init__(self, name, phone, address, email, password, is_admin):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.password = password
        self.is_admin = is_admin


class Item:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class OrderHistory:
    def __init__(self, id, email, food_id):
        self.id = id
        self.email = email
        self.food_id = food_id


user_l = []
order_l = []
item_l = []
order_history_l = []
user_order_history_l = []


def user_choice():
    print("*"*25, "USER PAGE", "*"*25)
    print("(1) REGISTER")
    print("(2) LOGIN")
    print("_"*70)


def read_user_csv():
    with open("user_data.csv", "r") as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            user_l.append(
                User(line[0], line[1], line[2], line[3], line[4], line[5]))


def write_user_csv():
    with open("user_data.csv", "w", newline="") as fp:
        csv_writer = csv.writer(fp)
        for i in user_l:
            csv_writer.writerow(
                [i.name, i.phone, i.address, i.email, i.password, i.is_admin])


def read_item_csv():
    with open("item_data.csv", "r") as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            item_l.append(
                Item(line[0], line[1], line[2], line[3], line[4], line[5]))


def read_order_history():
    with open("order_history.csv", "r") as fp:
        csv_reader = csv.reader(fp)
        for line in csv_reader:
            order_history_l.append(OrderHistory(line[0], line[1], line[2]))


def write_order_history():
    with open("order_history.csv", "w", newline="") as fp:
        csv_writer = csv.writer(fp)
        for j in order_history_l:
            csv_writer.writerow([j.id, j.email, j.food_id])


def add_data():
    user_input = User(input("Enter Name: "), input("Enter Phone No.: "), input("Enter Address: "),
                      input("Enter Email: "), input("Enter Password: "), "N")
    emailExists = False
    for user in user_l:
        if user_input.name2 == user.name2:
            print("This Email already exists")
            emailExists = True
            break
    if not emailExists:
        user_l.append(user_input)
        write_user_csv()


def login():
    print("*" * 25, "WELCOME", "*" * 25)
    login_user = input("username: ")
    login_password = input("Enter Password: ")
    for user in user_l:
        if login_user == user.name and login_password == user.password:
            print("_"*70, "\n\nSuccessfully logged-in")
            return user
    print("Credentials doesn't match")
    return ""


def login_action():
    read_item_csv()
    read_order_history()
    print("\n", "*" * 25, "USER OPTIONS", "*" * 25)
    print("(1) UPDATE PROFILE")
    print("(2) PLACE NEW ORDER")
    print("(3) ORDER HISTORY")
    print("(4) EXIT")
    action1 = input("Enter Choice: ")
    if action1 == "1":
        update_profile()
    elif action1 == "2":
        new_order()
    elif action1 == "3":
        order_history()
    elif action1 == "4":
        print("exit func.")
    else:
        print("Choose Valid Option")
        login_action()


def update_profile():
    print("\n", "*"*25, "EDIT PROFILE", "*"*25)
    print("(1) NAME")
    print("(2) PHONE")
    print("(3) ADDRESS")
    print("(4) PASSWORD")
    update_action = input("Choose Option to Update or press 5 to go back: ")
    print("_" * 70)
    for user in user_l:
        if logged_in_user.email == user.email:
            if update_action == "1":
                user.name = input("Enter new name: ")
                logged_in_user.name = user.name
            elif update_action == "2":
                user.phone = input("Enter new phone: ")
                logged_in_user.phone = user.phone
            elif update_action == "3":
                user.address = input("Enter new address: ")
                logged_in_user.address = user.address
            elif update_action == "4":
                user.password = input("Enter new password: ")
                logged_in_user.password = user.password
            elif update_action == "5":
                login_action()
            else:
                print("Please choose proper option")
                update_profile()
    write_user_csv()
    login_action()


def show_food_items():
    print("\n", "*"*25, "FOOD MENU", "*"*25, "\n")
    print("ID", "\t\t", "NAME", "\t\t\t\t", "QUANTITY", "\t", "PRICE")
    for item in item_l:
        print("           ")
        print(item.food_id, "\t", item.name, "\t\t",
              item.quantity, "\t\t", "₹"+item.price)


def calculate_total():
    total_amt = 0
    for order in order_l:
        total_amt += int(order.price) - (int(order.price)
                                         * int(order.discount) / 100)
    return total_amt


def new_order():
    show_food_items()
    print("*"*70)
    order_input = input(
        "Enter Food ID you wish to order separating using comma: ")
    order_input1 = order_input.split(",")
    for i in order_input1:
        for food in item_l:
            if i == food.food_id:
                order_l.append(food)
    print("\n", "*"*25, "YOUR ODER", "*"*25, "\n")
    print("Below are the ordered items: \n")
    for order in order_l:
        print(order.name, order.quantity, order.price, "\n")
    order_amount = calculate_total()
    print("*"*25, "BILL", "*"*25)
    print("Your total amount is {}.\n".format(order_amount))
    print("(1) CONFIRM ORDER")
    print("(2) ADD ITEM")
    print("(3) GO BACK\n")
    confirm_order_action = input("Enter your option: ")
    if confirm_order_action == "1":
        print("_" * 70, "\n")
        print("Your order is confirmed\n\n")
        add_history()
        login_action()
    elif confirm_order_action == "2":
        new_order()
    elif confirm_order_action == "3":
        order_l.clear()
        login_action()
    else:
        print("Choose valid option")


def add_history():
    history_id = get_history_id()
    for order in order_l:
        order_history_l.append(OrderHistory(
            history_id, logged_in_user.email, order.food_id))
    write_order_history()


def get_history_id():
    if len(order_history_l) == 0:
        h_id = "1"
    else:
        h_id = str(int(order_history_l[-1].id) + 1)
    return h_id


def order_history():
    for order in order_history_l:
        if logged_in_user.email == order.email:
            user_order_history_l.append(order)
    print("Your order is as follows: ")
    initial_id = user_order_history_l[0].id
    string_order = ""
    for user_order_history in user_order_history_l:
        for item in item_l:
            if item.food_id == user_order_history.food_id:
                if initial_id == user_order_history.id:
                    string_order = string_order+item.name+" | "
                    break
                else:
                    print(string_order)
                    string_order = ""+item.name+" | "
                    initial_id = user_order_history.id
        if user_order_history_l[-1] == user_order_history:
            print(string_order)
    login_action()

# Admin Code


def admin_choice():
    print("\n", "*" * 25, "ADMIN OPTIONS", "*" * 25)
    print("(1) ADD ITEM")
    print("(2) EDIT FOOD ITEM")
    print("(3) VIEW FOOD ITEMS")
    print("(4) REMOVE FOOD ITEMS")


def write_item_csv():
    with open("item_data.csv", "w", newline="") as fp:
        csv_writer = csv.writer(fp)
        for i in item_l:
            csv_writer.writerow(
                [i.food_id, i.name, i.quantity, i.price, i.discount, i.stock])


def get_food_id():
    if len(item_l) == 0:
        f_id = 1
    else:
        f_id = int(item_l[-1].food_id) + 1
    return f_id


isValidID = False


def edit_item():
    print("\n", "*" * 25, "EDIT ITEM", "*" * 25)
    food_id = input("ENTER FOOD ID: ")
    isValidID = True
    for item in item_l:
        if food_id == item.food_id:
            print(item.food_id, item.name, item.price)
            print("(1) FOOD NAME")
            print("(2) QUANTITY")
            print("(3) PRICE")
            print("(4) DISCOUNT")
            update_item = input(
                "Choose Option to Update or press 5 to go back: ")
            if update_item == "1":
                item.name = input("Enter New Name: ")
            elif update_item == "2":
                item.quantity = input("Enter Quantity: ")
            elif update_item == "3":
                item.price = input("Enter Price: ")
            elif update_item == "4":
                item.discount = input("Enter Discount")
            elif update_item == "5":
                admin_choice()
    write_item_csv()
    validID = False
    print("Enter valid Food ID")
    edit_item()


def add_item():
    print("\n", "*" * 25, "ADDING NEW ITEM", "*" * 25)
    item_input = Item(get_food_id(), input("Food Name: "), input("Quantity(100ml, 250gm, 4pc): "),
                      input("Price: "), input("Discount: "), input("Stock: "))
    item_l.append(item_input)
    write_item_csv()


def view_items():
    with open("item_data.csv", "r") as fp:
        for i in csv.DictReader(fp):
            print(i)


def remove_item():
    del_food_id = input("Enter Food ID for removing item: ")
    for i in item_l:
        if del_food_id == i.food_id:
            item_l.remove(i)
            break
    write_item_csv()


def admin_action():
    read_item_csv()
    while True:
        admin_choice()
        action = input("CHOOSE OPTION: ")
        if action == "1":
            add_item()
        elif action == "2":
            edit_item()
        elif action == "3":
            view_items()
        elif action == "4":
            remove_item()
        else:
            print("PLEASE CHOOSE PROPER OPTION")


read_user_csv()
while True:
    user_choice()
    action = input("\nEnter Choice: ")
    if action == "1":
        add_data()
    elif action == "2":
        logged_in_user = login()
        if logged_in_user == "":
            continue
        else:
            if logged_in_user.is_admin == "Y":
                admin_action()
            else:
                login_action()
