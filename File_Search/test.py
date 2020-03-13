__author__ = "Yutong Liu"

import os, re, sys
import app


def resolve_input():
    keyword = sys.argv[1]
    root_folder = sys.argv[2]

    return root_folder, keyword


if __name__ == '__main__':
    s = app.SearchFile()

    root_folder, keyword = resolve_input()
    result = s.search_file(keyword=keyword, root_folder=root_folder)
    s.plot_result(result=result)

