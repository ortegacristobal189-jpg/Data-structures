planets=["Mercury", "Venus", "Earth", "Murs", "Jupiter", "Saturn", "Uranus", "Neptune"] 
gravity =[3.7,8.8,9.8,3.7,24.7,10.4,8.6,11.1]
 # print(type(gravity)) #CLASS LIST
print(planets)
print(len(planets))

i = 0
print("-"*30)
print(f"|{"planet name":<15} |{"gravity":<9} |")
print("-"*39)
while i < len(planets):
    print(f"| {planets[i]:<15} | {gravity[i]:<9} |")
    print("-"*39)
    print(planets[i],"",gravity[i])
    i += 1
