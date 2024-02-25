import math;

# 1

n = 0;
while n < 10:
    print(n);
    n += 1;

# 2

print("Enter a number from 1 to 10:")
choice = int(input());

sum = 0;

for x in range(choice):
    sum += x;

print("sum = " + str(sum))

# 3

print("List:")

arrayOfNumbers = [1,2,3,4,5,6,7,8,9,10];

for x in arrayOfNumbers:
    print(x);

# 4

print("factorial of which number from the list would you like to find?")

numFac = int(input());
factorial = 1;
for x in range(numFac):
    factorial *= x+1;

print("Facrorial of " + str(numFac) + " = " + str(factorial))

# 5

print("what number would you like to convert to binary?")

numCon = int(input());

def convertToBinary(n):
    array = [];
    k = 0;
    while n > 0:
        if n%2 == 0:
            k = 0;
            array.append(str(k))
        else:
            k = 1;
            array.append(str(k))
        n = math.trunc(n/2);
    
    array.reverse()
    result = ''.join(array)
    print(result)

convertToBinary(numCon)