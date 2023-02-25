import os


def total_files(directory, f_type):
    total = 0
    for root, dims, files in os.walk(directory):
        for file in files:
            if file.endswith(f_type):
                total += 1
    return total


def data_distribution(directory, f_type):
    dir_out = []
    for root, dirs, file in os.walk(directory):
        for i in range(len(dirs)):
            sub_dir = f'{directory}/{dirs[i]}'
            sub_files_num = total_files(sub_dir, f_type)
            dir_out.append([dirs[i], sub_files_num])
    return dir_out


def data_percentage(idx_dir, all_files):
    print('DATA INFO')
    print('--------------------------')
    for fold, numb in idx_dir:
        print(f'TOTAL {fold.upper()}: {numb}')
        print(f'Percent of data {fold}: {(numb / all_files) * 100:.1f} %')
        print('--------------------------')


file_dir = '/Users/cameronolson/ML-DataSets/Sample Dataset'
file_type = '.wav'

link_list = data_distribution(file_dir, file_type)

num_files = total_files(file_dir, file_type)

print('\n')
print(f'Total Files: {num_files}')
print(f'Directory: {file_dir}')
print('\n')

data_percentage(link_list, num_files)
