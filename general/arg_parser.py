import argparse
import os
import sys


# Usage:
# from arg_parser import parse_arguments
# args = parse_arguments()
# print(args.file)



def parse_arguments():
    parser = argparse.ArgumentParser(description="Process images using Ollama model")
    parser.add_argument("-f", "--file", help="Path to a single image file")
    parser.add_argument("-o", "--folder", help="Path to a folder to scan")
    parser.add_argument("-a", "--action", help="the action to perform: all, rename, interview, thumb, csv", default="all")

    args = parser.parse_args()

    if args.file and not os.path.isfile(args.file):
        print(f"Error: File {args.file} does not exist")
        sys.exit(1)
    
    if args.folder and not os.path.isdir(args.folder):
        print(f"Error: Folder {args.folder} does not exist")
        sys.exit(1)

    if args.file and args.folder:
        print("Error: Pick a file or a folder. Not both.")
        sys.exit(1)

    if not args.file and not args.folder:
        print("Error: Please provide either a file (-f) or a folder (-o)")
        sys.exit(1)

    if args.file:
        args.file = os.path.abspath(args.file)

    if args.folder:
        args.folder = os.path.abspath(args.folder)

    return args
