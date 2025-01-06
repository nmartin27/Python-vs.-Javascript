# ## Get Name
# user_input = input("what is your name?")
# print(user_input + "!!!")

# ## Reverse it
# strings = ["a man", "a plan", "a canal", "Frenemies!"]
# for string in strings:
#     print(string)

# def reverse_it():
#     string = ["a man", "a plan", "a canal", "Frenemies!"]

#     reverse = ''

#     # Loop through the string and reverse it
#     for i in range(len(string)):
#         reverse += string[len(string) - (i + 1)]

#     print(reverse)  # Equivalent to alert in Python

# # Call the function
# reverse_it()

# ## Swap em
# # def swap_em():
# #     a = 10
# #     b = 30
# #     temp = None
# #     temp = b
# #     b = a
# #     a = temp
# # print("a is now {b}, and b is now {a}")

# # swap_em()

# def swap_em():
#     a = 10
#     b = 30
#     temp = None  # Initialize temp variable

#     # Swap the values
#     temp = b
#     b = a
#     a = temp

#     # Print the result
#     print(f"a is now {a}, and b is now {b}")

# # Call the function
# swap_em()

## Multiply Array/list

def multiply_array(ary):
    if len(ary) == 0:  # PY uses len(ary) instead of array.length
        return 1
    total = 1    
    for i in range(len(ary)): #Loop through
        total = total * ary[i]

    return total
# print(total)

## Fizz Buzzer
# x=15

def fizzbuzzer(x):
    if x % (3 * 5) == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("buzz")
    else: 
        print('archer')

result = fizzbuzzer(15)
print(result)

##Nth Fibonacci

def nth_Fibonacci():
    fibs = [1, 1]
    num = int(input("Which Fibonacci number you want? ")) ## int() == parseInt() change to integer

    while len(fibs) < num:
        # length = len(fibs)
        next_fib = fibs[-2] + fibs[- 1]
        fibs.append(next_fib) ## variable.append == variable.push

    print(f"{fibs[-1]} is the Fib number at position {num}")

nth_Fibonacci()

##Search Array/List
def search_array(array, value):
    for i in range(len(array) - 1):
        if array[i] == value:
            return True
            break
        return -1 

##Palindrome
def is_Palindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[len(str)- i - 1]:
            return False
    return True

##Has Dupes