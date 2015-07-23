# coding: utf-8
from __future__ import unicode_literals
import hashlib


def hash(absfilepath, hasher):
    with open(absfilepath, 'r') as f:
        hasher.update(f.read())
        return hasher.hexdigest()

def hash_lowmem(absfilepath, hasher, blocksize=2**16):
    """Memory efficient version
    """
    with open(absfilepath, 'r') as f:
        buf = f.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(blocksize)
        return hasher.hexdigest()

def md5(absfilepath):
    with open(absfilepath, 'r')as f:
        return hashlib.md5(f.read()).hexdigest()