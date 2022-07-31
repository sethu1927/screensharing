
from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("#private_ip",9090)

thr = threading.Thread( target = sender.start_stream)
thr.start()

while input('') != 'stop':
    continue
sender.stop_stream()
##############################