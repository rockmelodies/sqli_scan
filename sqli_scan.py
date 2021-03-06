"""
Author : d4m1ts
Version : 0.0.1
"""
import argparse
import sys
import os
from color import *

from libs import bing
from libs import yahoo
from libs import google

from src import Scan

def menu():
    parse = argparse.ArgumentParser()
    parse.add_argument('-k',dest='keyword',metavar='inurl:example',
                       help="sql injection keyword")
    parse.add_argument('-p',dest='page_num',metavar='5',
                       help="page of websites to look for in search engine")
    parse.add_argument('-e',dest='engine',metavar='search engine',
                       help="the search engine you want to use.  bing,yahoo,google")
    args = parse.parse_args()
    return args

def main():
    args = menu()
    if len(sys.argv) == 1:
        print ('Please add -h to get help ')
        sys.exit(0)

    keyword = str(args.keyword)
    page_num = int(args.page_num)
    engine = str(args.engine)
    if engine == 'bing':
        instance = bing.Bing(keyword,page_num)
        links = (instance.bing())
    elif engine == 'yahoo':
        instance = yahoo.Yahoo(keyword,page_num)
        links = (instance.yahoo())
    elif engine == 'google':
        instance = google.Google(keyword,page_num)
        links = (instance.google())

    scan = Scan.Scan(links)
    scan.main()
if __name__ == '__main__':
    if os.name == 'nt':
        printYellow ('''
    ===============================================================================

    _________________   .____    .___    _________
    /   _____/\_____  \ |    |   |   |  /   _____/ ____ _____    ____
    \_____  \  /  / \  \|    |   |   |  \_____  \_/ ___\\\\__  \  /    \\
    /        \/   \_/.  \    |___|   |  /        \  \___ / __ \|   |  \\
   /_______  /\_____\ \_/_______ \___| /_______  /\___  >____  /___|  /
           \/        \__>       \/             \/     \/     \/     \/
                                                                        d4m1ts
    ===============================================================================
        ''')
    else:
        print ("\033[1;33m" + '''
    ===============================================================================

    _________________   .____    .___    _________
    /   _____/\_____  \ |    |   |   |  /   _____/ ____ _____    ____
    \_____  \  /  / \  \|    |   |   |  \_____  \_/ ___\\\\__  \  /    \\
    /        \/   \_/.  \    |___|   |  /        \  \___ / __ \|   |  \\
   /_______  /\_____\ \_/_______ \___| /_______  /\___  >____  /___|  /
           \/        \__>       \/             \/     \/     \/     \/
                                                                        d4m1ts
    ===============================================================================
        '''+"\033[1;34m")
    main()
