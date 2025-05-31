
import csv

def write_phonebook():
    file = open("phonebook.csv","w")
    allno = []
    while True:
        y = []
        x = input("Enter contact nuber: ")
        if x.lower() == "stop":
            break
        else:
            y.append(x)
            allno.append(y)
    firs = csv.writer(file)
    firs.writerows(allno)
    
    print("Done")
    
    file.close()

write_phonebook()
