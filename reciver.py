from django.dispatch import receiver
from vidstream import StreamingServer
import threading

#privte ip-> only check in cmd
#port-> any
receiver = StreamingServer('#private_ip',9090)


#threading for parallell 
thr = threading.Thread( target = receiver.start_server)
thr.start()

while input('') != 'stop':
    continue

receiver.stop_server()
##########################################