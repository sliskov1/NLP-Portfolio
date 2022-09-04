import sys  # to get the system parameter
import os   # used by method 1
import csv
import re
import pickle


text_in = []

class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone
    def display(self):
        print('\nEmployee list:')
        print('\nEmployee id: ', self.id)
        print(self.first, self.mi, self.last)
        print(self.phone)

def inputfile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r+') as f:  
        f.readline()
        csvReader = csv.reader(f, delimiter=',')
        regexPhone= r'\w{3}-\w{3}-\w{4}'
        regexID = r'\w{2}\w{4}'
        count = 0
        for row in csvReader:
            row[0] = row[0].capitalize()            # last name
            row[1] = row[1].capitalize()            # first name
            row[2] = row[2].upper()                 # middle initial 
            if row[2] == '':
                row[2] = row[2].replace('', 'X')
            id = row[3]
            if re.search(regexID, id):  # id
                True
            else:
                id = input("Enter the correct ID: ")   
                row[3] = id                    
            row[4] = re.sub(r'\D', '-', row[4]) # phone number
            phone = row[4]
            if re.search(regexPhone, phone):
                True
            else:
                phone = input('Enter a valid number: ')
                row[4] = phone
            last = row[0]
            first = row[1]
            mi = row[2]
            id = row[3]
            phone = row[4]
            p = Person(last, first, mi, id, phone)
            dict = {id: p.display()}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        inputfile(fp)
