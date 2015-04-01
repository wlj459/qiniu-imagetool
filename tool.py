# -*- coding:utf-8 -*-
from qiniu import Auth
import os
import qiniu
import base64
import Image
from time import strftime, localtime


class QiniuTool(object):
    access_key = "hbpHhfXp27MvRDhgG6aTblX-FQsncR9SUOpSfFTn"
    secret_key = "pl5-DWcb2O3RLRkjtGjr1xX67VfOM6Q2HAlu-iG-7"
    bucket_name = 'zq-image'
    q = Auth(access_key, secret_key)

    def __init__(self, url, directory):
        self.url = url
        self.directory = unicode(directory, 'utf8')
    @staticmethod
    def get_name(name, size):
        name = 'zq-image:' + name + '-' + size + image[image.find('.'):]
        name = base64.encodestring(name)
        return name

    def resize(self):
        print type(self.directory)
        img = Image.open(self.directory)
        w, h = img.size
        if w > 1000:
            h = int(1000 / float(w) * h)
            w = 1000
            h = img.resize((w, h), Image.ANTIALIAS).save(image)

    def work(self):
        while True:
            self.resize()
            name = strftime("%Y%m%d%H%M%S", localtime()) + self.directory[self.directory.find('.'):]
            policy = {'persistentOps': 'imageView2/2/h/80|saveas/' + self.get_name(name, '80') +
                                       ';imageView2/2/h/160|saveas/' + self.get_name(name, '160') +
                                       ';imageView2/2/h/320|saveas/' + self.get_name(name, '320') +
                                       ';imageView2/2/h/640|saveas/' + self.get_name(name, '640')
            }
            token = self.q.upload_token(bucket=self.bucket_name, key=name, policy=policy)
            ret, err = qiniu.io.put_file(token, name, self.directory, extra)
            if err is not None:
                sys.stderr.write('error:%s' % err)
            else:
                print self.url + name + image[image.find('.'):]

directory = raw_input(u'输入文件地址'.encode('utf-8'))
qn = QiniuTool('7i7gqh.com1.z0.glb.clouddn.com', directory)
qn.work()