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

def calc_x(args):
    if args.dimension == "overworld":
        return int(args.x / 8)
    elif args.dimension == "nether":
        return int(args.x * 8)

def calc_y(args):
    return args.y

def calc_z(args):
    if args.dimension == "overworld":
        return int(args.z / 8)
    elif args.dimension == "nether":
        return int(args.z * 8)


def calc_dimension(args):
    """
    Work out the target dimension
    """
    if args.dimension == "overworld":
        return "nether"
    elif args.dimension == "nether":
        return "overworld"

def main():
    cmdargs = parseArguments()
    x = calc_x(cmdargs)
    y = calc_y(cmdargs)
    z = calc_z(cmdargs)
    dstdimension = calc_dimension(cmdargs)
    print(x,y,z,dstdimension)


if __name__ == '__main__':
    main()

    # Exit with a return code of 0 (success)
    sys.exit(0)