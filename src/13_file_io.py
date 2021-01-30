"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("C:/Users/infin/Desktop/lambdaschool/Computer Science/Python/Intro-Python-I/src/foo.txt")
print(f.read())
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
new = open("C:/Users/infin/Desktop/lambdaschool/Computer Science/Python/Intro-Python-I/src/bar.txt", "w")
new.write("Lorem Ipsum is simply dummy text of the printing and type setting industry.\n")
new.write("Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
new.close()
new = open("C:/Users/infin/Desktop/lambdaschool/Computer Science/Python/Intro-Python-I/src/bar.txt")
print(new.read())