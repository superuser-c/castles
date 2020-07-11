import socket as sck
import random as rnd
import threading

class ServerClient:
  def __init__(self, con, ip, port):
    self.con = con
    self.ip = ip
    self.port = port
  def close(self):
    self.con.close()

class Server:
  def __init__(self):
    self.host = "127.0.0.1"
    self.port = rnd.randrange(1024, 65536)
    self.s = None
    self.lt = None
    self.ltstop = False
    self.autoclose = True
    self.clients = []
  def start(self):
    self.s = sck.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((host, port))
    self.lt = threading.Thread(None, lambda: self.listen())
  def listen():
    while True:
      try:
        self.s.listen(1)
        self.s.settimeout(1)
        (con, (ip, port)) = self.s.accept()
        self.clients.append(ServerClient(con, ip, port))
      except socket.timeout:
        if self.ltstop:
          break
    if self.autoclose:
      self.close()
  def tick(self):
    pass
  def sendall(self):
    pass
  def stop(self):
    self.ltstop = True
  def close(self):
    for cl in self.clients:
      cl.close()
    if self.s is not None:
      self.s.close()
