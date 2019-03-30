

handle = open(‘/ tmp/random_data.txt’)  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()  # Always runs after try:


"""Any exception raised by the read method will always propagate up to the calling code,
yet the close method of handle is also guaranteed to run in the finally block. You
must call open before the try block because exceptions that occur when opening the file
(like IOError if the file does not exist) should skip the finally block."""
