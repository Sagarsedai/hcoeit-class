
"""
user = {
    "name":"Surajan",
    "age":"18",
    "address":"New Jersey",
    "country":"Space ",
}
print("Full Name Is",user.get("full_name", "No Name"))


# getting keys of dict

print(user.keys())

# getting values of dict

print(user.values())


# setting new key to dict
user.setdefault("father_name", "alien")
user["goal"] = "Greatest Of All"

# getting values of a dict

user.get("name") #=> can return None if key absent

user.get("mother_name", "default value if no key present")
"""

"""
WAP to get name, age, religion, father_name, mother_name, college_name,  
as inputs from terminal .
Declare an empty dict Add these key value pairs to a dictionary 
and print result

"""
"""attrs = ["name", "age", "religion", "father_name", "mother_name", "college_name"]

user_detail = {}

for i in attrs:
    # user_detail.setdefault(i , input(f"Enter your {i} \n")) 
    # Magic Methods
    user_detail.__setitem__(i , input(f"Enter your {i} \n"))

print(user_detail)

for i in user_detail:
    print(i)

print(
[i for i in user_detail])

breakpoint()


{
    "name":"ava",
    "address":{
        "aparment":"Green Hill",
        "lat":"10.1111",
        "lon":"90.6466",
    }
}

"""

user_detail_first = {
    "name":"Surajan",
    "age":"18",
}

user_detail_second = {
    "address":"New Jersey",
    "country":"Space ",
}

# merging two dict
user_detail = {
    **user_detail_first, 
    **user_detail_second,
    "state":"bagmati"
}
# print(user_detail)

# merging two or more lists

student1 = ["SUrajan", "Oscar","Rajan"]
student2 = ["Ava", "Aashma","Supriya"]

student = [*student1,*student2,"123"]

print(student)