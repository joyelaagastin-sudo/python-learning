# pcb = int(input("Enter the PCB percentage: "))
# pcm = int(input("Enter the PCM percentage: "))

# if pcb == 100:
#     college = "Your ward has been selected in the Medical College."
# elif pcm == 100:
#     college = "Your ward has been selected in the Engineering College."
# else:
#     college = "Your ward has been selected in the Arts College."

# print(college)

# for loop

# for i in range(1, 11):
#     print(i)           


# 
# total = 0
# for i in range(1, 6):
#     subject_mark = int(input("Enter the marks for subject : "))
#     total += subject_mark
# print("Total marks:", total)

# row = 3
# column = 4
# for i in range(row):
#     for j in range(column):
#         print("*", end=" ")
#     print()

# rows = 4

# for i in range( rows + 2):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# rows = 4
# columns = 1
# for i in range(rows + 1):
#     for j in range(, columns + i):
#         print("*", end=" ")
#     print()


# while loop

# energy = 10
# while energy > 0:
#     print("jumping")
#     print(f"Energy: {energy}")
#     energy -= 1
#     print("loop ended")
    
    
# from unittest import case

# status_code = int(input("Enter the status code: "))
# match status_code:
#     case 400:
#         print("Bad Request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not Found")
#     case _:
#             print("status code not recognized")


# a=6
# b=5
# if a > b :
#     print("a is greater than b")
# else:
#     print("b is greater than a")
    
      

# a = 34
# b = 8
# c = 1
# if a > b:
#     print("a is greater than b")
# elif b > c:
#     print("b is greater than c")
# else:
#     print("c is the greatest")




a = int(input("enter the a value : "))
b = int(input("enter the b value : "))
c = int(input("enter the c value : "))

if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
else:
    print("c is the greatest")