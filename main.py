total = 0
menuList = ["1.Burger:", "2.Pizza:", "3.Hotdog:"]  # 0-2
menuPrices = [6, 10, 4]
foodSizes = ["Small:", "Medium:", "Large:"]
sizeAddOn = [0, 1, 3]  #oops gotta finish
sizeGet = 0
choice = 0
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


def chooseFood(choice):
  while choice not in range(1, 4):  #need to fix loop D:
    printMenu()
    choice = int(input("What would you like: "))
    print(menuList[choice - 1], end="")  #prints our option
    print(
        str(menuPrices[choice - 1]) + f"{e}")
  return choice


def getTotal():  #calculates total
  global total
  tax = 1.75
  print("*******************************")
  quantity = int(input("How many would you like?: "))
  subtotal = menuPrices[choice - 1] * quantity
  print(f"Your subtotal is {subtotal}")
  print(tax)
  total = menuPrices[choice - 1] * quantity + tax
  print(f"So your total is: {total}")


choice = chooseFood(choice)
getTotal()
