import sys

args = sys.argv.pop(1)

def main():
    s, o, c = "", "", 1
    for i in args:
        if s == i:
            c += 1
        else:
            if c != 1:
                o += str(c)
            o += i
            c = 1
            s = i
    print(o)

if __name__ == '__main__':
    main()