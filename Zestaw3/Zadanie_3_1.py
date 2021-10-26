# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
#--------------------
# x = 2; y = 3;  <--| 
# if (x > y):       |
#    result = x; <--|---  Niepotrzebne średniki
# else:             |
#    result = y; <--|
#--------------------

# Poprawny kod:
x = 2
y = 3
if (x > y):
    result = x
else:
    result = y
print(result)

# for i in "qwerty": if ord(i) < 100: print (i)  <-- Niepoprawna struktura

# Poprawny kod:
for i in "qwerty": 
    if ord(i) < 100: 
        print(i)
        
# for i in "axby": print (ord(i) if ord(i) < 100 else i) <-- Niepoprawna struktura

# Poprawny kod:

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
