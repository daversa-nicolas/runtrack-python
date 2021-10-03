def demande():
    x=[input("give me a string\n")+"\n", "index 1 element\n"]
    return x

def open_file(demande):
    print(demande)
    print(type(demande))
    fdir='output.txt'
    with open(fdir,'w+') as fo:
        fo.writelines(demande)

    fo.close

def main():
    #calling function open file
    open_file(demande())

    #print(demande())

    return 0


if __name__ == '__main__':
    main()
# EndIf
