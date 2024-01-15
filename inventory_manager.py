#Name: Prerna Prabhu
#Date: 2019-12-09
#File Name: Prerna_Prabhu_Assignment_5_Lists
#Description: An inventory tracking system which updates inventory based on user input
#Test Cases: Edited AP001, AP003, Added Inventory and Deleted Inventory, Used AP005 FOR EVERY FUNCTION

#basically the list of inventory, stored in a txt file

with open("my inventory.txt", 'r') as file:  
    for line in file:
        filelist = list(line.split(", "))

n = len(filelist)
for x in range(n):
    if x%6 == 3:
        filelist[x] = int(filelist[x])
        filelist[x+1]= int(filelist[x+1])
        filelist[x+2] = int(filelist[x+2])
del(filelist[-1])

'''
print(filelist)
'''

#the lists
myinventory = filelist
headings = ["Product Code", "Product", "Description", "Quantity", "Amount Sold", "Total Received"]
searchlist = []



#functions
def inventory_list(): #main menu choice 1
    index = 0
    pos = 0
    print("")
    for x in range (6):
        print(str(headings[pos]).ljust(30), end = "")
        pos +=1
    print("")

    for x in range(len(myinventory)//6):
        for y in range(6):
            print(str(myinventory[index]).ljust(30), end = "")
            index += 1
        print("")
    menu()



def list_details(): #main menu choice 2
    while True:
        try:
            codetodetail = input("Enter the code of the product to list details of: ")
            n = myinventory.index(codetodetail)
            print("\nProduct Selected:", myinventory[n+1],"\nDescription: ", myinventory[n+2])
            break
        except:
            print("Enter a valid code!\n")
    menu()



def add_list(): #main menue choice 3
    while True:
        try:
            code = input("Enter new code including the brand of the phone: ")
            if code in myinventory:
                print("Code already in use!\n")
            else:
                break
        except:
            print("Code must include letters and numbers, try again!")
    while True:
        try:
            product = input("Enter product name: ")
            break
        except:
            print("Product name should include letters.\n")

    while True:
        try:
            description = input("Enter the description for the product: ")
            break
        except:
            print("Product description should include words.\n")
            
    while True:
        try:
            quantity = int(input("Enter the quantity in stock: "))
            break
        except:
            print("Quantity should be an integer.\n")

    while True:
        try:
            sold = int(input("Enter the amount of the product sold to date: "))
            break
        except:
            print("Amount sold should be an integer.\n")

    while True:
        try:
            received = int(input("Enter the amount received to date: "))
            break
        except:
            print("Amount received should be an integer,")

    newproduct = [code, product, description, quantity, sold, received]
    
    myinventory.append(code)
    myinventory.append(product)
    myinventory.append(description)
    myinventory.append(quantity)
    myinventory.append(sold)
    myinventory.append(received)
    print("\nProduct added to inventory.")

    inventory_list()
    menu()


def remove_product(): #main menu choice 4
    while True:
        try:
            code = input("Enter the code of the product that you would like to delete: ")
            if code in myinventory:
                break
            else:
                print("That item does not exist, try again!")
        except:
            print("That item does not exist, try again!")
            
    place = myinventory.index(code)
    for delete in range (6):
        del(myinventory[place])
    
    inventory_list()
    menu()




def edit_product(): #main menu choice 5
    while True:
        code = input("Enter product code to edit: ")
        if code in myinventory:
            break
        else:
            print("That item does not exist, try again! \n")
    n = myinventory.index(code)
    place = myinventory.index(code)
    pos = 0
    print("PRODUCT SELECTED:\n")
    for z in range(6):
        print(str(headings[pos]).ljust(33), end = "")
        pos += 1
    print("")

    for v in range(6):
        print(str(myinventory[n]).ljust(33), end = "")
        n += 1
    print("")

    while True: #edits code
        try:
            code_ans = input("Would you like to edit the product code? (y/n): ")
            if code_ans == "y":
                while True:
                    codechange = input("What would you like to change it to?: ")
                    if codechange in myinventory:
                        print("Code already in use! Try again.")
                    else:
                        break
                place = myinventory.index(code)
                del(myinventory[place])
                myinventory.insert(place, codechange)
                break
                
            elif code_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")


    while True: #edits Product name
        try:
            prod_ans = input("Would you like to edit the product? (y/n): ")
            if prod_ans == "y":
                while True:
                    try:
                        prodchange = input("What would you like to change it to?: ")
                        break
                    except:
                        print("The product name should include words!")
                    
                del(myinventory[place+1])
                myinventory.insert((place+1), prodchange)
                break
                    
            elif prod_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")

            
    while True: #edits description
        try:
            desc_ans = input("Would you like to edit the product description? (y/n): ")
            if desc_ans == "y":
                while True:
                    try:
                        descchange = input("What would you like to change it to?: ")
                        break
                    except:
                        print("The description should include words!")
                    
                del(myinventory[place+2])
                myinventory.insert((place+2), descchange)
                break
                    
            elif desc_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")

    

    while True: #edits quantity in stock
        try:
            quantity_ans = input("Would you like to edit the quantity in stock? (y/n): ")
            if quantity_ans == "y":
                while True:
                    try:
                        quantitychange = int(input("What would you like to change it to?: "))
                        break
                    except:
                        print("The quantity should be a integer! Try again.")

                del(myinventory[place+3])
                myinventory.insert((place+3), quantitychange)
                break
                    
            elif quantity_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")


    while True: #edits total sold to date
        try:
            sold_ans= input("Would you like to edit the amount sold to date? (y/n): ")
            if sold_ans == "y":
                while True:
                    try:
                        soldchange = int(input("What would you like to change it to?: "))
                        break
                    except:
                        print("The amount sold to date should be a integer! Try again.")
                    
                
                myinventory.insert((place+4), soldchange)
                del(myinventory[place+5])
                break
                    
            elif sold_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")

    while True: #edits total received to date
        try:
            rece_ans= input("Would you like to edit the amount received to date (y/n): ")
            if rece_ans == "y":
                while True:
                    try:
                        recechange = int(input("What would you like to change it to?: "))
                        break
                    except:
                        print("The amount received to date should be a integer! Try again.")
                    
                del(myinventory[place+5])
                myinventory.insert((place+5), recechange)
                break
                    
            elif rece_ans == 'n':
                break

            else:
                print("Invalid option! Try again. \n")
        except:
            print("Invalid option! Try again. \n")

    if ((myinventory[place+3]) + (myinventory[place+4])) != (myinventory[place+5]):
        print("\n!!!!!!!!!!! \n WARNING: Quantity in Stock and Amount Sold to Date does not equal Total Received to Date. Please edit quantities for this product.")
        print("If this was done on purpose, ignore this message.\n !!!!!!!!!!")

    inventory_list()
    menu()
    

def search_list(): #main menu choice 6
    tosearch = input("Enter text to find in the inventory (case sensitive): ")
    for x in range (len(myinventory)):
        if tosearch in str(myinventory[x]):
            n = x-(x%6) 
            if myinventory[n] not in searchlist:
                searchlist.append(myinventory[n])

    if len(searchlist) == 0:
        print("No products found.")

    else:
        for y in range(len(searchlist)):
            print("\n Found in: ", searchlist[y])
            index = myinventory.index(searchlist[y])
            place = 0
                    
            for z in range(6):
                print(str(headings[pos]).ljust(30), end = "")
                place += 1
            print("")

            for v in range(6):
                print(str(myinventory[index]).ljust(30), end = "")
                index += 1
            print("")

        for r in range(len(searchlist)):
            del(searchlist[R])
        menu()
'''
def search_list():
    tosearch = input("Enter text to find in the inventory (case sensitive): ")
    for x in range(len(myinventory)):
        if tosearch in str(myinventory[x]):
            n = x - (x % 5) 
            if myinventory[n] not in searchlist: # adds the product to a new list so it can be printed later
                searchlist.append(myinventory[n])
    if len(searchlist) == 0:
        print("No items were found.")
    else: # all three for loops below work hand in hand to print the product being searched for and its description
        for y in range(len(searchlist)):
            print("\n Found in: ", searchlist[y])
            index = myinventory.index(searchlist[y])
            pos = 0
                    
            for z in range(5):
                print(str(headings[pos]).ljust(33), end = "")
                pos += 1
            print("")

            for v in range(5):
                print(str(myinventory[index]).ljust(33), end = "")
                index += 1
            print("")

        for r in range(len(searchlist)): # deletes so that it can re-used for the next search
            del(searchlist[0])
        menu()
'''
def receive_product(): #main menu choice 7
    while True:
        try:
            code = input("Enter the code of the product that has been received: ")
            if code in myinventory:
                break
            else:
                print("Error, item not found, try again.")
        except:
            print("Enter valid code!")

    n = myinventory.index(code)
    print("Product Selected: ", myinventory[n+1])
    received = int(input("Enter the quantity of the product received: "))

    quantity = myinventory[n+3]
    totalreceived = myinventory[n+5]
    
    newquantity = quantity + received
    newtotalreceived = totalreceived + received

    del(myinventory[n+3])
    myinventory.insert((n+3), newquantity)
    del(myinventory[n+5])
    myinventory.insert((n+5), newtotalreceived)

    inventory_list()

    menu()

def sale_product(): #main menu choice 8
    while True:
        try:
            code = input("Enter the code of the product that has been sold: ")
            if code in myinventory:
                break
            else:
                print("Item does not exist, try again.")
        except:
            print("Item does not exist, try again.")

    n = myinventory.index(code)
    print("\nProduct selected: ", myinventory[n+1])

    sold = int(input("\nEnter the amount of this product recently sold: "))
    totalsold = myinventory[n+4]
    quantity = myinventory[n+3]
    newtotalsold = totalsold + sold
    newquantity = quantity - sold

    del(myinventory[n+4])
    myinventory.insert((n+4), newtotalsold)
    del(myinventory[n+3])
    myinventory.insert((n+3), newquantity)

    inventory_list()
    menu()



def save_list():
    from time import sleep
    sleep(0.2)
    print("\nS", end ="")
    sleep(0.2)
    print("a", end ="")
    sleep(0.2)
    print("v", end ="")
    sleep(0.2)
    print("i", end ="")
    sleep(0.2)
    print("n", end ="")
    sleep(0.2)
    print("g", end ="")
    sleep(0.2)
    print(".", end ="")
    sleep(0.2)
    print(".", end ="")
    sleep(0.2)
    print(".")
    sleep(0.2)
    try:
        with open('Assignment 5 list.txt', 'w') as f:
            for item in myinventory:
                f.write("%s, " % item)
        print("\n[SAVE COMPLETE]")
        sleep(0.3)
        menu ()
    except:
        print("Save Error occured. Try again")
        menu()


def quit_program():
    try:
        with open('Assignment 5 list.txt', 'w') as f:
            for item in myinventory:
                f.write("%s, " % item)
        print("\nSAVE COMPLETE")
        print("\nThank you for using a product by NST™ lmt. Goodbye.")
        import os
        os._exit(0)
    except:
        print("Error occured, Try Again.")
        
    

def menu():
    while True:
        print(("\nMain Menu: \n"))
        print("1) List Current Inventory")
        print("2) List Product Detail")
        print("3) Add New Product")
        print("4) Remove product from inventory")
        print("5) Edit product") #make sure to finish the code for this
        print("6) Receive Product into Stock")
        print("7) Sale of Product")
        print("8) Search")
        print("9) Save Changes")
        print("10) Quit Program")
        print(" ")
        
        try:
            choice = int(input("Enter one of the options listed above: "))
            
            if choice == 1:
                inventory_list()
            elif choice == 2:
                list_details()
            elif choice == 3:
                add_list()
            elif choice == 4:
                remove_product()
            elif choice == 5:
                edit_product()
            elif choice == 6:
                receive_product()
            elif choice == 7:
                sale_product()
            elif choice == 8:
                search_list()
                break
            elif choice == 9:
                save_list()
            elif choice == 10:
                quit_program()
                break
            else:
                print("Invalid Option! Enter a number above. \n")
        except:
            print("Invalid Option! Try Again. \n")
    
#main
from time import sleep
sleep(0.2)
print("L", end ="")
sleep(0.2)
print("O", end ="")
sleep(0.2)
print("A", end ="")
sleep(0.2)
print("D", end ="")
sleep(0.2)
print("I", end ="")
sleep(0.2)
print("N", end ="")
sleep(0.2)
print("G", end ="")
sleep(0.2)
print(".", end ="")
sleep(0.2)
print(".", end ="")
sleep(0.2)
print(".\n")

print("    _   _____________")
print("   / | / / ___/_  __/")
print("  /  |/ /\__ \ / /   ")
print(" / /|  /___/ // /    ")
print("/_/ |_//____//_/     ʟᴍᴛ.")
print("                     ")
print("Inventory Tracker by NST™ lmt.\n")
print("Welcome, user.")
sleep(0.5)
menu()


