# -*- coding: utf-8 -*-
from qiniu import Auth
import os
import qiniu
import base64
import Image
from time import strftime, localtime
import sys


reload(sys)
sys.setdefaultencoding('utf8')


class QiniuTool(object):
    access_key = "hbpHhfXp27MvRDhgG6aTblX-FQsncR9SUOpSfFTn"
    secret_key = "pl5-DWcb2O3RLRkjtGjr1xX67VfOM6Q2HAlu-iG-7"
    bucket_name = 'ndyd'
    q = Auth("mjVPFqjtkmymps-JmNUJbY5YScuM4DcU3o7Vt36_", "opWBNXYSrejXCzQ0-kG20YcK5YaJ-2RuD_TzMCSM")
    print q

    def __init__(self, url, directory):
        self.url = url
        self.directory = directory.decode('utf8')

    def get_name(self, name, size):
        name = self.bucket_name + ':' + name + '-' + size + self.directory[self.directory.find('.'):]
        name = base64.encodestring(name)
        return name

    def resize(self):
        img = Image.open(self.directory)
        w, h = img.size
        if w > 1000:
            h = int(1000 / float(w) * h)
            w = 1000
            h = img.resize((w, h), Image.ANTIALIAS).save(self.directory)

    def work(self):
        self.resize()
        name = strftime("%Y%m%d%H%M%S", localtime()) + self.directory[self.directory.find('.'):]
        policy = {'persistentOps': 'imageView2/2/h/80|saveas/' + self.get_name(name, '80') +
                                   ';imageView2/2/h/160|saveas/' + self.get_name(name, '160') +
                                   ';imageView2/2/h/320|saveas/' + self.get_name(name, '320') +
                                   ';imageView2/2/h/640|saveas/' + self.get_name(name, '640')
        }
        mime_type = "text/plain"
        localfile = __file__
        token = self.q.upload_token(bucket=self.bucket_name, key=name, policy=policy)
        ret, err = qiniu.put_file(token, name, self.directory)
        if err is not None:# error!
            sys.stderr.write('error:%s' % err)
        else:
            print self.url + name + image[image.find('.'):]


while True:
    directory = raw_input(u'输入文件地址'.encode('utf-8'))
    qn = QiniuTool('7i7gqh.com1.z0.glb.clouddn.com', directory)
    qn.work()