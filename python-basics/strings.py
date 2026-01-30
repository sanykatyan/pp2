#python string examples
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

  txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  txt = "The best things in life are free!"
print("expensive" not in txt)

#SLICING STRINGS
b = "Hello, World!"
print(b[-5:-2])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:5])

#MODIFY STRINGS
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#CONCATENATE STRINGS
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#FORMAT STRINGS
age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north."

#STRING METHODS
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


txt = "hello world!"
x = txt.islower()
print(x)


txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

