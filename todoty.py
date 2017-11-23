# Read over the lines of a file and list out the lines containing TODO:

# Regular expressions module
import re
import sys

# Compile matching object
todo = re.compile( "TODO", re.IGNORECASE )
eol = re.compile( '\n' )

# Testing string
string = "Okay this is an example of a few lines of text in a string.\nTodo: this is the line we want \n not this line"

### Test Matching ###
# Search the string for TODO
match = todo.search( string )
# Start a new string from the beginning of Todo
remainder = string[ match.end(): ]
# Search the remainder of the string
end_of_line = eol.search( string[ match.end(): ])
# If neither is null then we print 
if match is not None and end_of_line is not None:
    print( match.group() + remainder[ : end_of_line.start() ] )
### Test Matching ###


### Custom exceptions ###
class ArgumentCountError( Exception ):
    pass


### Read in the file from the command line argument 
def read_in_file( ):
    # How many arguments
    if( len( sys.argv ) != 2 ):
        raise ArgumentCountError( "Wrong number of arguments. Todoty takes in one file as an argument. Try -h or --help for more information" )
    # Read in from the file passed
    file_string = open( sys.argv[1], "r" ).read()
    return file_string



if __name__=="__main__":
    todoty = read_in_file( )
    print( todoty )
