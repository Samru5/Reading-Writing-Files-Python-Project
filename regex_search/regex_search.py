# regex_search.py
"""The program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.
The results should be printed to the screen. """
import os
import re


# Method takes the user-supplied regular expression to be searched within all txt files & takes folder location where all txt files are present
def regexSearch(regexStr, folderPath):

    if not os.path.isdir(folderPath):
        return 'Provide a directory path'

    userRegex = re.compile(regexStr)

    # To check files within the given folder
    for filename in os.listdir(folderPath):

        # Check for the file names ending with txt extension
        if filename.endswith('.txt'):

            with open(filename) as file:

                for line in file:
                    data = userRegex.search(line)

                    if data:
                        print(line, end='')


# Main Method
if __name__ == "__main__":
    regex = input('Enter regex string to find inside the text files-: ')
    # Providing regex expression & path of current folder as arguments to the regexSearch method
    regexSearch(regex, '.')
