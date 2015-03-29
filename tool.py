# -*- coding:utf-8 -*-
import qiniu.conf
import sys
import os
import qiniu.io
import qiniu.rs
import base64
import Image
from time import strftime,localtime
def getname(name,size):
	name='zq-image:'+name+'-'+size+image[image.find('.'):]
	name=base64.encodestring(name)
	return name
def resize(image):
	img=Image.open(image)
	w,h=img.size
	if(w>1000):
		h=int(1000/float(w)*h)
		w=1000
		h=img.resize((w,h),Image.ANTIALIAS).save(image)


qiniu.conf.ACCESS_KEY="hbpHhfXp27MvRDhgG6aTblX-FQsncR9SUOpSfFTn"
qiniu.conf.SECRET_KEY="pl5-DWcb2O3RLRkjtGj1xX67VfOM6Q2HAlu-iG-7"
while(True):
	image=raw_input("directory")
	resize(image)
	name=strftime("%Y%m%d%H%M%S", localtime())
	policy=qiniu.rs.PutPolicy('zq-image')
	policy.saveKey=name+image[image.find('.'):] 
	policy.persistentOps='imageView2/2/h/80|saveas/'+getname(name,'80')+';imageView2/2/h/160|saveas/'+getname(name,'160')+';imageView2/2/h/320|saveas/'+getname(name,'320')+';imageView2/2/h/640|saveas/'+getname(name,'640')
	uptoken=policy.token()
	extra=qiniu.io.PutExtra()

	ret,err=qiniu.io.put_file(uptoken,None,image,extra)
	if err is  not None:
		sys.stderr.write('error:%s' % err)
	else:
		print 'http://zq-image.qiniudn.com/'+name+image[image.find('.'):]  


