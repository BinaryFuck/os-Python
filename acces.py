import os

print("The Os is", os.name)
print("The Os Name Is", os.uname())
print("The Current Working Directory Is", os.getcwd())
print("The List Of Directories In It are: ")
print(os.listdir())
print("Test If a Specific File Exits Or Not")
try:
    filename = 'abc.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
    print("Exits")
except IOError:
    print("Not Accesed or Problem In  reading " + filename)
