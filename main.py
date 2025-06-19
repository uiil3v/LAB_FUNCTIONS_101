
def pattern_int (userNum:int):
    for num in range(userNum , 0  , -1):
        for num2 in range(num, 0, -1):       
            print(num2, end=' ')             
        print()          


number = int(input("Enter a number: "))
pattern_int(number)


        


