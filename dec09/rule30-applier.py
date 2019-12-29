#!/usr/bin/env python
from math import sqrt, floor
from time import sleep

import numpy
from PIL import Image

MAGNIFICATION_FACTOR = 5

def load_image(filename):
    im = Image.open(filename)
    bytes = im.getchannel('L').tobytes()
    size = int(sqrt(len(bytes)))
    ndarr = numpy.array([int(b/0xff) for b in bytes])
    return ndarr.reshape((size, size))

def save_image(arr:numpy.ndarray, name):
    b = []
    for image_row in arr.tolist():
        for n_rows in range(MAGNIFICATION_FACTOR):
            for px in image_row:
                for n_columns in range(MAGNIFICATION_FACTOR):
                    b.append(int(px * 0xff) if px < 2 else px)
    size = arr.shape[0] * MAGNIFICATION_FACTOR
    im = Image.frombytes("L", (size, size), bytes(b))
    im.save(name)

def slide_down_ndarray(arr:numpy.ndarray):
    height = arr.shape[0]
    width = arr.shape[1]
    for row in range(arr.shape[0]-1, 0, -1):
        arr[row] = arr[row-1]
    arr[0] = numpy.ones((1, width)) * 0xff
    return arr

def slide_down_ndarray_ntimes(arr, times):
    for i in range(times):
        arr = slide_down_ndarray(arr)
    return arr

if __name__ == '__main__':
    arr = load_image('bd659aba-5ad2-4ad3-992c-6f99023792bc.small.png')
    rule30_arr = load_image('rule30-cropped.png')
    rule302_arr = load_image('rule30-cropped_2.png')
    size = rule30_arr.shape[0]
    center = int((size -1)/2)
    # cropped_rule30 = rule30_arr[0:33, center-13:center+19+1]
    # cropped_rule30 = rule30_arr[0:33, center-9:center+23+1]
    cropped_rule302 = rule302_arr[0:33, center-11:center+21+1]
    save_image(cropped_rule302, "rule30_out.png")
    # slid_rule30 = slide_down_ndarray_ntimes(cropped_rule30, 4)
    # slid_rule30 = slide_down_ndarray_ntimes(cropped_rule30, 8)
    slid_rule302 = slide_down_ndarray_ntimes(cropped_rule302, 0)
    # rot_slid_rule30 =  slide_down_ndarray_ntimes(numpy.rot90(slid_rule30), 1)
    rot_slid_rule302 =  slide_down_ndarray_ntimes(slid_rule302, 0)
    save_image(rot_slid_rule302, "rule30_out_shift.png")

    arr = numpy.logical_xor(arr, numpy.logical_not(rot_slid_rule302))
    # arr = apply_rule30_to_single_stream(arr)
    # arr = apply_rule30(arr)
    # arr = apply_rule135(arr)
    save_image(arr, "out.png")

"""
UNUSED
"""
def split_array(array, chunk_size):
    array_length = len(array)
    r = {}
    for i in range(array_length):
        row = floor(i/chunk_size)
        if r.get(row) is None:
            r[row] = []
        r[row].append(array[i])
    return r

def apply_rule30(rows):
    """
    [left_cell XOR (central_cell OR right_cell)]

    0 0 0 -> 0
    0 0 1 -> 1
    0 1 0 -> 1
    0 1 1 -> 1
    1 0 0 -> 1
    1 0 1 -> 0
    1 1 0 -> 0
    1 1 1 -> 0
    """
    rs = {}
    for index, row in rows.items():
        if index < 0:
            rs[index] = row
        else:
            rs[index] = apply_rule30_to_row(row)
    return rs

def apply_rule30_to_single_stream(rows):
    """
    [left_cell XOR (central_cell OR right_cell)]

    0 0 0 -> 0
    0 0 1 -> 1
    0 1 0 -> 1
    0 1 1 -> 1
    1 0 0 -> 1
    1 0 1 -> 0
    1 1 0 -> 0
    1 1 1 -> 0
    """
    chunk_size = len(rows.get(0))
    rs = split_array(apply_rule30_to_row([px for row in rows.values() for px in row]), chunk_size)
    return rs

def apply_rule135(rows):
    """
    NOT [left_cell XOR (central_cell AND right_cell)]

    0 0 0 -> 1
    0 0 1 -> 1
    0 1 0 -> 1
    0 1 1 -> 0
    1 0 0 -> 0
    1 0 1 -> 0
    1 1 0 -> 0
    1 1 1 -> 1
    """
    rs = {}
    for index, row in rows.items():
        if index < 0:
            rs[index] = row
        else:
            rs[index] = apply_rule135_to_row(row)
    return rs

def apply_rule30_to_row(row):
    ret_row = [row[0]]
    for i in range(1, len(row)-1):
        if i == 0:
            # continue
            left_cell = 0
        else:
            left_cell = row[i-1]
        central_cell = row[i]
        if i == len(row) - 1:
            # continue
            right_cell = 0
        else:
            right_cell = row[i+1]
        val = int(bool(left_cell) ^ (bool(central_cell) | bool(right_cell)))
        ret_row.append(val)
    ret_row.append(row[len(row) -1])
    return ret_row


def apply_rule135_to_row(row):
    ret_row = [row[0]]
    for i in range(1, len(row)-1):
        if i == 0:
            # continue
            left_cell = 0
        else:
            left_cell = row[i-1]
        central_cell = row[i]
        if i == len(row) - 1:
            # continue
            right_cell = 0
        else:
            right_cell = row[i+1]
        val = int(not bool(left_cell) ^ (bool(central_cell) & bool(right_cell)))
        ret_row.append(val)
    ret_row.append(row[len(row) -1])
    return ret_row


