import csv
from collections import defaultdict


def read_records():
    '''
        Program to read CSV file and converting it into 
        dictionary data structure to play with..

        Incase the format is invalid, then the code will raise the exception which is handled.
    '''

    phonebook = defaultdict(list)
    with open('phone_dataset.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                if len(row) == 3:
                    fname, lname = map(str.strip, row[0].split(" "))
                    phone, state = row[-2].strip(), row[-1].strip()
                elif len(row) == 4:
                    if row[2].replace(' ', '').isalpha():
                        lname, fname, state, phone = map(str.strip, row)
                    else:
                        fname, lname, phone, state = map(str.strip, row)
                else:
                    pass
                phonebook[lname.strip()].append([fname, state, phone])
            except ValueError:
                pass
    return phonebook


def sort_by_firstname(rec):

    return rec[0]
    
def export_phonebooks(phonebook):
    '''
        This program reads the queries.txt and search for any key if 
        it is present in phonebook
    '''

    file1 = open('query.txt', 'r') 
    Lines = file1.readlines() 
    output = open('output.txt','w')
    for line in Lines:
        key = line.strip()
        output.write('Matches for : '+key)
        output.write('\n')
        records = sorted(phonebook.get(key, []), key=sort_by_firstname)
        if not records:
            output.write('No Results Found')
            output.write('\n')
        else:
            for idx, val in enumerate(records, start=1):
                x = "Result {idx}: {lname}, {fname}, {state}, {phone} \n".format(idx=idx,
                                                                          lname=key,
                                                                          fname=val[0],
                                                                          state=val[1],
                                                                          phone=val[2])
                output.write(x)

    output.close()


if __name__ == '__main__':
    phonebook = read_records()
    export_phonebooks(phonebook)