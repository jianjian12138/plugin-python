a = "it is \"ok\""
a = "it is 'ok'"
a = 'it is \'ok\''
a = 'it is "ok"'

a = """this is a multiline
string"""
b = '''another multiline
string'''

a = "both 'single' and \"double\""
a = 'both \'single\' and "double"'

a = u"unicode snowman: \u26C4"
a = r"this does not have a tab: \t"
# Bytes crash the astexport.py script
# a = b"here's some bytes"

a = '''escaped triple quote \''' in middle'''
a = """escaped triple quote \""" in middle"""

a = """other triple quote ''' in the middle"""
a = '''other triple quote """ in the middle'''

# The interior triple quotes don't get escaped properly
# a = '''both triple quotes """ and \''' in the middle'''
# a = """both triple quotes ''' and \""" in the middle"""

# In the future these might be re-flowed, if that's a feature we want to
# implement.

foo('this should NOT be '
    'a multi-line string')

foo("this should NOT be "
    'a multi-line string')

foo(r"this should NOT be \t "
    r'a multi-line string \n')

# Bytes crash the astexport.py script
#foo(bR"this should NOT be \t "
#    Br'a multi-line string \n')

foo("""this should remain as is """
    '''because it is really weird''')

foo("this should remain as is \t "
    r'because it is really weird \n')

foo(
    'this SHOULD be a multi-line string because it is very long and does not fit on one line'
)

foo(
    'this SHOULD be re-flowed, but still a multi-line string '
    "because it is very long and does not fit on one line"
)

foo(
    '''this SHOULD NOT be re-flowed, but still a multi-line string '''
    """because it is very long and does not fit on one line"""
)
