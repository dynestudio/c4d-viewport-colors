import c4d
from c4d import gui
#Welcome to the world of Python


def main():
    rgbvar = [80,160,240]
    rgbvar2 = [x / 255.0 for x in rgbvar]
    rround =  [round(x,3) for x in rgbvar2]
    print rround
    print rgbvar2

if __name__=='__main__':
    main()
