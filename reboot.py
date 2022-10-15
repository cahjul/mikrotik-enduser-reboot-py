import paramiko

magicword = "/system/reboot"

#Insert your Mikrotik device information. Suggest create a low-level group and user (Only reboot + ssh permission allowed).

host = 'YOURHOSTHERE'
username = 'YOURLOWPRIVILEGEUSERHERE'
password = 'YOURSTRONGPASSWORDHERE'

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(magicword)
print(_stdout.read().decode())
client.close()
