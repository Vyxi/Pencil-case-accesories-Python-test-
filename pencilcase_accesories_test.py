print ('How many pencil case items do you have?')

x = int(input("Pencils: "))
y = int(input("Pens: "))
w = int(input("Erasers: "))

def sum(a,b,c):
    return a + b +c

z = sum(x,y,w)
print(z, 'pencil case items.')
