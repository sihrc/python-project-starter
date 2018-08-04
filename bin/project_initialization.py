#! /usr/bin/python3
# This script is self destructive. Once complete, the project will be formatted with proper values & this script will be deleted.

import argparse
import os
import shutil

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
IGNORE_PATHS = (
    os.path.abspath(os.path.join(PROJECT_ROOT, ".git")),
    os.path.abspath(__file__),
)


def walk_directory(fsobj, args):
    if os.path.abspath(fsobj) in IGNORE_PATHS:
        return
    if os.path.isdir(fsobj):
        new_fsobj = fsobj.replace("{{package}}", args["package"])
        if new_fsobj != fsobj:
            os.rename(fsobj, new_fsobj)
        for item in os.listdir(new_fsobj):
            walk_directory(os.path.join(new_fsobj, item), args)
    else:
        with open(fsobj, "r") as file_read:
            contents = file_read.read()

        for key, value in args.items():
            contents = contents.replace("{{" + key + "}}", value)

        with open(fsobj, "w") as file_write:
            file_write.write(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--author", help="Name of author", required=True)
    parser.add_argument(
        "--email", help="Email for contacting author about project", required=True
    )
    parser.add_argument(
        "--package", help="Name for the this python project", required=True
    )
    parser.add_argument(
        "--description", help="Description for this python project", required=True
    )

    args = vars(parser.parse_args())
    walk_directory(PROJECT_ROOT, args)
    with open(os.path.join(PROJECT_ROOT, ".env"), "w") as f:
        f.write("# environment variables")
    os.remove(__file__)
