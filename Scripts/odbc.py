f = open("C:\\temp\\morro\\morro.csv", "r")
contents = f.readlines()
f.close()

contents.insert(1, 'teste\n')

f = open("C:\\temp\\morro\\morro.csv", "w")
contents = "".join(contents)
f.write(contents)
f.close()
