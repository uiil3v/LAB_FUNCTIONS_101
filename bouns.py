
def pattern_string(userNum: int):
    result = ""
    for num in range(userNum, 0, -1):
        for num2 in range(num, 0, -1):
            result += str(num2) + " "
        result += "\n"
    return result

number = int(input("Enter a number: "))
print(pattern_string(number))
print(type(pattern_string(number)))

