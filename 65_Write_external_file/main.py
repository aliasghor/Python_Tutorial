# Using the write mode
print(20 * "=" + " Using the write mode " + 20 * "=")

with open("data.txt",'w') as write_file:
    write_file.write("Ali Ganteng\n")

with open("data.txt",'r') as read_file:
    print(read_file.read())

# Using the append mode

print("\n" + 20 * "=" + " Using the append mode " + 20 * "=")

with open("data.txt",'a') as append_file:
    append_file.write("Mogi")

with open("data.txt",'r') as read_file:
    print(read_file.read())