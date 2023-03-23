#import inflect module
import inflect
#define p
p = inflect.engine()

#make empty list named "names"
names = []

#make loop with try-except which will ask user for name and append it to names list
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break
