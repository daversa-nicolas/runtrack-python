
def open_file():
    fdir='output1.txt'

    with open(fdir,'r+') as fo:
        string=fo.readline()
    #comment

    return string

    fo.close

def print_console(open_file):
    print(open_file)

def main():
    #calling function open file
    print_console(open_file)

    #print(demande())

if __name__ == '__main__':
    main()
# EndIf
