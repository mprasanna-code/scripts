#!/usr/bin/env python

import sys
import paramiko
import getpass


def ssh_command(ssh, command_file):
    ssh.invoke_shell()
    with open(command_file) as f:
        for command in f:
            print '##### Command: ' + command
            stdin, stdout, stderr = ssh.exec_command(command)
            print('======================= Stdout')
            print(stdout.read())
            print('======================= StdError')
            print(stderr.read()) 
            print('================================')

def ssh_connect(host, user, key):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh.connect(hostname=host, username=user, key_filename=key)
        ssh.connect(hostname=host, username=user, password=key)
        print '***** Executing on ' + host + '  User: ' + user
        return ssh
    except Exception as e:
        print('Connection Failed')
        print(e)

if __name__ == '__main__':
    username = raw_input("Username:")
    #key = raw_input("Public key full path:")
    #key= raw_input("Password:")
    key=getpass.getpass()
    #host = raw_input("Target Host:")
    cmd_file = sys.argv[1]
    with open(sys.argv[2]) as f:
        for host in f:
            ssh_h = ssh_connect(host.strip(), username, key)
            ssh_command(ssh_h, cmd_file)
