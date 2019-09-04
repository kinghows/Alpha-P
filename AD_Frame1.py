#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.adv
import os
import random
import time
from PIL import Image
import math
import hashlib
import urllib.parse
from urllib.parse import urlencode
import urllib.response
from urllib.request import urlopen
import base64
import json
import requests  
import cv2
import numpy as np
import exifread
from decimal import Decimal
from position_utils import *
import datetime

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, 
 wxID_FRAME1BEAUTY, 
 wxID_FRAME1BTN_CLEAR, 
 wxID_FRAME1BTN_TEST_BEAUTY, 
 wxID_FRAME1BTN_TEST_POSION, 
 wxID_FRAME1GENERICDIRCTRL1,
 wxID_FRAME1PANEL1,
 wxID_FRAME1SASHLAYOUTWINDOW1, 
 wxID_FRAME1TEXTRETURN, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(438, 55), size=wx.Size(873, 704),
              style=wx.DEFAULT_FRAME_STYLE, title=u'pic_check')
        self.SetClientSize(wx.Size(857, 665))
        self.Bind(wx.EVT_SIZE, self.OnFrame1Size)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(392, -8), size=wx.Size(463, 664),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetMinSize(wx.Size(455, 778))

        self.sashLayoutWindow1 = wx.adv.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(392, 664), style=wx.CLIP_CHILDREN|wx.adv.SW_3D)
        self.sashLayoutWindow1.SetAlignment(wx.adv.LAYOUT_LEFT)
        self.sashLayoutWindow1.SetOrientation(wx.adv.LAYOUT_VERTICAL)
        self.sashLayoutWindow1.SetSashVisible(wx.adv.SASH_RIGHT, True)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(392, 664))
        self.sashLayoutWindow1.Bind(wx.adv.EVT_SASH_DRAGGED,
              self.OnSashLayoutWindow1SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW1)

        self.textReturn = wx.TextCtrl(id=wxID_FRAME1TEXTRETURN,
              name=u'textReturn', parent=self.panel1, pos=wx.Point(104, 0),
              size=wx.Size(1110, 1050), style=wx.TE_MULTILINE, value='')

        self.genericDirCtrl1 = wx.GenericDirCtrl(defaultFilter=0, dir='.',
              filter=u'Fichier png(*.png,*.jpg)|*.png;*.jpg',
              id=wxID_FRAME1GENERICDIRCTRL1, name='genericDirCtrl1',
              parent=self.sashLayoutWindow1, pos=wx.Point(0, 0),
              size=wx.Size(392, 664),
              style=wx.DIRCTRL_3D_INTERNAL | wx.SUNKEN_BORDER)
        self.genericDirCtrl1.SetMinSize(wx.Size(270, 664))
        self.genericDirCtrl1.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSel)

        self.btn_test_posion = wx.Button(id=wxID_FRAME1BTN_TEST_POSION,
              label=u'\u4f4d\u7f6e\u68c0\u6d4b', name=u'btn_test_posion',
              parent=self.panel1, pos=wx.Point(16, 116), size=wx.Size(75, 24),
              style=0)
        self.btn_test_posion.Bind(wx.EVT_BUTTON, self.Onbtn_test_posionButton,
              id=wxID_FRAME1BTN_TEST_POSION)

        self.btn_test_beauty = wx.Button(id=wxID_FRAME1BTN_TEST_BEAUTY,
              label=u'\u989c\u503c\u68c0\u6d4b', name=u'btn_test_beauty',
              parent=self.panel1, pos=wx.Point(16, 176), size=wx.Size(75, 24),
              style=0)
        self.btn_test_beauty.Bind(wx.EVT_BUTTON, self.Onbtn_test_beautyButton,
              id=wxID_FRAME1BTN_TEST_BEAUTY)

        self.btn_clear = wx.Button(id=wxID_FRAME1BTN_CLEAR,
              label=u'\u6e05\u7a7a\u7ed3\u679c', name=u'btn_clear',
              parent=self.panel1, pos=wx.Point(16, 236), size=wx.Size(75, 24),
              style=0)
        self.btn_clear.Bind(wx.EVT_BUTTON, self.Onbtn_clearButton,
              id=wxID_FRAME1BTN_CLEAR)



    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FileName=None
        self.gender =0

    def checkStatusRange(self, event):
        return event.GetDragStatus() != wx.SASH_STATUS_OUT_OF_RANGE

    def doLayout(self):
        wx.adv.LayoutAlgorithm().LayoutWindow(self, self.panel1)
        self.panel1.Refresh()
        
    def OnWxframe1Size(self, event):
        self.doLayout()

    def OnSashLayoutWindow1SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnSashLayoutWindow2SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow2.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()
        event.Skip()

    def OnFrame1Size(self, event):
        self.doLayout()
        event.Skip()

        
    def OnSel(self, event):
        self.FileName = self.genericDirCtrl1.GetFilePath()
        
    def Onbtn_clearButton(self, event):
        self.textReturn.Clear()
        event.Skip()

    def get_address(self, location):
        api_key = "516453e417b50bcf6716040c234b6c1f"
        url_get_position = 'https://restapi.amap.com/v3/geocode/regeo?key={}&location={}'
        resp = requests.get(url_get_position.format(api_key, location))
        location_data = json.loads(resp.text)
        address = location_data.get('regeocode').get('formatted_address')
        return address

    def format_lati_long_data(self, data):
        data_list_tmp = str(data).replace('[', '').replace(']', '').split(',')
        data_list = [data.strip() for data in data_list_tmp]
        data_tmp = data_list[-1].split('/')
        data_sec = int(data_tmp[0]) / int(data_tmp[1]) / 3600
        data_tmp = data_list[-2]
        data_minute = int(data_tmp) / 60
        data_degree = int(data_list[0])
        result = "%.6f" % (data_degree + data_minute + data_sec)
        return float(result)

    def get_image_ability(self,img):
        img_exif = exifread.process_file(open(img, 'rb'))

        if img_exif:
            latitude_gps = img_exif['GPS GPSLatitude']
            latitude_direction = img_exif['GPS GPSLatitudeRef']
            longitude_gps = img_exif['GPS GPSLongitude']
            longitude_direction = img_exif['GPS GPSLongitudeRef']
            take_time = img_exif['EXIF DateTimeOriginal']
            format_time = str(take_time).split(" ")[0].replace(":", "-")
            self.textReturn.AppendText('date     : '+ format_time+'\n')

            if latitude_gps and longitude_gps and take_time:
                latitude = self.format_lati_long_data(latitude_gps)
                longitude = self.format_lati_long_data(longitude_gps)
                location = wgs84togcj02(longitude, latitude)

                return f'{location[0]},{location[1]}'
            else:
                self.textReturn.AppendText('图片属性不完整。\n')
                return ''
        else:
            self.textReturn.AppendText('图片不是原图。\n')
            return ''

    def location(self, img):
        coordinate = self.get_image_ability(img)
        if not coordinate:
            return
        address = self.get_address(coordinate)
        self.textReturn.AppendText('address:'+ address+'\n')

    def Onbtn_test_posionButton(self, event):
        if os.path.isfile(self.FileName):
            self.textReturn.AppendText(self.FileName+'\n')
            self.location(self.FileName)

        event.Skip()	
	
    def get_params(self,img):                        
        params = {'app_id':'1106941552',              
                  'image':img,                  
                  'mode':'0' ,                    
                  'time_stamp':str(int(time.time())),       
                  'nonce_str':str(int(time.time())),         
                 }

        sort_dict= sorted(params.items(), key=lambda item:item[0], reverse = False)  
        sort_dict.append(('app_key','ecTptvOyErjHiNgo'))   
        rawtext= urlencode(sort_dict).encode()  
        sha = hashlib.md5()    
        sha.update(rawtext)
        md5text= sha.hexdigest().upper()        
        params['sign']=md5text                  
        return  params                         

    def resize_image(self, origin_img, optimize_img, threshold):
        with Image.open(origin_img) as im:
            width, height = im.size
            file_size =  width*height
            if file_size > threshold:
 
                if width >= height:
                    new_width = int(math.sqrt(threshold / 2))
                    new_height = int(new_width * height * 1.0 / width)
                else:
                    new_height = int(math.sqrt(threshold / 2))
                    new_width = int(new_height * width * 1.0 / height)

                resized_im = im.resize((new_width, new_height))
                resized_im.save(optimize_img)
            else:
                im.save(optimize_img)    

    def Onbtn_test_beautyButton(self, event):
        if os.path.isfile(self.FileName):
            self.textReturn.AppendText(self.FileName+'\n')
            
            self.resize_image(self.FileName, 'optimized.jpg', 1024*1024)
            
            frame=cv2.imread('optimized.jpg')
            nparry_encode = cv2.imencode('.jpg', frame)[1]
            data_encode = np.array(nparry_encode)
            img = base64.b64encode(data_encode)   

            params = self.get_params(img)    

            url = "https://api.ai.qq.com/fcgi-bin/face/face_detectface"
            res = requests.post(url,params).json()
            if res['ret'] == 0:
                for face in res['data']['face_list']:
                    #print(face)
                    x=face['x']
                    y=face['y']
                    w=face['width']
                    h=face['height']
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
                    cv2.putText(frame,'age   :'+str(face['age']), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2,cv2.LINE_8, 0)
                    cv2.putText(frame,'beauty:'+str(face['beauty']), (x, y+h+40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2,cv2.LINE_8, 0)
                    self.textReturn.AppendText('face_id: '+ str(face['face_id'])+'\n')
                    self.textReturn.AppendText('gender: '+ str(face['gender'])+'\n')
                    self.textReturn.AppendText('age     : '+ str(face['age'])+'\n')
                    self.textReturn.AppendText('beauty : '+ str(face['beauty'])+'\n')
                    self.textReturn.AppendText('smile   : '+ str(face['expression'])+'\n')
				
                cv2.imshow('img',frame)
                cv2.imwrite('optimized.jpg',frame)
                cv2.waitKey(0)
            else:
                self.textReturn.AppendText('no face\n')
            
        event.Skip()


