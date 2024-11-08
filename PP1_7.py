2335

def q1(): 
  #Write code here
  bool1 = 5 < 10
  print(bool1)

def q2():
  #Write code here
  num1 = input("Input an integer: ")
  num2 = int(num1)
  bool2= (num2 > 5)
  print(bool2)

def q3():
  #Write code here
  num3 = input("Input the letter a:")
  num4 = int(num3)
  bool3 = (num4 == "a") 
  print(bool3)

def q4():
  #Write code here
  num5= input("Input a word earlier in the dictionary than google: ")
  bool4 = num5.lower() < "google"
  print(bool4)

def q5():
  #Write code here
  num7= input("Input an integer: ")
  num8= input("Input another integer: ")
  num9= int(num7)
  num10= int(num8)
  num11= num9 * num10
  bool5= num11 > 40
  print("Your numbers multiplied together are greater than 40: ", bool5)

#Do edit the code below
#Comment the lines below when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
