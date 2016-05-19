
# Jason Nghe 77653463 and Junjie Lin 25792830, Lab5, Pro.1
import os
import stat
import shutil
def main():
    '''The main function'''
    root_dir = valid_path_check()
    full_index = index_all(root_dir)
    choice = 1 # Initialze choice to 1, to begin the loop.
    while not choice == 0: # While the user hasnt pressed Exit
        print("\nMENU: \n" + 
              "1. Search By Name: \n" +
              "2. Search by Name Ending: \n" +
              "3. Search by Size: \n" +
              "4. Print Path: \n" +
              "5. Print First Line of Test: \n" +
              "6. Copy the File: \n" +
              "7. Touch the File: \n" +
              "0. Exit: \n")
        choice = valid_choice_number()
        while choice < 0 or choice > 7:
            print("Error: Try again: ")
            choice = valid_choice_number()
        if choice == 1:
            # Case 1: Search by Name.
            name = str(input("Enter the name you wish to search for: "))
            result = search_names(name, full_index)
            
            if len(result) == 0:
                print("There are no entries with the specified key, " + name)
            else:
                print("Results: ")
                for i in range(len(result)):
                    print(result[i])
        elif choice == 2:
            # Case 2: Search by Extension.
            ext = str(input("Enter the extension you wish to seach for: "))
            result = search_ext(ext, full_index)
            if len(result) == 0:
                print("There are no entries with the specified key, " + ext)
            else:
                print("Results: ")
                for i in range(len(result)):
                    print(result[i])
        elif choice == 3:
            # Case 3: By Size.
            size = int(input("Enter the size limit you want: "))
            result = search_size(size, full_index)
            if len(result) == 0:
                print("There are no entries with the specifed key, " + str(size))
            else:
                print("Results: ")
                for i in range(len(result)):
                    print(result[i])
        elif choice == 4:
            print_paths(root_dir)
        elif choice == 5:
            filename = str(input("Enter the filename you want to read: "))
            result = search_names(filename,full_index)
            if len(result) == 0:
                print("There are no entries with the specified key: " + filename)
            else:
                first_line(result[0])
        elif choice == 6:
            '''MAKE A COPY FUNCTION HERE'''
            filename = str(input("Enter the filename you want to copy: "))
            result = search_names(filename,full_index)
            if len(result) == 0:
                print("There are no entries with the specified key: " + filename)
            else:
                copy_file(result[0],result[0] + ".copy")
                print("File has been copied")
        elif choice == 7:
            filename = str(input("Enter the filename you want to touch: "))
            result = search_names(filename,full_index)
            if len(result) == 0:
                print("There are no entries with the specified key: " + filename)
            else:
                touch(result[0])
                print('File has been Touched')
        else: # choice == 0
            print("Goodbye.")
            
def valid_path_check():
    root_dir = input(str("Enter a directory name: "))
    while not os.path.exists(root_dir):
        print("Error: The path you have specified was not found.")
        root_dir = str(input("Enter a directory name: "))
    return root_dir

def valid_choice_number():
    try:
        choice = int(input("Enter a choice: "))
        return choice
    except ValueError:
        print("Error, the value you entered was not valid: ")
        choice = int(input("Enter a choice: "))
        return choice

def index_all(root_dir: str) -> list:
    '''Records all entries in the root directory and
    returns the results as a list.'''    
    full_index = [] # This is where we will store all of the entries in the directory
    apple = os.listdir(root_dir)
    for i in apple:
        orange=os.path.join(root_dir,i)
#        if not os.path.isfile(orange):
        if os.path.isdir(orange):
            full_index+= index_all(orange)
        else:
            full_index.append(orange)
    return full_index


def search_names(name: str, full_index: list) -> list:
    '''Searches the index list by name'''
    result = []
    for i in range(len(full_index)):
        if name in full_index[i]:
            result.append(os.path.realpath(full_index[i]))
    return result

def search_ext(name: str, full_index:list) -> list:
    '''Searches the index list by extension'''
    result = []
    for i in range(len(full_index)):
        root, ext = os.path.splitext(full_index[i])
        if name == ext:
            result.append(os.path.realpath(full_index[i]))
    return result

def search_size(size: int, full_index:list) -> list:
    '''Searches the index list for file sizes'''
    result = []
    for i in range(len(full_index)):
        if size <= os.path.getsize(full_index[i]):
            result.append(os.path.realpath(full_index[i]))
        else:
            pass
    return result

def print_paths(path: str):
    for i in os.listdir(path):
        path_to_check = os.path.join(path, i)
        if os.path.isfile(path_to_check):
            print(path_to_check)
        else:
            print_paths(path_to_check)
            
def first_line(s:str):
    f=open(s)
    line=f.readline()
    print(line)

def copy_file(file:str,newfile:str):
    shutil.copyfile(file, newfile)
    return

def touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'w').close()

if __name__ == '__main__':
    main()

