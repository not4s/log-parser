#!/usr/bin/env python3
import re, sys

def parser(filepath):
    # Given file is a text file
    if filepath.split('.')[-1] == 'txt':
        # Open up the target file and read the text as whole
        with open(filepath, 'r') as file:
            text = file.read()
        split_text = re.split('-+\n', text) # Split the text into blocks
        
        # Create new file with the given block
        for block in split_text:
            block_name = block.split('\n')[0]
            with open(f'{block_name}.txt', 'w') as new_file:
                new_file.write(block)

def main():
    parser(sys.argv[1])

if __name__ == '__main__':
    main()
