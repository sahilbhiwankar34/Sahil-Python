source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    if not line.strip().startswith("#"):
        f2.write(line)

f1.close()
f2.close()

print("\nSource File Content:")
f = open(source, "r")
print(f.read())
f.close()

print("\nDestination File Content:")
f = open(destination, "r")
print(f.read())
f.close()
