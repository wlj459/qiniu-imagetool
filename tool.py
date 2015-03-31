# -*- coding:utf-8 -*-
from qiniu import auth
import os
import qiniu.io
import qiniu.rs
import base64
import Image
from time import strftime, localtime


class QiniuTool(self):
    access_key = "hbpHhfXp27MvRDhgG6aTblX-FQsncR9SUOpSfFTn"
    secret_key = "pl5-DWcb2O3RLRkjtGj1xX67VfOM6Q2HAlu-iG-7"
    bucket_name = 'zq-image'
    q = auth(access_key, secret_key)

    def __init__(self, url, directory):
        self.url = url
        self.directory = directory

    @staticmethod
    def get_name(name, size):
        name = 'zq-image:'+name+'-'+size+image[image.find('.'):]
        name = base64.encodestring(name)
        return name

    def resize(self):
        img = Image.open(self.directory)
        w, h = img.size
        if w > 1000:
            h = int(1000/float(w)*h)
            w = 1000
            h = img.resize((w, h), Image.ANTIALIAS).save(image)

    def work(self):
        while True:
            self.resize()
            name = strftime("%Y%m%d%H%M%S", localtime())
            policy = qiniu.rs.PutPolicy('zq-image')
            policy.saveKey = name+image[image.find('.'):]
            policy.persistentOps = 'imageView2/2/h/80|saveas/' + self.get_name(name, '80') + \
                                   ';imageView2/2/h/160|saveas/' + self.get_name(name, '160') + \
                                   ';imageView2/2/h/320|saveas/' + self.get_name(name, '320') + \
                                   ';imageView2/2/h/640|saveas/' + self.get_name(name, '640')
            uptoken = policy.token()
            extra = qiniu.io.PutExtra()
            ret, err = qiniu.io.put_file(uptoken, None, image, extra)
            if err is not None:
                sys.stderr.write('error:%s' % err)
            else:
                print self.url + name + image[image.find('.'):]


