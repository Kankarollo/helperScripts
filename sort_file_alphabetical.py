import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Sort file in alphabetical order")
    parser.add_argument('-p',dest='path', type=str, help="Path to file to be sorted.")
    parser.add_argument('-s',dest='save_path', type=str, help="Path to save sort list.")

    args = parser.parse_args()

    if not args.path:
        print("Add path to the file.")
        error()

    path_to_file = args.path
    path_to_new_file = path_to_file

    if args.save_path:
        path_to_new_file = args.save_path 

    file_text = load_file(path_to_file)
    file_text.sort()
    save_to_file(file_text, path_to_new_file)

    print("Script ended successfull!")


def load_file(path:str):
    with open(path, "r") as file:
        file_text = [line for line in file.readlines()]
    return file_text

def save_to_file(file_text:list, path:str):
    with open(path, "w") as file:
        for line in file_text:
            file.writelines(line)

def error():
    print("Script failed...")
    sys.exit(1)

if __name__ == '__main__':
    main()
