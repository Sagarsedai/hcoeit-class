"""
Mode	Description
r	Open a file in reading mode (default)
w	Open a file in writing mode
x	Open a file for exclusive creation 
a	Open a file in appending mode (adds content at the end of the file)
t	Open a file in text mode (default)
b	Open a file in binary mode
+	Open a file in both read and write mode
"""

# open a file in default mode (read and text)
# equivalent to open("test.txt", "rt")
"""
file1 = open("test.txt", "a")
# read the file content
# read_content = file1.read()
# file1.write("Milan Kandel")
file1.write("\n Arpan Gautam \n")
# print(read_content)
file1.close()
"""
"""
# open the file2.txt in write mode
file2 = open("file2.txt", "w")

# write contents to the file2.txt file
file2.write('Hello World\n')
"""
"""
with open("file1.txt", "a+") as file1:
    file1.writelines(
        [f"{i}\n" for i in range(5000)],
    )
    read_content = file1.read()
    print(read_content)
    file1.close()"""
"""

"""
students = []
for _ in range(5):
    students.append(
        {
            "name": input("Enter student name:\n"),
        }
    )
with open("student.txt", "w+") as sfile:
    sfile.writelines(
        [f"{i["name"]}\n" for i in students],
    )
    # read_content = sfile.read()
    # print(read_content)
    sfile.close()
