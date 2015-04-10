# -*- coding: utf-8 -*-
import qiniu.conf
import sys
import os
import qiniu.io
import qiniu.rs
import base64
import Image
from time import strftime,localtime


class QiniuTool(object):
    bucket_name = 'zq-image'
    qiniu.conf.ACCESS_KEY = "hbpHhfXp27MvRDhgG6aTblX-FQsncR9SUOpSfFTn"
    qiniu.conf.SECRET_KEY = "pl5-DWcb2O3RLRkjtGj1xX67VfOM6Q2HAlu-iG-7"

    def __init__(self, url, directory):
        self.url = url
        self.directory = directory.decode('GBK')

    def get_name(self, name, size):
        name = self.bucket_name + ':' + name + '-' + size
        name = base64.encodestring(name)
        return name

    def resize(self):
        img = Image.open(self.directory)
        w, h = img.size
        if w > 1000:
            h = int(1000 / float(w) * h)
            w = 1000
            img.resize((w, h), Image.ANTIALIAS).save(self.directory)

    def work(self):
        self.resize()

        name = strftime("%Y%m%d%H%M%S", localtime())

        policy = qiniu.rs.PutPolicy(self.bucket_name)
        policy.saveKey = name
        policy.persistentOps = 'imageView2/2/h/80|saveas/' \
                               + self.get_name(name, '80') \
                               + ';imageView2/2/h/160|saveas/' \
                               + self.get_name(name, '160') \
                               + ';imageView2/2/h/320|saveas/' \
                               + self.get_name(name, '320') \
                               + ';imageView2/2/h/640|saveas/' \
                               + self.get_name(name, '640')
        uptoken = policy.token()
        extra = qiniu.io.PutExtra()

        ret, err = qiniu.io.put_file(uptoken, None, self.directory, extra)
        if err is not None:
            sys.stderr.write('error:%s' % err)
        else:
            print '7i7gqh.com1.z0.glb.clouddn.com/' + name + '\n\n\n'


while True:
    enter = raw_input(u'输入任意键继续'.encode('gbk'))
    os.system('cls')
    directory = raw_input(u'输入文件地址:\n\n'.encode('gbk'))
    if directory[0] == '"':
        directory = directory[1:len(directory) - 1]
    print (u'\n\n文件正在上传。。。。。。。。。\n\n'.encode('gbk'))
    print (u'图片链接地址：\n\n'.encode('gbk'))
    qn = QiniuTool('http://7i7gqh.com1.z0.glb.clouddn.com/', directory)
    qn.work()
