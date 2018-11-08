import os
import argparse


def main(database: str, url_list_file: str):
    # TODO: do something
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File path")
    parser.add_argument("-i", "--input", help="File containing data")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)