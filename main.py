from food_order import Admin



class Main:
    def execute(self, choice):
        if choice == 1:
            print('show foods:')
            order_object.show_foods()
        if choice == 2:
            print('show foods')
            order_object.buy_foods()
        if choice == 3:
            print('show user info') 
            order_object.user_info()          
        if choice == 0:
            print('visit again')
if __name__ == '__main__':
    name = input("Enter food name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input('enter a price: '))
    discount = int(input('enter a discount: '))
    stock = int(input('enter a stock: '))
    order_object = Admin(name,quantity,price, discount, stock)
    obj = Main()
    while True:
        choice = int(input('Enter-1 to show foods, 2 for tickets, 3 for booked seats, 4 for user info, 0 to exit: '))
        obj.execute(choice)