import argparse
import os

def get_size_dir(path, extension=None):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                if extension is None or f.endswith(extension):
                    total_size += os.path.getsize(fp)
    return total_size

def get_size_file(path):
    return os.path.getsize(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--directory", help="get size of directory")
    group.add_argument("-f", "--file",      help="get size of file")
    parser.add_argument("-F", "--Format",   help="specific formats")
    args = parser.parse_args()
    if args.directory:
        if args.Format:
            print(int(get_size_dir(args.directory, args.Format) / 1024), "KB")
        else:
            print(int(get_size_dir(args.directory) / 1024), "KB")
    elif args.file:
        print(int(get_size_file(args.file) / 1024), "KB")
