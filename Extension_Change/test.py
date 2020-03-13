__author__ = "Yutong Liu"

import os, re, sys, logging
import app


def resolve_input():
    root_folder = sys.argv[1]
    replacement = sys.argv[2]

    return root_folder, replacement


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)

    root_folder, replacement = resolve_input()
    logging.warning('Test')


    EC = app.ExtensionChange()
    EC.extension_change(root_folder, replacement)
