#!/usr/bin/env python3

from core import omnibus

if __name__ == '__main__':
    #local env
    omnibus.run(port=5993, debug=True)
