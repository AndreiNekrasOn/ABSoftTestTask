import multiprocessing as mp
import os
import ftplib
import json


class ServerInfo(object):
    def __init__(self, config_file):
        with open(config_file) as cf:
            server_info = json.loads(cf.read())
        self.name = server_info['server_name']
        self.username = server_info['user_name']
        self.password = server_info['password']
        self.local_paths = server_info['local_paths']
        self.server_paths = server_info['server_paths']


def ftp_makedir(path):
    try:
        ftps.mkd(os.path.dirname(path))
    except ftplib.error_perm:
        if len(os.path.dirname(path)):
            print("path is not a valid directory or directory already exists: ", os.path.dirname(path), sep='')
        else:
            pass


def ftp_write(local_dir, ftp_dir):
    ftp_makedir(ftp_dir)
    with open(local_dir, 'rb') as f:
        ftps.storbinary("STOR " + ftp_dir, f)


server = ServerInfo("config.json")
ftps = ftplib.FTP(server.name)
ftps.login(server.username, server.password)

if __name__ == '__main__':
    zipped_dirs = zip(server.local_paths, server.server_paths)
    with mp.Pool() as pool:
        pool.starmap(ftp_write, zipped_dirs)
