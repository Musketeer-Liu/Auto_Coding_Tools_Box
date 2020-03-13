__author__ = "Yutong Liu"

import os, re, sys
import app


def resolve_input():
    root_folder = sys.argv[1]
    keyword = sys.argv[2]
    replacement = sys.argv[3]

    return root_folder, keyword, replacement


if __name__ == '__main__':
    root_folder, keyword, replacement = resolve_input()


    r = app.RenameFile()
    r.rename_files(root_folder, keyword, replacement)
