__author__ = "Yutong Liu"

import os, re, sys
import matplotlib.pyplot as plt



class SearchFile:

    def search_file(self, keyword, root_folder):
        result = dict()
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                if re.search(keyword, file) is not None:
                    result[root] = result.get(root, 0) + 1 
        print(result)
        return result

    def plot_result(self, result):
        key_list, val_list = [], []
        for key, val in result.items():
            key_list.append(key)
            val_list.append(val)

        plt.bar(key_list, val_list)
        plt.savefig('/Users/yutong/diagram.png')


