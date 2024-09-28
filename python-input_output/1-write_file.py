#!/bin/usr/python3

def write_file(filename="", text=""):
    '''Use 'with' to open the file in write mode'''
    with open(filename, 'w', encoding='UTF-8') as file:
        '''
            Write the text to the file and
            return the number of characters written
        '''
        return file.write(text)
