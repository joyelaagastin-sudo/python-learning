# 1
# num = int(input("Enter a number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10
# print("sum=", sum)

# 2

# num =int(input("Enter N :"))
# sum = 0
# for i in range (1, num + 1):
#     sum = sum + i * i
# print("sum =", sum)


# 3

# sum = 0
# for i in range(10):
#     num = int(input("Enter a number: "))
#     sum = sum + num
#     average = sum / 10
# print("average =", average)

# 4

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# 5

# A = [4,5,2,77,6,8,11]
# max = A[0]
# for i in A:
#     if i > max:
#         max = i
# print("maximum =", max)


# 6


# letters =["a", "b", "c", "d"]
# for i in range (4):
#     print(letters[i] * (i + 1))

# 8

# petrol = 0

# while petrol <= 0:
#     petrol = float(input("Enter petrol in liters: "))

# distance = petrol * 50

# print("Distance =", distance, "km")


# 9

# for num in range(1,100000):
#     sum = 0
#     for i in str(num):
#         sum = sum + int(i)**3

#     if sum == num:
#         print(num, "is an Armstrong number")

# for i in range(1, 16):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)