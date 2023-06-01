import argparse
import sys

"""
A fun project to allow a user to enter the co-ordinates of a player in minecraft
and get the co-ordinates from the opposing dimension.

x,y,z for overworld becomes x, y, z for the nether.

The real purpose of this script is to use 
"""

def parseArguments():
    """
    Parse the command line arguments.
    """

    parser = argparse.ArgumentParser(
        prog='MineCoords',
        description='Minecraft co-ordinates calculator',
        epilog='Text at the bottom of help')

    #parser.add_argument('filename')  # positional argument

    parser.add_argument('-x',
                        default=0,
                        type=int,
                        action="store",
                        help="The X co-ordinate of the source dimension")  # option that takes a value
    parser.add_argument('-y',
                        default=64,
                        type=int,
                        action="store",
                        help="The Y co-ordinate of the source dimension")  # option that takes a value
    parser.add_argument('-z',
                        default=0,
                        type=int,
                        action="store",
                        help="The Z co-ordinate of the source dimension")  # option that takes a value
    parser.add_argument('-d',
                        '--dimension',
                        default="overworld",
                        choices=["overworld","nether"],
                        type=str,
                        action="store",
                        help="The source dimension")

    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag

    args = parser.parse_args()

    print(args.x, args.y, args.z, args.dimension)
    print(args)

    return args

def calc_x(x,dimension):
    if dimension == "overworld":
        return int(x / 8)
    elif dimension == "nether":
        return int(x * 8)

def calc_y(y,dimension):
    return y

def calc_z(z,dimension):
    if dimension == "overworld":
        return int(z / 8)
    elif dimension == "nether":
        return int(z * 8)


def calc_dimension(dimension):
    """
    Work out the target dimension
    """
    if dimension == "overworld":
        return "nether"
    elif dimension == "nether":
        return "overworld"

def main():
    cmdargs = parseArguments()
    x = calc_x(cmdargs.x,cmdargs.dimension)
    y = calc_y(cmdargs.y,cmdargs.dimension)
    z = calc_z(cmdargs.z,cmdargs.dimension)
    dstdimension = calc_dimension(cmdargs.dimension)
    print(x,y,z,dstdimension)


if __name__ == '__main__':
    main()

    # Exit with a return code of 0 (success)
    sys.exit(0)