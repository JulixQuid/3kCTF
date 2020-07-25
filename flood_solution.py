from pwn import *
import time

class Pwner():

    def __init__(self):
        self.conn = remote( 'flood.3k.ctf.to' , 7777)
        self.logs_console=list()
        self.key = '35ec04cd3b79ab89896836c69257ce86487cf55f'

    def auth(self):
        self.conn.sendline(self.key)
        self.conn.sendline('Hextraditables')

    def earn1000Points(self):
        tic=time.time()
        for i in range(0, 1000):
            print(self.conn.recvline())
            self.conn.sendline('1')
            print(self.conn.recv(10000))
            self.conn.sendline('1')
            print(self.conn.recv(10000))
            suma_str = self.conn.recvline()
            print(suma_str)
            aux=sum([int(s) for s in suma_str.split() if s.isdigit()])
            print(aux)
            self.conn.sendline(str(aux))
        toc = time.time()
        print(toc-tic,'secs. earning 1000 points ')

    def buyGold(self):

pwner=Pwner()
pwner.auth()
pwner.earn1000Points()
pwner.conn.interactive()