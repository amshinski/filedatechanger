import os
import sys
import time
import ntpath
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from win32_setctime import setctime


def time_to_seconds(month, day, year, hour, minute, second):
    """Function returns custom time to seconds passed since epoch.

        Arguments:
                month {int} -- numbers 1-12
                day {int} -- num 1-31
                year {int} -- year in format YYYY
                hour {int} -- num 0-23
                minute {int} -- num 0-59
                second {int} -- num 0-59

        Returns:
                Time %m/%d/%Y %H:%M:%S to seconds passed since epoch.
        """
    choose_time = (f'{month}/{day}/{year} {hour}:{minute}:{second}')
    target_time = time.strptime(choose_time, '%m/%d/%Y %H:%M:%S')
    target_time = time.mktime(target_time)
    return target_time


def get_files_path():
    Tk().withdraw()
    files = askopenfilenames()
    return files


# def get_files_modification_time(filenames):
#     mod_time_dict = {}
#     for file in filenames:
#         mod_time_dict[file] = str(time.ctime(os.stat(file)[8]))
#     return mod_time_dict


# def get_files_creation_time(filenames):
#     cr_time_dict = {}
#     for file in filenames:
#         cr_time_dict[file] = str(time.ctime(os.stat(file)[9]))
#     return cr_time_dict


def get_mod_and_cr_time(filenames):
    time_dict = {}
    for file in filenames:
        head, tail = ntpath.split(file)
        if tail:
            time_dict[tail] = (
                str(time.ctime(os.stat(file)[8])),
                str(time.ctime(os.stat(file)[9]))
            )
        else:
            time_dict[ntpath.basename(head)] = (
                str(time.ctime(os.stat(file)[8])),
                str(time.ctime(os.stat(file)[9]))
            )
    return time_dict


def change_files_modification_time(modified_time, filenames=()):
    for file in filenames:
        os.utime(file, (time.time(), modified_time))


def change_files_creation_time(modified_time, filenames=()):
    for file in filenames:
        setctime(file, modified_time)
