total = 0
menuPrices = [6, 10, 4]
menuList = ["1.Burger:", "2.Pizza:", "3.Hotdog:"]
foodSizes = ["Small:", "Medium:", "Large:"]
sizeAddOn = [0, 1, 3]  #oops gotta finish
sizeGet = 0
e = "$"
print("Generic Resturant Menu")


def printMenu():
  print("*******************************")
  for i in range(len(menuList)):  #iterates through the length of the list
    print(menuList[i], menuPrices[i])  #print each item in the lists
  for i in range(len(foodSizes)):
    print(foodSizes[i],
          str(sizeAddOn[i]) + f"{e}")  #print the sizes and the dollar amount
  print("*******************************")

def chooseFood():
  global choice
  choice = int(input())
  match choice:
    case 1:
      choice = 6
      print(f"{menuList[0]} {menuPrices[0]} ".strip() + e)

    case 2:
      choice = 10
      print(f"{menuList[1]}, {menuPrices[1]}".strip() + e)
    case 3:
      choice = 4
      print(f"{menuList[2]}, {menuPrices[2]}".strip() + e)
    case _:
      print("Not a valid item!")
      printMenu()
      chooseFood()
      print(" ")

def getTotal():  #calculates total
  global total
  print("*******************************")
  quantity = int(input("How many would you like?: "))
  tax = quantity/3
  tax = round(tax)
  subtotal = choice * quantity
  print(f"Your subtotal is {subtotal}")
  print(f"Tax: {tax}")
  total = choice * quantity + tax
  print(f"So your total is: {total}")

printMenu()
chooseFood()
getTotal()