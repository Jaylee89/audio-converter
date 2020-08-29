#!/usr/bin/env python3

import sys
from pymediainfo import MediaInfo

def log(s):
    sys.stderr.write("[log] {}".format(s))
    sys.stderr.write("\n")
    sys.stderr.flush()

if __name__ == "__main__":
    media_info = MediaInfo.parse('input/85537')
    data = media_info.to_json()
    log(data)
    log("Completed!")