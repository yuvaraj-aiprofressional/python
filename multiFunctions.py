class multiFunctions():
    def Subfields():
        subFields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for items in subFields:
            print(items)

    def OddEven():
          inputValue = int(input("Enter a number: "))
          if((inputValue%2) == 0):
              print(inputValue," is Even number")
          else:
              print(inputValue," is Odd number")

    def Elegible():
        gender, age = input("Enter Your Gender: "), int(input("Enter Your Age: "))
        print("Your Gender : ",gender)
        print("Your Age : ",age)
        if((gender == 'Male' and age > 21) or (gender == 'Female' and age > 18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        Subject1, Subject2, Subject3, Subject4, Subject5 = int(input("Enter Your Subject1 Mark: ")), int(input("Enter Your Subject2 Mark: ")), int(input("Enter Your Subject3 Mark: ")), int(input("Enter Your Subject4 Mark: ")), int(input("Enter Your Subject5 Mark: "))
        print("Subject1 : ",Subject1)
        print("Subject2 : ",Subject2)
        print("Subject3 : ",Subject3)
        print("Subject4 : ",Subject4)
        print("Subject5 : ",Subject5)
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : ",total)
        print("Percentage : ",(total/5))

    def triangle():
        Height, area_Breadth, Height1, Height2, perimeter_Breadth = int(input("Enter Area Height Value : ")), int(input("Enter Area  Breadth Value : ")), int(input("Enter Perimeter Height1 Value: ")), int(input("Enter Perimeter Height2 Value: ")), int(input("Enter Perimeter Breadth Value: "))     
        print("Height : ",Height)
        print("Breadth : ",area_Breadth)
        print("Area of Triangle : ",((Height*area_Breadth)/2))
        print("Height1 : ",Height1)
        print("Subject4 : ",Height2)
        print("Height2 : ",perimeter_Breadth)
        print("Perimeter of Triangle : ",  (Height1+Height2+perimeter_Breadth))   

                  
            