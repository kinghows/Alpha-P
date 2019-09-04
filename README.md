# pic_check
检测手机照片的拍摄时间和地点以及颜值

python 版本：Python 3.7.4rc2

安装：

wxPython
https://wxpython.org/Phoenix/snapshot-builds/
pip install E:\SOFT\Python\windows\wxPython-4.1.0a1.dev4250+34521dc1-cp37-cp37m-win_amd64.whl

pip install pyinstaller
如果报错，请安装numpy1.16.2
ModuleNotFoundError: No module named 'numpy.random.common'
pip uninstall numpy
pip install numpy==1.16.2

打包成一个exe文件：
pyinstaller -F pic_check.py