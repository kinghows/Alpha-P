# Alpha-P
检测手机照片的拍摄时间和地点以及颜值.（检测拍摄地点必须使用开了手机定位的原图。）

人脸识别采用腾讯：[人脸识别 API](http://ai.qq.com/)

地图定位采用高德：[Web服务API](https://lbs.amap.com/api/webservice/summary/)

example:

![example](https://github.com/kinghows/pic_check/edit/master/optimized.jpg)

python 版本：Python 3.7.4rc2

开发安装：

wxPython:

https://wxpython.org/Phoenix/snapshot-builds/

pip install E:\SOFT\Python\windows\wxPython-4.1.0a1.dev4250+34521dc1-cp37-cp37m-win_amd64.whl

pip install pyinstaller

如果报错，请安装numpy1.16.2

ModuleNotFoundError: No module named 'numpy.random.common'

pip uninstall numpy

pip install numpy==1.16.2

打包成一个exe文件：

pyinstaller -F Alpha-P.py

## 好玩的Alpha系列，喜欢的打颗星：

- [Alpha-12306：买个票](https://github.com/kinghows/Alpha-12306)

- [Alpha-B：下载关注的最新B站视频](https://github.com/kinghows/Alpha-B)

- [Alpha-C：智能闲聊](https://github.com/kinghows/Alpha-C)

- [Alpha-D：人工智能刷抖音](https://github.com/kinghows/Alpha-D)

- [Alpha-J：微信跳一跳python玩法](https://github.com/kinghows/Alpha-J)

- [Alpha-A：量化投资--一个全栈实验项目](https://github.com/kinghows/Alpha-A)
