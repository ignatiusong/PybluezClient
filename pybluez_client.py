import sys
import bluetooth

uuid = "ce5b77c0-1cfc-11ec-8367-0800200c9a66"
address = "A8:0C:63:2E:F7:0A"
service_matches = bluetooth.find_service(address=address, uuid=uuid)

if len(service_matches) == 0:
    print("couldn't find the FooBar service")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
while True:
    msg = sock.recv(1024).decode()
    print(msg)
    if msg == 'quit':
        break
    sock.send(msg.encode())
sock.close()
