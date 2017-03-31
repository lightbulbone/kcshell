#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'rui@deniable.org'

import sys
if sys.version_info.major < 3: print("[-] You need Python 3."); sys.exit(255)

APP_NAME = "kcshell"
APP_VERSION = "0.0.1b"

import config

class Kickoff(object):
    def run(self):
        pwn = config.get_op_modes()[config.get_default_op_mode()]
        pwn.cmdloop()

def main():
    Kickoff().run()

if __name__ == '__main__':
    print("-=[ {0} v{1} ]=-".format(APP_NAME, APP_VERSION))
    main()

