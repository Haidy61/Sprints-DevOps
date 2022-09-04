def MyFunc():
    values=input("Enter list of numbers separated by space")
    numbers= values.split()
    for i in numbers:
        if type(eval(i))== int:
            #if ((i %2 ==0))
            #aver=sum(i)/len(i)
            print ("Average of list element is ")
            #print(aver)
        elif type(eval(i))== float :
            maximum=max(numbers)
            print("Maximum float is: ",maximum)
        else:
            return 0 

MyFunc()