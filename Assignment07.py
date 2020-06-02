# ------------------------------------------------- #
# Title: Assignment 07
# Description: Example script to show how to use
#               pickle module and to show how to
#               handle exceptions with try-except.
# ChangeLog: (Who, When, What)
# NSMITH,05/27/2020,Created Script
# NSMITH,05/31/2020,Added Pickling code
# NSMITH,05/31/2020,Added Unpickling code
# NSMITH,05/31/2020,Added try statement example
# ------------------------------------------------- #

import pickle

debutAlbums = [{'band': 'Led Zeppelin', 'debut': 'Led Zeppelin'},  # create a list object
               {'band': 'U2', 'debut': 'Boy'}]

# pickling an object
pickling = open("debuts.dat", "wb")  # open a binary file for writing
pickle.dump(debutAlbums, pickling)  # serialization i.e. pickling
# print(type(pickling))
pickling.close()  # close the file

# unpickling an object
unpickling = open("debuts.dat", "rb")  # open binary file for reading
debutAlbumsUP = pickle.load(unpickling)  # de-serialization i.e. unpickling
unpickling.close()  # close the file

print(debutAlbumsUP)  # print to check that it worked
print(type(debutAlbumsUP))  # check the data type

try:
    strData= input("Give me a number: ")
    # strData = (1 + strData) # uncomment this line for TypeError
    # intData = int(strData) # uncomment this line for ValueError
    if not strData.isnumeric():  # was non-number entered?
        raise ValueError('Give me a number, please.')  # raise ValueError
    # quot = int(strData)/0 # uncomment this line for ZeroDivisionError
except TypeError as e:
    print("You done messed up kid!")
    print("You know you can't add numbers to strings!")
    print(f'Or as Python would say..."{e}"')
except ZeroDivisionError as e:
    print("Don't worry, it's not you it's me.")
    print("I guess I should write better code.")
    print(f'Python had this to say about it, "{e}"')
except ValueError as e:
    print("Why you messing with me?")
    print(f"I asked for a number and you give me '{strData}'?!")
    print(f'This is what Python thinks about it: "{e}"')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(f'Python had this to say about it, "{e}"')
    #print(e,e.__doc__,type(e),e.__str__(),sep='\n')  # too verbose
else:
    print('We had no errors!')
finally:
    print('Errors or not, this will execute.')