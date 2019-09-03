#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from pentest.brute.dict import BruteDictionaryIter
from pentest.io         import Inputs


class Controller(object):


    def __init__(self):

        # Header message
        print('Dictionary Maker');

        # Input handler
        inputs = Inputs()

        # Options from user input
        data = {
            'max-length' : inputs.get('Enter max longitude of word [4]        : ', int, 4),
            'lowercase'  : inputs.get('Use letters lowercase?      [Y/n]      : ', bool, True),
            'uppercase'  : inputs.get('Use letters uppercase?      [y/N]      : ', bool, False),
            'numbers'    : inputs.get('Use numbers?                [Y/n]      : ', bool, True),
            'specials'   : inputs.get('Use specials chars?         [y/N]      : ', bool, False),
            'filename'   : None
        }

        while(True):

            # Get the filename of dictionary to make
            data['filename'] = inputs.get('Filename of dictionary      [dict.txt] : ', str, 'dict.txt')

            # File exist?
            if(not os.path.isfile(data['filename'])):
                break

            # Replace the file?
            if(inputs.get('The file exists. You want to replace it? [y/N] : ', bool, False)):

                # Delete old file
                os.remove(data['filename'])

                break

        # File dictionary pointer on memory
        fileHandler = open(data['filename'], 'w')

        # Make the iterator
        bruteDictionaryIter = BruteDictionaryIter(
            maxLength = data['max-length'],
            lowercase = data['lowercase'],
            uppercase = data['uppercase'],
            numbers   = data['numbers'],
            specials  = data['specials']
        )

        # Process the iteration
        for item in bruteDictionaryIter:

            # Write the word
            fileHandler.write(item + '\n')

            # Print the progress            
            print(''.join([
                '\r',
                'Progress: ',
                str(bruteDictionaryIter.currentWordIndex),
                '/',
                str(bruteDictionaryIter.totalWords),
                ' - ',
                item
            ]), end='', flush=True)

        fileHandler.close()

        print('\r                                                       \rEnd!')


if __name__ == '__main__':

    try:
        Controller()

    except KeyboardInterrupt as e:
        # Ctrl+C, it's ok.
        pass

    except Exception as e:
        # Unhandled exception
        raise e