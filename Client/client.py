import requests
import cv2


def predict_result(img, ipconf):
    img = cv2.resize(img, (1280, 720))
    payload = {'image': img.tostring()}

    # Submit the request.
    # PyTorch_REST_API_URL = 'http://172.18.242.221:7878/predict'
    PyTorch_REST_API_URL = ipconf
    r = requests.post(PyTorch_REST_API_URL, files=payload).json()

    # Ensure the request was successful.
    if r['success']:
        res = r['result']
        return res
    else:
        print('Request failed')

    return 0

class Wire(object):
    def __init__(self, ipconf):
        self.Q = 0
        self.ipconf = ipconf
    
    def process(self, img):
        self.Q = predict_result(img, self.ipconf)
