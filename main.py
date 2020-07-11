import argparse


def main():
    parser = argparse.ArgumentParser(
        description="sum the integers at the command line")

    parser.add_argument(
        "markdown_files",
        nargs="+",
        help="files to convert to markdown")

    args = parser.parse_args()
    print(args.markdown_files)


if __name__ == "__main__": 
    main()

    
