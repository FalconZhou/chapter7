# coding:UTF-8

import os
"""
 列举当前目录下所有文件

Returns:
    [type]: [description]
"""

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    
    return str(files)

