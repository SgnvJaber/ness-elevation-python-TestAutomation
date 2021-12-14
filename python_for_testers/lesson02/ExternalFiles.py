input_file= 'example.txt'
def write_to_file(file_name):
    file=open(file_name,"w")
    file.write("~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write("Hello world\n")
    file.write("This is an example file written by python.\n")
    file.write("~~~~~~~~~~~~~~~~~~~~~~\n")
    file.close()
def read_from_file(file_name):
    file=open(file_name,"r")
    print("The content of the file is:\n"+str(file.read()))
    file.close()
write_to_file(input_file)
read_from_file(input_file)