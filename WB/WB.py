import time


from wb_login import login
from wb_get_data import get_data
from wb_send import send_wb

(session, uid) = login("18482065251", "Lz122521#")
while True:
    t = time.localtime(time.time())
    if t.tm_sec == 0:
        (text, url_pic) = get_data()
        send_wb(session, text, url_pic)
    else:
        t = time.localtime(time.time())
        sec = 60 - t.tm_sec
        time.sleep(sec)
