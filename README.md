# 结印世界(Hand-Sign-World)
(本repo用于保存深度学习课程大作业的成果，包括实现代码以及最终展示海报)

本项目使用了Background Matting Model模型用于实时背景替换，以及EfficientDet-D0模型用于手势识别。通过结合这些模型我们完成了一个可以通过玩家手势实时抠图并进行背景更换的小游戏，效果如下所示。

<img src="./demo.gif"/>

## 项目构成

* UI 界面以及 Background Matting Model 模型部署于本地，详见目录 Client
* EfficientDet-D0 模型部署于服务器，详见目录 Server

## 环境要求

客户端

* Python 3.8
* PyQt5
* opencv-python

服务端

* Python 3.8
* TensorFlow 2.3.0
* Flask 2.0.1
* opencv-python
* GPU 显存至少 11G

## 运行方法

首先根据具体情况修改 Client/GUI.py 文件中的第20行，将其中的 IP 地址改为服务器地址。

```python
ipconf = 'http://172.18.242.221:7878/predict'
```

在本地运行 Client/GUI.py 文件。

然后修改 Server/server.py 文件中的第10行，设置要使用的 GPU 编号。

```python
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```

在服务器运行 Server/server.py 文件。