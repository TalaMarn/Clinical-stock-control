import pandas as pd
import os

df = pd.read_csv('stock.csv')
def show_stock(): 
     print(df)

def add_new_item():
     item = input('Enter item name: ')
     if item in df['Name'].values:
          print('Item already exists')
          return df
     qty = int(input('Enter quantity: '))
     price = float(input('Enter price: '))
     df.loc[len(df)] = [item,qty,price]
     print(f"{item} added successfully")
     return df

def update_item():
     item = input("Enter item name to update: ")
     if item in df['Name'].values:
          qty = int(input("Enter a new quantity: "))
          df.loc[df['Name']==item, 'Quantity'] = qty
          print(f"{item} updated to {qty}")
     else:
          print("Item not found")

def remove_item():
     item = input("Enter item name to remove: ")
     if item in df['Name'].values:
          df.drop(df[df['Name']==item].index, inplace=True)
          print(f"{item} removed successfully")
     else:
          print("Item not found")

def check_low_stock(low=20):
     print('These stock are low in quantity: ')
     print(df[df['Quantity'] <= low])


while True:
     os.system('cls')
     print('welcome to stock control system')
     print('--------------------------------')
     print('1. Show Stock')
     print('2. Add New Item')
     print('3. Update Item Quantity')
     print('4. Remove Item')
     print('5. Check Low Stock')
     print('6. Exit')

     choice = input('Enter your choice (1-6): ')
     os.system('cls')
     if choice == '1':
          show_stock()
          input('Press any key to continue....')
          os.system('Cls')
     elif choice == '2':
          add_new_item()
          input('Press any key to continue....')
          os.system('Cls')
     elif choice == '3':
          update_item()
          input('Press any key to continue....')
          os.system('Cls')
     elif choice == '4':
          remove_item()
          input('Press any key to continue....')
          os.system('Cls')
     elif choice == '5':
          check_low_stock()
          input('Press any key to continue....')
          os.system('Cls')
     elif choice == '6':
          print('Exiting the system. Goodbye!')
          os.system('Cls')
          break
     else:
          print('Invalid choice. Please try again.')
          input('Press any key to continue....')
          os.system('Cls')