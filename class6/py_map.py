
# Map means transform

students = [
    {"name":"Ram","age":5},
    {"name":"Roshan", "age":21}
]


mapped = map( lambda x :  {"age":x['age']} , students )

mapped = list(mapped)
breakpoint()    