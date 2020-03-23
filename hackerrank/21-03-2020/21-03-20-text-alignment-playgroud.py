c = '#'
thickness = 7

for i in range(thickness):
    print((i*c).rjust(thickness-1," ") + c + (i*c).ljust(thickness-1, " "))

for i in range(thickness+1):
    print((c * thickness).center(thickness*2," ") + (c * thickness).center(thickness*6," "))

for i in range((thickness+1)//2):
    print((c * thickness * 5).center(thickness * 6, " "))

for i in range(thickness+1):
    print((c * thickness).center(thickness*2," ") + (c * thickness).center(thickness*6," "))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness) * 5, " ")) + c + (c*(thickness-i-1)).ljust(thickness)," ")


