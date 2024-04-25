#!/bin/python

import shutil


def format_bytes(num_bytes):
    """
    Convert a number of bytes into a human-readable format using binary prefixes.

    Args:
        num_bytes (int): The number of bytes.

    Returns:
        str: The formatted string with the appropriate unit.
    """
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while num_bytes >= power:
        num_bytes /= power
        n += 1
    return f"{round(num_bytes, 2)}{power_labels[n]}"


def diskspace(mode, media=False):
    dir = '/home/ramage/media' if media else '/'
    total, used, free = shutil.disk_usage(dir)
    data_disk = {
        'DiskUsage': f'{format_bytes(used)} / {format_bytes(total)}',
        'FreeSpace': f'{format_bytes(free)}'
    }
    return data_disk.get(mode, "Invalid mode specified")
