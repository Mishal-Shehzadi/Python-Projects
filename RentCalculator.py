
rent = input ("Enter your hostel/flat rent =")
food = input ("Enter the amount of food ordered =")
electricity = int (input("Enter the total of electricity ="))
chargePerUnit = int (input("Enter the charge per unit ="))
person = int (input("Enter the people living in a room = "))

totalBill = electricity * chargePerUnit

output = (food + rent + totalBill) // person
print ("Each person will pay = ", output)