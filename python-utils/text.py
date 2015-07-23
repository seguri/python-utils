# coding: utf-8
from __future__ import unicode_literals

def isBlank(s):
    """Check if string is empty or whitespace-only
    """
    return not isNotBlank(s)

def isNotBlank(s):
    """Check if string is empty or whitespace-only
    """
    return bool(s and s.strip())