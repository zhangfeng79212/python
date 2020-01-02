from ctypes import *  # @UnusedWildImport
print(windll.kernel32)
msvcrt = cdll.msvcrt
print(msvcrt)
print(msvcrt.printf)
msg_str = b"Hello world!\n"
msvcrt.printf(b"Testing: %s", msg_str)
# 强制刷新缓冲区，立即输出，
# 若无此句，会导致下面的python语句输出结束了才输出下面的字符串
msvcrt.fflush(0)