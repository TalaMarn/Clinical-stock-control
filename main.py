import pandas as pd
import os

def clean_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def show_stock(): 
     print(df)

def create_stock_file():
     df = pd.DataFrame(columns=['Name','Quantity','Price'])
     df.to_csv('stock.csv', index=False)
     return df

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

print('welcome to stock control system')
print('--------------------------------')
print('Choose an option to proceed: ')
print('1. Proceed to existing stock file')
print('2. Create a new stock file')
choice = input('Enter your choice (1 or 2): ')
clean_screen()
if choice == '1':
     df = pd.read_csv('stock.csv')
elif choice == '2':
     df = pd.DataFrame(columns=['Name','Quantity','Price'])
     df.to_csv('stock.csv', index=False)

while True:

     print('1. Show Stock')
     print('2. Add New Item')
     print('3. Update Item Quantity')
     print('4. Remove Item')
     print('5. Check Low Stock')
     print('6. Create Stock File')
     print('7. Save and Exit')
     print('8. Exit')

     choice = input('Enter your choice (1-8): ')
     if choice == '1':
          show_stock()
          input('Press any key to continue....')
          clean_screen()
     elif choice == '2':
          add_new_item()
          input('Press any key to continue....')
          clean_screen()
     elif choice == '3':
          update_item()
          input('Press any key to continue....')
          clean_screen()
     elif choice == '4':
          remove_item()
          input('Press any key to continue....')
          clean_screen()
     elif choice == '5':
          check_low_stock()
          input('Press any key to continue....')
          clean_screen()
     elif choice == '6':
          create_stock_file()
          print('Stock file created successfully')
          input('Press any key to continue....')
          clean_screen()
     elif choice == '7':
          df.to_csv('stock.csv', index=False)
          clean_screen()
          print('Exiting the system. Goodbye!')
          break
     elif choice == '8':
          clean_screen()
          print('Exiting without saving. Goodbye!')
          break
     else:
          print('Invalid choice. Please try again.')
          input('Press any key to continue....')
          clean_screen()