import pandas as pd
import os
import subprocess

class StockControlSystem:

#---------------------------Functions Start Here---------------------------#

     def verify_login(self):
          self.__user = 'admin'
          self.__pwd = 'password123'
          attempts = 3
          username = input('Enter username: ')
          password = input('Enter password: ')
          while (username != self.__user or password != self.__pwd) and attempts > 1:
               attempts -= 1
               print(f'Incorrect credentials. You have {attempts} attempts left.')
               username = input('Enter username: ')
               password = input('Enter password: ')
          if username != self.__user or password != self.__pwd:
               print('Too many incorrect attempts. Exiting the system.')
               exit()

     
     def clean_screen(self):
          # system() is deprecated; use subprocess instead
          command = 'cls' if os.name == 'nt' else 'clear'
          subprocess.run(command, shell=True)

     def show_stock(self): 
          print(df)

     def create_stock_file(self):
          df = pd.DataFrame(columns=['Name','Quantity','Price'])
          df.to_csv('stock.csv', index=False)
          return df

     def add_new_item(self):
          item = input('Enter item name: ')
          if item in df['Name'].values:
               print('Item already exists')
               return df
          qty = int(input('Enter quantity: '))
          price = float(input('Enter price: '))
          df.loc[len(df)] = [item,qty,price]
          print(f"{item} added successfully")
          return df

     def update_item(self):
          item = input("Enter item name to update: ")
          if item in df['Name'].values:
               qty = int(input("Enter a new quantity: "))
               price = float(input("Enter a new price: "))
               df.loc[df['Name']==item, 'Price'] = price
               df.loc[df['Name']==item, 'Quantity'] = qty
               print(f"{item} updated to {qty} with price {price}")
          else:
               print("Item not found")

     def remove_item(self):
          item = input("Enter item name to remove: ")
          if item in df['Name'].values:
               df.drop(df[df['Name']==item].index, inplace=True)
               print(f"{item} removed successfully")
          else:
               print("Item not found")

     def check_low_stock(self,low=20):
          print('These stock are low in quantity: ')
          print(df[df['Quantity'] <= low])

#---------------------------Functions End Here---------------------------#

#---------------------------Login Interface---------------------------#
print('welcome to stock control system')
print('--------------------------------')
scs = StockControlSystem()
scs.verify_login()
scs.clean_screen()
print('Login successful!')
input('Press Enter key to continue....')

#---------------------------Main Program---------------------------#
scs.clean_screen()
print('Choose an option to proceed: ')
print('1. Proceed to existing stock file')
print('2. Create a new stock file')
choice = input('Enter your choice (1 or 2): ')
scs.clean_screen()
if choice == '1':
     try:
          df = pd.read_csv('stock.csv')
     except FileNotFoundError:
          print('No existing stock file found. Please create a new stock file.')
     df = pd.read_csv('stock.csv')
elif choice == '2':
     df = scs.create_stock_file()
     print('New stock file created successfully')
else:
     print('Invalid choice. Exiting the system.')
     exit()

while True:
     scs.clean_screen()
     print('1. Show Stock')
     print('2. Add New Item')
     print('3. Update Item Quantity')
     print('4. Remove Item')
     print('5. Check Low Stock')
     print('6. Save and Exit')
     print('7. Exit')

     choice = input('Enter your choice (1-8): ')
     if choice == '1':
          scs.show_stock()
          input('Press Enter key to continue....')
     elif choice == '2':
          scs.add_new_item()
          input('Press Enter key to continue....')
     elif choice == '3':
          scs.update_item()
          input('Press Enter key to continue....')
     elif choice == '4':
          scs.remove_item()
          input('Press Enter key to continue....')
     elif choice == '5':
          scs.check_low_stock()
          input('Press Enter key to continue....')
     elif choice == '6':
          df.to_csv('stock.csv', index=False)
          print('Exiting the system. Goodbye!')
          break
     elif choice == '7':
          print('Exiting without saving. Goodbye!')
          break
     else:
          print('Invalid choice. Please try again.')
          input('Press Enter key to continue....')
scs.clean_screen()