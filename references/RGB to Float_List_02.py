import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    rgbvar = [0.123,0.733,0.345]
    rgbvar2 = [x * 255.0 for x in rgbvar]
    rround =  [round(x,3) for x in rgbvar2]
    rint = [int(x) for x in rround]
    print rround
    print rgbvar2
    print rint

if __name__=='__main__':
    main()
