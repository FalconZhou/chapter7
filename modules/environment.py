# coding: UTF-8
"""
 获取所有环境变量

Returns:
    [type]: [description]
"""

import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)