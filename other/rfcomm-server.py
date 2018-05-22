from bluetooth import *
import pygame

pygame.mixer.init()
bearSound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/bear.wav")
greetingSound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/greeting.wav")
kissesSound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/kisses.wav")
laughSound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/laugh.wav")
secretSound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/secret.wav")
sorrySound = pygame.mixer.Sound("/home/pi/Workspace/path-agile-development/other/sorry.wav")

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                   #protocols = [ OBEX_UUID ]
                   )

while True:
    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
        if data == "makeBearSound":
          bearSound.play()
        elif data == "makeGreetingSound":
          greetingSound.play()
        elif data == "makeKissesSound":
          kissesSound.play()
        elif data == "makeLaughSound":
          laughSound.play()
        elif data == "makeSecretSound":
          secretSound.play()
        elif data == "makeSorrySound":
          sorrySound.play()
    except IOError:
        pass
    except KeyboardInterrupt:

        print "disconnected"

        client_sock.close()
        server_sock.close()
        print "all done"

        break

# print("disconnected")
#
# client_sock.close()
# server_sock.close()
# print("all done")
