import os
import pathlib
import librosa


# Function: Moves files
def file_mover(file_name, root_dir, destination):
    new_file_path = os.path.join(destination, file_name)
    pathlib.Path(os.path.join(root_dir, file_name)).rename(new_file_path)


# Function Filter: Audio length
def audio_length(file_name, directory):
    full_name = os.path.join(directory, file_name)
    audio, sr = librosa.load(full_name)
    len_audio = librosa.get_duration(y=audio, sr=sr)
    return len_audio


# Function: puts it all together
def audio_length_filter(DIR, audio_filter_val):
    total = 0
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if '._' not in file:  # This can be removed: you should do filter before audio length filter
                if file.endswith('.wav'):
                    # print(os.path.join(root, file))
                    aud_len = audio_length(file, root)
                    if aud_len > audio_filter_val:
                        print(f'{file} {aud_len:.2f} sec')
                        total += 1
                        #  NEED TO ADD FILE MOVEMENT
    print(total)


def audio_filter_mover(DIR, audio_filter_val, destination):
    total = 0
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if '._' not in file:  # This can be removed: you should do filter before audio length filter
                if file.endswith('.wav'):
                    # print(os.path.join(root, file))
                    aud_len = audio_length(file, root)
                    if aud_len > audio_filter_val:
                        print(f'{file} {aud_len:.2f} sec')
                        total += 1
                        file_mover(file, root, destination)
                        #  NEED TO ADD FILE MOVEMENT
    print(total)


# Function: Print out
def filter_count(DIR, filter_str):
    total = 0
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if filter_str in file.lower():
                total += 1
                print(file)
    print(total)


def key_count(DIR, key):
    total = 0
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if key not in file.lower():
                total += 1

    print(total)


def file_filter(DIR, target_dir, filter_key_str):
    for root, dirs, files in os.walk(DIR):
        for file in files:
            if file.endswith('.wav') and filter_key_str in file.lower():
                # MOVE FILES!!!!
                print("moving")
                file_mover(file, root, target_dir)
            # if mode == 'key':
            #     if file.endswith('.wav') and filter_key_str not in file.lower():
            #         # MOVE FILES
            #         file_mover(file, root, target_dir)
            # else:
            #     print('Set mode: [filter: removes, key: keeps]')
            #     break


# LOGIC AND MORE

# General filters
f_1 = '._'  # 8192
f_2 = 'revers' # 14
f_3 = 'fx' # 56
f_4 = 'melodic' # 36
f_5 = 'vocal' # 59

# Snare
sf_1 = 'roll' #74

# kick filters
kf_1 = 'sub'  # 188: run this before 808
kf_2 = '808'  # 363: this is probobly worth it for cleaning

# Hat filters
hf_1 = 'ride' # 34
hf_2 = 'percussion' # 56
hf_3 = 'decap_808' # 25
hf_4 = 'decap_clap' # 6

time_test1 = 2.0  # this removes 1329 samples: this could be the move
time_test2 = 3.0  # this removes 451 --- this could be a good start, then examine remaining data and go lower if needed

T_DIR = '/Users/cameronolson/Storage/NN_PYTORCH_WORK/Drum Samples/kick'
B_DIR = '/Users/cameronolson/ML-DataSets/Sample Dataset/snares'
path_dump = '/Users/cameronolson/ML-DataSets/DUMP'
# audio_length_filter(B_DIR, 2.0)
# audio_filter_mover(B_DIR, 2.0, path_dump)
# filter_count(B_DIR, hf_1)
# key_count(B_DIR, 'hat')
# file_filter(B_DIR, path_dump, hf_1)

# TODO: Fix mode -- you dont need it but it would be good
# TODO: test file move
