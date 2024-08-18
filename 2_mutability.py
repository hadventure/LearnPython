filenames = ["1. Raw Data.txt", "2. Reports", "3. Presentations"]
filenames1 = ("1. Raw Data.txt", "2. Reports", "3. Presentations")

for filename in filenames:
    filename = filename.replace(".", '-', 1)
    print(filename)
    filename

print(filenames)
