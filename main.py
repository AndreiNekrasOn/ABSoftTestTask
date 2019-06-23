import multiprocessing as mp
import os
import ftplib

ftps = ftplib.FTP('localhost')
ftps.login('Andrei', '')


def ftp_validate_dir(path):
    try:
        ftps.mkd(os.path.dirname(path))
    except ftplib.error_perm:
        if len(os.path.dirname(path)):
            print("logfile :: path is not a valid directory or directory already exists: /",
                  os.path.dirname(path), sep='')
        else:
            pass


def ftp_write(local_dir, ftp_dir):
    ftp_validate_dir(ftp_dir)
    with open(local_dir, 'rb') as f:
        ftps.storbinary("STOR " + ftp_dir, f)


if __name__ == '__main__':
    srcs = [
        'C:\\Users\\Андрей\\Desktop\\PythonPro\\ABSoftTestTask\\first.txt',
        'C:\\Users\\Андрей\\Desktop\\PythonPro\\ABSoftTestTask\\second.txt',
    ]
    nsrcs = [
        'helllo/new.txt',
        'bye.txt',
    ]

    zipped_dirs = list(zip(srcs, nsrcs))
    with mp.Pool() as pool:
        pool.starmap(ftp_write, zipped_dirs)


# import multiprocessing as mp
# import os
# import ftplib
#
#
# class FTPWriter:
#     ftps = ftplib.FTP()
#
#     def __init__(self, address, username, password):
#         ftps = ftplib.FTP(address)
#         ftps.login(username, password)
#
#     def validate_dir(self, path):
#         try:
#             self.ftps.mkd(os.path.dirname(path))
#         except ftplib.error_perm:
#             if len(os.path.dirname(path)):
#                 print("logfile :: path is not a valid directory or directory already exists: /",
#                       os.path.dirname(path), sep='')
#             else:
#                 pass
#
#     def write(self, local_dir, ftp_dir):
#         self.validate_dir(ftp_dir)
#         with open(local_dir, 'rb') as f:
#             self.ftps.storbinary("STOR " + ftp_dir, f)
#
#     def __del__(self):
#         self.ftps.close()
#
#
# if __name__ == '__main__':
#     srcs = [
#         'C:\\Users\\Андрей\\Desktop\\PythonPro\\ABSoftTestTask\\first.txt',
#         'C:\\Users\\Андрей\\Desktop\\PythonPro\\ABSoftTestTask\\second.txt',
#     ]
#     nsrcs = [
#         'helllo/new.txt',
#         'bye.txt',
#     ]
#
#     writer = FTPWriter('localhost', 'Andrei', '')
#     zipped_dirs = list(zip(srcs, nsrcs))
#     with mp.Pool() as pool:
#         pool.starmap(writer.write, zipped_dirs)
