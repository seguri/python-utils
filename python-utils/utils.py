# coding: utf-8

#-------------------------------------------------------------------------------
# Strings
#-------------------------------------------------------------------------------

def isBlank(s):
    """Check if string is empty or whitespace-only
    """
    return not isNotBlank(s)

def isNotBlank(s):
    """Check if string is empty or whitespace-only
    """
    return bool(s and s.strip())