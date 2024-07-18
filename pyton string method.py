txt = "hello, and welcome to my world."

x = txt.capitalize()
print (x)

x = txt.casefold()
print(x)

x = txt.center(20)
print(x)

x = txt.count("e")
print(x)

x = txt.encode()
print(x)

x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

x = txt.find("e")
print(x)


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt1 = "For only {price:.2f} dollars!"
print(txt1.format_map({'price': 49}))


txt2 = "Hello, welcome to my world."
x = txt2.index("welcome")
print(x)


txt3 = "Company12"
x = txt3.isalnum()
print(x)


txt4 = "CompanyX"
x = txt4.isalpha()
print(x)


txt5 = "Company123"
x = txt5.isascii()
print(x)

txt = "50800"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "hello world!"
x = txt.islower()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())


txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) # True


txt = "   "
x = txt.isspace()
print(x) # True


txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) # True


txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # True


myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) # John#Peter#Vicky


left_justified = text.ljust(25, '-')
print("Left Justified:", left_justified)


lowercase_text = text.lower()
print("Lowercase:", lowercase_text)


stripped_text = text.lstrip()
print("Left Stripped:", stripped_text)


translation_table = str.maketrans("aeiou", "12345")
translated_text = text.translate(translation_table)
print("Translated:", translated_text)


partitioned_text = text.partition(",")
print("Partitioned:", partitioned_text)


str = "this is string example....wow!!!"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))


str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

str1 = "this is string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.index(str2))

str = "this is string example....wow!!!"
print (str.rjust(50, '0'))

str = "this is string example....wow!!!"
print (str.rpartition('is'))

txt = "apple#banana#cherry#orange"
x = txt.rsplit("#", 1)
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

text = "  Hello, World!  "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

text = "Hello, World!"
swapped_text = text.swapcase()
print(swapped_text)  # Output: "hELLO, wORLD!"

text = "hello, world!"
titled_text = text.title()
print(titled_text)  # Output: "Hello, World!"

table = str.maketrans("aeiou", "12345")
text = "hello, world!"
translated_text = text.translate(table)
print(translated_text)  # Output: "h2ll4, w4rld!"

text = "Hello, World!"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO, WORLD!"

text = "50"
filled_text = text.zfill(5)
print(filled_text)  # Output: "00050"
