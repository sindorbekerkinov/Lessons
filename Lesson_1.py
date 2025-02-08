txt = "hello, and welcome to my world."
print (txt.capitalize())
print(txt.casefold())
print(txt.count("and"))
print(txt.encode())
print(txt.endswith("."))
print(txt.find("and"))
print(txt.index("welcome"))
print(txt.istitle())
print( txt.isupper())
print(txt.lower())

txt = "apple"
print(txt.center(20))

txt = "For only {price:.1f} dollars!"
print(txt.format(price = 45))

text = "Company12"
print(text.isalnum())

txt = "CompanyX"
print(txt.isalpha())

txt = "1234"
print(txt.isdecimal())

myTuple = ("John", "Peter", "Vicky")
print(" and ".join(myTuple))

txt = "Apelsin"
print(txt.ljust(15), "is my favorite fruit.")
print("of all fruits", txt.lstrip(), "is my favorite")

txt = "Hello Sam!"
print(txt.translate(str.maketrans("S", "P")))

txt = "I could eat bananas all day"
print(txt.partition("bananas"))

txt = "I like bananas"
print(txt.replace("bananas", "apples"))
print(txt.rindex("like"))
print(txt.upper())
print(txt.title())
print(txt.swapcase())
print(txt.startswith("Hello"))
print(txt.splitlines())
print(txt.translate({8: 7}))
txt = "50"
print(txt.zfill(10))