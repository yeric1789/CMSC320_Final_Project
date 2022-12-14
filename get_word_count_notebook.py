import os
import sys
import time
import json
from  nbformat import current as current_nb
import io
# Get the number of words in the markdown cells of a notebook
def get_word_count(notebook):
    # open the notebook in json format
    print("Opening notebook: " + notebook)
    with io.open(notebook, 'r', encoding='utf-8') as f:
        nb = current_nb.read(f, 'json')

    word_count = 0
    for cell in nb.worksheets[0].cells:
        if cell.cell_type == "markdown":
            word_count += len(cell['source'].replace('#', '').lstrip().split(' '))
    return word_count


if __name__ == '__main__':
    # get the notebook name from the command line
    notebook = sys.argv[1]
    # get the word count
    word_count = get_word_count(notebook)
    # print the word count
    print(word_count)