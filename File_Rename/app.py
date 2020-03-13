__author__ = "Yutong Liu"

import os, re, sys


class RenameFile:


    def rename_files(self, root_folder, keyword, replacement):
        target_dir = os.path.abspath(root_folder)
        print('Target_dir: ', target_dir)
        for file in os.listdir(target_dir):
            path, filename = os.path.split(file)
            name, extension = os.path.splitext(filename)
            source = name.split('_')[-1]
            if source == replacement: continue
            if source == keyword:
                change = name[:-len(source)] + replacement + extension
            else:
                change = name + '_' + replacement + extension
            os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, change))
            print('Rename filename: ', file)
