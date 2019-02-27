# 4.13.3: Greeting
# Keegan Killian
# 2.6.19



name = input("What is your name?: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()



# 4.13.4: Functions and Variables
# Keegan Killian
# 2.14.19



x = 2202

def print_something():
    x = 22
    print(x)

print_something()
print(x)



# 4.13.5: Functions and Variables - part 2
# Keegan Killian
# 2.14.19

my_variable = 3.14

def something():
    print(my_variable + 10)

something()



# 4.13.6: Functions and Variables, part 3
# Keegan Killian
# 2.18.19



def print_number(x):
    print(str(x))

print_number(15)
print_number('\n' + 'Hello World')


# 4.14.4: Name and Age
# Keegan Killian
# 2.18.19

def name_and_age(name, age):
    print('\n' 'Hi, my name is',name, 'and I am',str(age), 'years old.')

name_and_age('Keegan', 15)
name_and_age('paul', 18)
name_and_age('bill', 76)


