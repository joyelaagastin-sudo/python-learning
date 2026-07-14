# # 1
# secret = 7
# while True:
#     guess = int(input("enter the secret number :"))
#     if guess == secret:
#         print("congratulation you guessed it right")
#         break
#     else:
#         print("try agatin")


# 2
# count = 0
# even = 0
# odd = 0
# while count < 10 :
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     count += 1
# print("Even =",even)
# print("Odd =",odd)

# 3
# num = int(input("Enter a positive number: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print("Number of digits:", count)


# # 4

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# operation = input("Enter the operation (+, -, *, /): ")

# match operation:
#     case "+":
#         result = a + b
#         print("Result:", result)
#     case "-":
#         result = a - b
#         print("Result:", result)
#     case "*":
#         result = a * b
#         print("Result:", result)
#     case "/":
#         if b != 0:
#             result = a / b
#             print("Result:", result)
#         else:
#             print("Error: Division by zero")
#     case _:
#         print("Invalid operation")

