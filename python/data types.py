print("hello. welcome to data structures class !!!")
number1 = 10
print(f"ver number1 is: {type(number1)}")
gravity = 9.8
print(f"ver gravity is: {type(gravity)}")
numberx = 8j
print(f"ver numberx is: {type(numberx)}")

#string data types
my_name = "ortega"
fullname = "peter McDonald"
description = '''
hello, how's it going?
this is amazing !!!
'''
print(f"var my_name is: {type(my_name)}")
print(f"var fullname is: {type(fullname)}")
print(f"var desciption is: {type(description)}")
#lists
personal_info = [
    "Cristobal",
    "Ortega",
    20,
    True,
    "3005910463",
    "pasto",
    ["juli",9]
    ]
print(personal_info)
# show father ege and city
print(f"father age: {personal_info[2]}")
print(type(personal_info))
print("father city: ", personal_info[5])
# show daugther name and age
print(f"daugther name: {personal_info[6][0]}")
print(f"daugther age: {personal_info[6][1]}")
#update father age
new_age = input("please, type the new father age: ")
personal_info[2] = new_age
print(f"new father age is: {personal_info[2]}")
# add new imformation
personal_info.append("malala")
print(personal_info)

# tuple
user_data = ("benazir", "butto")
print(user_data)
print(user_data[0])
new_age = 40
user_data[2] = new_age
