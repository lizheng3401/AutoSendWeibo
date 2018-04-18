import json
import requests

from weibo.weibo_message import WeiboMessage

def getData():
    url_text = "https://v1.hitokoto.cn/"
    url_pic = "https://img.xjh.me/random_img.php?type=bg&ctype=nature&return=302&device=mobile"
    resp_text = requests.get(url=url_text)
    content = json.loads(resp_text.content)
    text = content.get("hitokoto")+"  ——"+content.get("from")
    return WeiboMessage(text, [url_pic])
