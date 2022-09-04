def myFunc(LISTOFNUM, LISTOFFLOAT):
    AVERAGE = []  # for storing the average of even int
    SUM = 0
    MAXIMUMOFFLOAT = 0.0
    for i in LISTOFNUM:
        if type(i) == type(1):  # checking it is integer
            if i % 2 == 0:  # checking it is even integer
                AVERAGE.append(i)  # adding values to list
                SUM = SUM + i

                # for float numbers
    for i in LISTOFFLOAT:
        if type(i) == type(0.0):  # checking it is float
            if i > MAXIMUMOFFLOAT:  # if i greater than maximum
                MAXIMUMOFFLOAT = i  # i is maximum

    if len(AVERAGE) == 0 or SUM == 0 or MAXIMUMOFFLOAT != -1.0:
        return 0  # list doesn't contain neither int nor float

    return (SUM / len(AVERAGE), MAXIMUMOFFLOAT)


#def MyFunc():
 #   values=input("Enter list of numbers separated by space")
  #  numbers= values.split()
   # for i in numbers:
    #    if type(eval(i))== int:
     #       #if ((i %2 ==0))
      #      #aver=sum(i)/len(i)
       #     print ("Average of list element is ")
           #print(aver)
       # elif type(eval(i))== float :
        #    maximum=max(numbers)
         #   print("Maximum float is: ",maximum)
        #else:
         #   return 0 

# MyFunc()