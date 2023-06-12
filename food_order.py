class Admin():
    def __init__(self,foodID, name, quantity, price, discount, stock):
        self.foodID = foodID
        self.name = name
        self.quantity =  quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        self.user_info = {}
        
    def show_foods(self):
        for i in range(self.name):
            for j in range(self.quantity):
                if i == 0:
                    if j == 0:
                        print(' ', end= ' ')
                    else:
                        print(j, end=' ')
                elif j == 0:
                    print(i, end=' ')
                else:
                    if self.is_food_ordered(i,j):
                        print('ordered', end=' ')
                    else:
                        print('Not ordered', end=' ')
    
    def buy_foods(self):
        foods_items = input("Enter food name: ")
        quantitys = int(input("Enter quantity: "))
        
        item_price =  100
        total_price = self.price * self.quantity
        if quantitys <= 5:
            item_price = 100        
        else:
            item_price = 80
        option = int(input(f'you have selected row is {foods_items} amd column is {quantitys}, so your ticket price is {total_price}, if you still want to book your order enter 1 - yes, 2 - no '))
        if option == 1:
            name = input("Enter your name: ")
            gender = input('enter your gender: ')
            age = int(input('enter your age: '))
            phone = int(input("enter your phone no. : "))
            self.user_details = [name, gender, age, phone]  
            print(self.user_details)
            print('ticker booked successfully')
        else:
            print('oops... Thanks for connecting with us')
    
    def user_info(self):
        foods_items = input("Enter food name: ")
        quantitys = int(input("Enter quantity: "))
        total_price = self.price * self.quantity
        user_details = self.user_details.get(total_price, None)
        if user_details:
            print(f'name of user: {user_details[0]}')
            print(f'genger is: {user_details[1]}')            
    def is_order_booked(self, rows, coloumns):
        total_price = self.price * self.quantity
        if total_price in self.user_details.keys():
            return True
        return False 