#!/usr/bin/python2.7

# NTLM: MD4( UTF-16LE('secret') )

import hashlib, sys

print hashlib.new(
    'md4',
    ''.join(
        sys.argv[1:]
    ).encode('utf-16le')
).hexdigest()
