file = open("example.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 ==0:
        outfile += file.readline()
    else:
        file.readline()
    
file = open("example.txt", "w")
file.write(outfile)
file.close()