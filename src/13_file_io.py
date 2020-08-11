"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

foo = open('./src/foo.txt', 'r')
fooRead = foo.read()
print(fooRead)
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open('./src/bar.txt', 'w')
bar.write('line one arbitrary\n')
bar.write('line 2 arbitrary\n')
bar.write('line 3 arbitrary')
bar.close()
with open('./src/bar.txt') as bar:
    print(bar.read())