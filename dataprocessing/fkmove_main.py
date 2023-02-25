import os
import shutil
import argparse
import pathlib


def key_file_copy(file_dir, destination_dir, key, filter_param, file_type):
    """
    function to copy files to a target directory matching given parameters
    :param file_dir: location of files
    :param destination_dir: directory to copy files to
    :param key: str to include (optional)
    :param filter_param: str to exclude (optional)
    :param file_type: file you type you are filtering for (.wav)
    """
    # If key exists make it lowercase
    if key is not None:
        key = key.lower()
    # If filter exists make it lowercase
    if filter_param is not None:
        filter_param = filter_param.lower()
    # Directory search, lists all files and folders in directory
    for root, dirs, files in os.walk(file_dir):
        # loop through file names
        for file in files:
            sample_loc = os.path.join(root, file).lower()
            if key is None:
                if filter_param is None:
                    if file.endswith(file_type):
                        # copy files
                        shutil.copy(os.path.join(root, file), destination_dir)
                        print(file)
                else:
                    if filter_param not in sample_loc:
                        if file.endswith(file_type):
                            # copy files
                            shutil.copy(os.path.join(root, file), destination_dir)
                            print(file)

            else:
                if filter_param is None:
                    if key in sample_loc:
                        if file.endswith(file_type):
                            # copy files
                            shutil.copy(os.path.join(root, file), destination_dir)
                            print(file)
                else:
                    if key in sample_loc and filter_param not in sample_loc:
                        if file.endswith(file_type):
                            # copy files
                            shutil.copy(os.path.join(root, file), destination_dir)
                            print(file)


def dir_val_checker(file_dir, key, filter_param, file_type):
    """
    Function to check num of values matching your parameters
    """
    # If key exists make it lowercase
    if key is not None:
        key = key.lower()
    # If filter exists make it lowercase
    if filter_param is not None:
        filter_param = filter_param.lower()
    # Total files for print out
    total = 0

    # Directory search, lists all files and folders in directory
    for root, dirs, files in os.walk(file_dir):
        # loop through file names
        for file in files:
            # Full file path - lowercase for normalization
            sample_loc = os.path.join(root, file).lower()
            if key is None:
                if filter_param is None:
                    if file.endswith(file_type):
                        total += 1
                else:
                    if file.endswith(file_type):
                        total += 1
            else:
                if filter_param is None:
                    if key in sample_loc:
                        if file.endswith(file_type):
                            total += 1
                else:
                    if key in sample_loc and filter_param not in sample_loc:
                        if file.endswith(file_type):
                            total += 1
    return total


def print_window(key, p_line, filter_param, destination_dir, file_type, total_file_num, file_dir):
    """
    function: prints out info
    """
    print('\n')
    print(f'|Key          |{key}')
    print(f"|-------------|{p_line}")
    print(f'|Filter       |{filter_param}')
    print(f"|-------------|{p_line}")
    print(f'|File Loc     |{file_dir}')
    print(f"|-------------|{p_line}")
    print(f'|Destination  |{destination_dir}')
    print(f"|-------------|{p_line}")
    print(f'|File Type    |{file_type}')
    print(f"|-------------|{p_line}")
    print(f'|Total Files  |{total_file_num}')
    print('\n')


def line_length(file_dir, destination_dir):
    """
    Calculates length of print line length
    """
    if len(file_dir) > len(destination_dir):
        return len(file_dir) * '-'
    else:
        return len(destination_dir) * '-'


default_fd = '/Users/cameronolson/Storage/NN_PYTORCH_WORK/Drum Samples/kick'
default_d = '/Users/cameronolson/Storage/NN_PYTORCH_WORK/Drum Samples/output'
default_k = None
default_fp = None
default_ft = '.wav'

# Input info for command line use: use default_fd, default_d if you don't want to do this
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-fd', '--file_dir', type=str, default=default_fd,
                            help='Directory where files are stored')
    arg_parser.add_argument('-d', '--destination_dir', type=str, default=default_d,
                            help="Directory where you want files")
    arg_parser.add_argument('-k', '--key', type=str, default=default_k, help='keyword')

    arg_parser.add_argument('-fp', '--filter_param', type=str, default=default_fp,
                            help='Optional: word you want filtered out')
    arg_parser.add_argument('-ft', '--file_type', type=str, default=default_ft,
                            help="Type of file you want")
args = arg_parser.parse_args()
assert pathlib.Path(args.file_dir).is_dir()
assert pathlib.Path(args.destination_dir).is_dir()

file_directory = args.file_dir
destination_directory = args.destination_dir
filter_parameters = args.filter_param
key_str = args.key
file_type_filter = args.file_type

# COMMENT OUT ABOVE AND PUT PATHS BELLOW FOR NO ARGPARSE

# file_directory = ''
# destination_directory = ''
# filter_parameters = ''
# key_str = ''
# file_type_filter = ''

# =========================
# Logic
# =========================

# Calculate total files: dir_val_checker()
total_files = dir_val_checker(file_directory, key_str, filter_parameters, file_type_filter)
# calculate line: line_length()
fit_line = line_length(file_directory, destination_directory)
# print helper window
print_window(key_str, fit_line, filter_parameters, destination_directory, file_type_filter, total_files, file_directory)

# Sanity check
initializer = input('Continue[y/n] ')

if initializer.lower() == 'y':
    print('\n')
    print('Copying Files...')
    print('\n')
    key_file_copy(file_directory, destination_directory, key_str, filter_parameters, file_type_filter)
    print('\n')
    print(f'Files Moved To: {destination_directory}')
    print('\n')

else:
    print("Operation Cancelled")




