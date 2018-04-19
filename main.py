# -*- coding: utf-8 -*-

import send_task
from weibo.weibo_login import wblogin
from picLogin import login
if __name__ == '__main__':
    # (wei_session, uid) = wblogin(username, password)
    (wei_session, uid) = login("18482065251", "Lz122521#")
    if uid is not None:
        wei_session.get('http://weibo.com/')
        task = send_task.SendTask(wei_session, uid)
        task.start()

        while True:
            cmd = input('enter [exit] to stop:')
            if cmd.upper() == "EXIT":
                task.stop()
                break

    print('exit...')
