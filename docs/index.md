Nathaniel Smith  
June 1, 2020  
Foundations of Programming: Python (IT FDN 100 A Sp 20)  
Assignment07  


# Python: Pickling Data and Exception Handling
## Introduction
In this paper I will explain how to pickle (and unpickle) objects and how to handle exceptions in Python.  
## What is pickle?
pickle is a Python module. As such, it must be imported with the import statement, see Figure 1.
```
import pickle
```
#### *Figure 1. Importing the pickle Module*
pickle is used to serialize or de-serialize Python objects. Some objects that can be serialized with the pickle module include, but are not limited to, None, True, False, integers, floats, strings, tuples, lists, and dictionaries. “pickling” is the conversion of objects into byte streams and “unpickling” is the conversion of byte streams into objects according to the official Python documentation (https://docs.python.org/3/library/pickle.html) (external site).
## Why pickle?
The pickle module is very useful, and efficient, at writing objects into binary files and reading objects from binary files. For example, it can be used to save a user’s updated profile to a database, or to save the state of a program at close so that the program can continue from the stop point after restarting.
## How Do You Pickle?
It’s easy to pickle, especially if you are familiar with reading and writing strings to plain text files. First, you need to open an object file with the open() function, but you have to open the object file with access mode ‘wb’. The b stands for binary. See the example in Figure 2.
```
pickling = open("debuts.dat", "wb")
```
#### *Figure 2. Open an Object File with Mode 'wb'*
Next, you write a Python object to the binary file using the pickle.dump() function. This step is the serialization process. In my example, I assigned a list of dictionary elements to the variable debutAlbums. The list object is then written to the binary object file pickling. See the example in Figure 3.
```
pickle.dump(debutAlbums,  pickling)
```
#### *Figure 3. pickle.dump() Function*
Finally, you close the file with the .close() function. The above steps are shown together in Figure 4.
```
import pickle

debutAlbums = [{'band': 'Led Zeppelin', 'debut': 'Led Zeppelin'},  # create a list object
               {'band': 'U2', 'debut': 'Boy'}]

# pickling an object
pickling = open("debuts.dat", "wb")  # open a binary file for writing
pickle.dump(debutAlbums, pickling)  # serialization i.e. pickling
print(type(pickling))
pickling.close()  # close the file
```
#### *Figure 4. Pickling an Object*
Running the code in Figure 4 results in the object type printing to screen (because of the print statement, which I did not mention earlier) and writing the object debutAlbums to the debuts.dat file. The class type of pickling is _io.BufferedWriter. The debuts.dat file is shown in Figure 5.  

![Figure 5](./images/figure5.png "debuts.dat binary file")
#### *Figure 5. debuts.dat Binary File*
The debuts.dat binary file is not human readable. I can pick out a few words, but most of the characters make sense to me. This is how binary files are stored. It is completely readable by the computer. Do not confuse this with the file being encrypted. Because anyone can unpickle the contents of the file to read it. And that is what I explain next.
## How do you Unpickle?
Unpickling is just as easy as pickling. First, the pickle module is imported. Second, a binary object file is opened with the open() function, but this time with access mode ‘rb’. Finally, the pickle.load() function is used to unpickle the file into a variable i.e. de-serialize the data in the file into an object. This code is shown in Figure 6.
```
import pickle

# unpickling an object
unpickling = open("debuts.dat", "rb")  # open binary file for reading
debutAlbumsUP = pickle.load(unpickling)  # de-serialization i.e. unpickling
unpickling.close()  # close the file
```
#### *Figure 6. Unpickling an Object*
To see what is stored in debutAlbumsUP I use the print() function. I also use a print function to check that the data type is list which is what I am expecting because I initially started with a list of dictionary elements, debutAlbums, that was pickled and then unpickled.
```
print(debutAlbumsUP)  # print to check that it worked
print(type(debutAlbumsUP))  # check the data type
```
#### *Figure 7. Print() Functions*
The print statements of Figure 7 printed the text shown in Figure 8. Indeed, the original list was printed to screen and debutAlbumsUP is type list.
![Figure 8](./images/figure8.png "Result of print() Function")
#### *Figure 8. Result of print() Function in Figure 7*
## Additional Resources on Pickle
Here is a list of additional resources that discuss pickling and unpickling:  
•	https://www.youtube.com/watch?v=2Tw39kZIbhs (external site) – great introduction to pickle  
•	https://docs.python.org/3/library/pickle.html (external site) – all the ins and outs of pickle  
•	https://www.geeksforgeeks.org/understanding-python-pickling-example/ (external site) – provides a nice example of pickling without a file  
## Exception Handling
Exception handling is a way to handle errors that arise during the execution of code. Errors can result because of bad user inputs, or missing files, or bad programming. There are many reasons that an error might occur. If an error occurs in a script that does not have exception handling, the script will exit with an error and print the error to the screen that is not usually understood by the user. Exception handling is a way to capture these errors, provide useful messages to the user, and allow the program to continue running. In Python, we use the try statement to handle exceptions.
## Try Statement
A try statement consists of a try clause and an except clause. And there can be multiple except clauses. The try clause begins with the keyword “try” followed by a colon, followed by an indented block of code. It is in this indented block that you place code to be “checked” for errors. The code in the block will try to run. If there are no exceptions the code will execute as intended. If an error is encountered the script will jump to the except clause.










## Summary
