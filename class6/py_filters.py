# Used for filtering items in list to return a new list
"""
students = [
    {"name":"Ram","age":20},
    {"name":"Roshan", "age":21},
    {"name":"Shyam", "age":20},
    {"name":"Gita", "age":23},
    {"name":"Sita", "age":12},
]
fv = filter(lambda y : "R" in y["name"], students)
print(fv)
fv = list(fv)
print(fv)"""


# WAP To Take 10 students details  from terminal (name, age, religion)
# make a dictionary for every student and push all items to a list of students
# transform list of students dict to list of dict with names only
# filter list of students of age 20 


students = []

for i in range(10):
    students.append(
        {
            "name":input("Enter name: \n"),
            "age":int(input("Enter age: \n")),
            "religion":input("Enter religion : \n")
        }
    )

name_only_dict_list = list(map(lambda x : {"name":x["name"]}, students))

print("Mapped list of students are \n",name_only_dict_list)


age_20_students = list(filter(lambda x : x["age"] == 20,students))

print("Filtered list of students with age 20 are \n",age_20_students)