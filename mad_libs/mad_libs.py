# mad_libs.py
""" reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. """
import os
import re

"""Method is to take input file & checks the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file 
& replaces them with user provided input & write in output text file"""
def madLibs(input_file, output_file):
    # checks for NOUN,ADJECTIVE,ADVERB,VERB words in input file
    regex = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB)')

    # Opens input file in read mode & output file in write mode
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        content = in_file.read()

        matches = regex.findall(content)

        for found in matches:
            sub = input('Enter a ' + found + ': ')

            # Replaces the match words with user given data
            content = content.replace(found, sub, 1)

        # writes the updated data in output file
        out_file.write(content)
        print(content)


if __name__ == "__main__":
    madLibs('input.txt', 'output.txt')
