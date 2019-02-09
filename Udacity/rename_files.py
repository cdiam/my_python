#!/usr/bin/python

import os

import time



def rename_files():
    file_list = os.listdir("/Users/cdiam/.wireshark/profiles")
    print file_list

rename_files()