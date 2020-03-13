__author__ = "Yutong Liu"

import os, re, sys, logging


class ExtensionChange:


    def extension_change(self, root_folder, replacement):
        target_dir = os.path.abspath(root_folder)
        logging.warning('Target_dir: {}'.format(target_dir))
        # print('Target_dir: ', target_dir)
        for file in os.listdir(target_dir):
            filename, extension = os.path.splitext(file)
            changed = filename + '.' + replacement
            os.rename(os.path.join(target_dir, file), os.path.join(target_dir, changed))
            # print('Change Extension of {} to {}: '.format(file, changed))
            logging.warning('Change Extension of {} to {}: '.format(file, changed))
