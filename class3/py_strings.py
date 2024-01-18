# Strings in python
# Strings are immutable

name = "Aabha"

description = """Lorem ipsum dolor sit amet, consectetur adipiscing e
    lit. Integer tincidunt rhoncus eros, eu pellentesque urna pulvinar rutrum.
    Quisque in arcu sed augue tincidunt pretium in id lectus.
    Donec sed massa porta, accumsan felis non, vehicula purus. 
    Proin sed lorem ac turpis posuere maximus quis ut orci. 
    Integer euismod lacus at nisi blandit, at vestibulum dolor pharetra.
    Maecenas facilisis nulla non magna molestie ullamcorper. 
    Vivamus auctor dolor mauris, in pellentesque neque fringilla non.
    Maecenas varius ultrices urna sed sagittis. Etiam iaculis tincidunt 
    quam id imperdiet. Nam mollis tellus eget enim bibendum, 
    id suscipit felis suscipit. Orci varius natoque penatibus et magnis
    dis parturient montes, nascetur ridiculus mus. Suspendisse purus metus,
    egestas ut dui eu, pretium vestibulum enim. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."""




# take fullname as input
full_name = input("Enter your full name: \n")
# Split your full name
full_name_split = full_name.split(" ")

# Printing your splitted name

print(f"FirstName Is {full_name_split[0]}")
print(f"MiddleName Is {full_name_split[1]}")
print(f"LastName Is {full_name_split[2]}")


print(full_name.replace("Jung","Kumar"))

name = "Surajan"
breakpoint()