import urllib.request
import shutil
import pysftp

def retrieve_external_ip():
    #This part gets the public IP address.
    get_public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    #This part opens the existing_ip.txt file, writes the data from 'existing_ip_file' to it, then closes it.
    existing_ip_file = open('/home/ssymon/python_scripts/existing/existing_ip.txt','w')
    existing_ip_file.write(get_public_ip)
    existing_ip_file.close()

def compare_IP_addresses():
    #This part opens the existing_ip.txt file and reads puts its contents into the existing_ip_file_contents variable.
    existing_ip_file = open('/home/ssymon/python_scripts/existing/existing_ip.txt','r')
    existing_ip_file_contents = existing_ip_file.read()
    #This part opens the previous_ip.txt file and reads puts its contents into the previous_ip_file_contents variable.
    previous_ip_file = open('/home/ssymon/python_scripts/previous/previous_ip.txt','r')
    previous_ip_file_contents = previous_ip_file.read()
    existing_ip_file.close()
    previous_ip_file.close()
    #This part compares the existing_ip_file_contents and previous_ip_file_contents variables and copies if different.
    if existing_ip_file_contents != previous_ip_file_contents:
        shutil.copy('/home/ssymon/python_scripts/existing/existing_ip.txt','/home/ssymon/python_scripts/previous/previous_ip.txt')
        sftp_transfer()

def sftp_transfer():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host='symon.ca', username='put_username_here', password='put_password_here', cnopts=cnopts, port=put_port#_here) as sftp:
        sftp.put_d('/home/ssymon/python_scripts/previous/','/SYMON_SHARE/Router Backups/marg_ip/')
        sftp.close()

retrieve_external_ip()
compare_IP_addresses()
