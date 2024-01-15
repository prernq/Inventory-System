#Name: Prerna Prabhu
#Date: 2019-12-09
#File Name: Prerna_Prabhu_Assignment_5
#Description:


# the inventory as a list where each index contains the info for that product
#make sure to change the quantities later!!!!
myinventory = ["AP001", "iPhone 7", 19, 1, 20, "AP002", "iPhone 8", 9, 8, 20, "AP003", "iPhone 8+", 11, 6, 30, "AP004", "iPhone XR", 7, 9, 30, "AP005", "iPhone XS", 12, 14, 30, "AP006", "iPhone 11", 8, 12, 30]
headings = ["Product No.", "Description", "Quantity", "Amount Sold", "Total Received"]
searchlist = []
'''
with open('myinventory list.py', 'r') as myinventory:
    data = file.readlines()

with open('myinventory list.p', 'w') as file:
    file.writelines(data)
'''

def inventory_list(): #(main menu #1)
    with open("Inventory.txt", 'r') as file:
        print(" ")
        for line in file:
            print(line.strip())
    print("\n----------------\n")
    menu()



def list_details(): #(main menu #2)
    while True:
        try:
            codetodetail = input("Enter the code of the product to list details of: ")
            n = myinventory.index(codetodetail)
            print(myinventory[n], "        Description: ", myinventory[n+1])
            break
        except:
            print("Enter a valid code!")
    menu()


def add_list():
    while True:
        code = input("Enter new code including the brand of the phone: ")
        if code in myinventory:
            print("Code already in use!")
        else:
            break           
    description = input("Enter the description for the product: ")
    quantity = int(input("Enter the quantity in stock: "))
    sold = int(input("Enter the amount of the product sold to date: "))
    received = int(input("Enter the amount received to date: "))
    newproduct = [code, description, quantity, sold, received]
    
    myinventory.append(code)
    myinventory.append(description)
    myinventory.append(quantity)
    myinventory.append(sold)
    myinventory.append(received)
    print("\n Product added to inventory.")
    
    file1 = open("Inventory.txt","a") 
    file1.write('\n')
    file1.write(code)
    file1.write("			")
    file1.write(description)
    file1.write("		")
    file1.write(str(quantity))
    file1.write("		")
    file1.write(str(sold))
    file1.write("		")
    file1.write(str(received))
    file1.close()
    
    inventory_list()




def remove_product():
    while True:
        code = input("Enter the code of the product that you would like to delete: ")
        if code in myinventory:
            break
        else:
            print("That item does not exist, try again!")
            
    place = myinventory.index(code)
    del(myinventory[place])
    del(myinventory[place])
    del(myinventory[place])
    del(myinventory[place])
    del(myinventory[place])
    print(myinventory)
    #DO IT TO THE TXT FILE
'''
def edit_product():
    code = input("Enter product code to edit: ")
    while True:
        if code in myinventory:
            break
        else:
            print("That item does not exist, try again!")
    codeanswer = input("Would you like to edit the code? (y/n): ")
    while True:
        try:
            if codeanswer == 'y':
                newcode = input("Enter new code: ")
                while True:
                    if newcode in myinventory:
                        print("Code already in use, try again!")
                    else:
                        break
                    
                n = myinventory.index(code)
                myinventory.insert(n, newcode)
                myinventory.remove(code)
            elif codeanswer == 'n':
                break
            else:
                print("That is not a valid input, try again.")

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



def receive_product():
    while True:
        code = input("Enter the code of the product that has been received: ")
        if code in myinventory:
            break
        else:
            print("Item does not exist, try again.")

    n = myinventory.index(code)
    print("Product Selected: ", myinventory[n+1])
    received = int(input("Enter the quantity of the product received: "))

    quantity = myinventory[n+2]
    totalreceived = myinventory[n+4]
    newquantity = quantity + received
    newtotalreceived = totalreceived + received

    del(myinventory[n+2])
    myinventory.insert((n+2), newquantity)
    del(myinventory[n+4])
    myinventory.insert((n+4), newtotalreceived)

    print(myinventory)

    menu()

def sale_product():
    while True:
        code = input("Enter the code of the product that has been sold: ")
        if code in myinventory:
            break
        else:
            print("Item does not exist, try again.")

    n = myinventory.index(code)
    print("Product selected: ", myinventory[n+1])

    sold = int(input("Enter the amount of this product recently sold: "))
    totalsold = myinventory[n+3]
    quantity = myinventory[n+2]
    newtotalsold = totalsold + sold
    newquantity = quantity - sold

    del(myinventory[n+3])
    myinventory.insert((n+3), newtotalsold)
    del(myinventory[n+2])
    myinventory.insert((n+2), newquantity)

    print(myinventory)

    menu()
    
    
'''
    print("Would you like to search by:")
    print("1) Product Code")
    print("2) Product Description")
    print("3) Quantity in stock")
    print("4) Quantity Sold to Date")
    print("5) Total Received to Date \n")
    searchby = int("Enter a search option:")


def sale_product():
    code = input("Enter the product code of the product that was sold:")
'''
def menu():
    print("Main Menu: \n")
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

    while True:
        
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
            elif choice == 9:
                save_list()
            elif choice == 10:
                quit_program()
            else:
                print("Invalid Option! Try Again.")
        except:
            print("Invalid Option! Try Again.")
    
#main
menu()

