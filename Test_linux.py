# coding:utf-8
import paramiko

ip = '219.243.86.220'
port = 22
username = 'root'
password = '3W.hebut.com'
win_path = 'D:/sysctl.conf'
linux_path = '/etc/sysctl.conf'


# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip, port, username, password)
def login(ip, username, password, port=22):
    '''
    用paramiko SSH登录远程服务器
    ip: 远程服务器的IP
    username: 远程服务器登录用户名
    password: 远程服务器登录用户密码
    port: 远程服务器的端口，SSH协议默认为22
    '''
    # 创建一个SSH客户端对象
    ssh = paramiko.SSHClient()
    # 设置访问策略
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 与远程主机进行连接
    ssh.connect(hostname=ip, port=port, username=username, password=password)
    return ssh


def upload_file(ssh, local_file_path, remote_file_path):
    '''
    上传文件

    :param ssh: SSH连接对象
    :param local_file_path: 本地文件路径
    :param remote_file_path: 远程文件存放路径
    '''
    # 创建sftp对象上传文件
    sftp = ssh.open_sftp()
    sftp.put(local_file_path, remote_file_path)
    sftp.close()


def download_file(ssh, remote_file_path, local_file_path):
    '''
    下载文件

     ssh: SSH连接对象
     remote_file_path: 远程文件路径
     local_file_path: 本地文件存放路径
    '''
    # 创建sftp对象下载文件
    sftp = ssh.open_sftp()
    sftp.get(remote_file_path, local_file_path)
    sftp.close()


def main():
    ssh = login(ip, username, password)

    # 上传文件
    upload_file(ssh, win_path, linux_path)
    # 下载文件
    download_file(ssh, linux_path, win_path)


if __name__ == '__main__':
    main()
