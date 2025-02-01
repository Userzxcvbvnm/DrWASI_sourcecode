from enum import Enum

class FUNCPATTERN(Enum):
    args_get = (r'(Argument 0: ).*', r'\1(.*)')
    args_sizes_get = (r'(Argument 0 size: ).*', r'\1(.*)')
    clock_time_get = (r'Current time: (.*) seconds, .* nanoseconds', r'Current time: \1 seconds, (.*) nanoseconds')
    fd_fdstat_set_rights = (r'Current file rights:\s*([\s\S]*?)\n\n', r'Current file rights:(.*)\n\n')
    fd_pread = (r'(preadv successfully read 0 bytes|preadv error.)', r'(preadv successfully read 0 bytes|preadv error.)')
    fd_pwrite = (r'pwritev successful. 0 bytes written', r'(pwritev successful. 0 bytes written|pwritev failed)\\s*')
    fd_read = (r'Read 0 bytes using readv', r'(Read 0 bytes using readv|Error reading from file descriptor)\\s*')
    fd_write = (r'Enter function fd_write_.*\nFile current offset before write: 0\nFile current offset after write: 0\nWrite to file descriptor successful. Number of bytes written: 0', r'Enter function fd_write_.*\nFile current offset before write: 0\nFile current offset after write: 0\n(Write to file descriptor successful. Number of bytes written: 0|Write to file descriptor failed!)')
    random_get = (r'Enter random_get_(.*?).\nRandom number: \d+', r'Enter random_get_(.*?).\nRandom number: \\d+')
    path_open = (r'Open file or directory failed: (Permission denied|Operation not permitted)', r'Open file or directory failed: (Permission denied|Operation not permitted)')