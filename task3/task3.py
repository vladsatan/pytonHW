import math

# 1

def calculateCircleArea(r):
    
    area = math.pi * r**2
    return round(area)

radius = float(input("Введіть радіус кола: "))

circle_area = calculateCircleArea(radius)
print("Площа кола з радіусом", radius, "дорівнює", circle_area)

# 2

def format_number(n):
    
    num_str = str(n)
    
    nn = num_str * 2
    nnn = num_str * 3
    
    result = int(num_str) + int(nn) + int(nnn)
    
    return result

number = 5
print(format_number(number))  

# 3

def get_sum(arr):

    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

    return sum

array = [1,2,3,4]
get_sums = get_sum(array)
print("Сума чисел зі списку:",get_sums)

# 4

def get_multiplication(arr):
    
    sum = 1

    for i in range(len(arr)):
        sum *= arr[i]

    return sum

array = [2,2,2,4]
get_multiplications = get_multiplication(array)
print("Добуток чисел зі списку:",get_multiplications)

# 5

def get_min_value(array):

    min = array[0];

    for i in range(len(array)):
        print(array[i])
        if array[i] < min:
            min = array[i]

    return min

array2 = [10,5,23,8]
get_min_values = get_min_value(array2)
print("Найменьше число у списку -",get_min_values)