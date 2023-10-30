# integer division
x = 37
remainder = x % 2
print(remainder)

# commenting and string manipulation
'''
comment example for multiple lines
'''
my_string = """Hello, it's me."

'He said "You are amazing!" yesterday."""
print(my_string)

age = 34
age_as_str = str(age)

print("Youa are " + age_as_str)

# string formatting
name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

name = "Bob"
print(greeting)

final_greeting = "How are you, {}?"
greetings = "How are you, {name}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

greeting = greetings.format(name="Leo")
print(greeting)

greeting = greetings.format(name=name)
print(greeting)

# user inputs
age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")

# Booleans and comparisons
age = 20
is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print((f"You got it right: {matches}."))

#age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}.")

usually_not_working = age > 18 or age <= 65
print(f"At {age}, you are usually working: {usually_not_working}.")

print(bool(0))
print(bool(""))

# python always looks left and 'THEN' right.
# below shows True first then False, meaning the result will always be 'False' with the 'AND' operator.
# However, the 'OR' operator will check the first value and if True, then it will end the parsing at the first "TRUE" value.
x = True and False
print(x)

print(not True) # will print False
print(not False) # will print True


# Lists in python
friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne" # this type of variable is unsustainable.

friends = ["Rolf", "Bob", "Anne"] # keep the variable type the same within the list too reduce confusion.
print(friends[0])
print(len(friends))

# lists within a list
friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][1])
print(friends[0][0])

friends = [
        ["Rolf", 24], 
        ["Bob", 30], 
        ["Anne", 27]
]

friends.append(["Leo", 32])
print(len(friends))

friends.remove(["Bob", 30])
print(len(friends))

# Tuples
short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "BoB")
tuple_in_list = ["Rolf", "Bob"] # this creates 2 elements instead of tuple inside the list
tuple_in_list = [("Rof", "Bob"), "Lisa"]
print(x for x in tuple_in_list)

# adding to a tuple?
friends = ("Rolf", "Bob", "Anne")
# cannot execute 'friends.append("Jane")' as it will cause compile error

# correct way to add to tuple
friends = friends + ("Jen",)
print(friends)
