import cv2 as cv
import numpy as np
import socket
import os
import flask
import threading
import tensorflow as tf

array_size = (720, 1280, 3)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
app = flask.Flask(__name__)
model_path = './model/EfficientDetD0/saved_model'
loaded_model = tf.saved_model.load(model_path)
DEFAULT_FUNCTION_KEY = 'serving_default'
model = loaded_model.signatures[DEFAULT_FUNCTION_KEY]
print('load model successfully!')

def run_inference_single_image(image, inference_func):
    tensor = tf.convert_to_tensor(image)
    output = inference_func(tensor)
    output['num_detections'] = int(output['num_detections'][0])
    output['detection_classes'] = output['detection_classes'][0].numpy()
    output['detection_boxes'] = output['detection_boxes'][0].numpy()
    output['detection_scores'] = output['detection_scores'][0].numpy()
    return output


@app.route("/predict", methods=["POST"])
def predict():
    print('receive a request')
    # Initialize the data dictionary that will be returned from the view.
    data = {"success": False}

    # Ensure an image was properly uploaded to our endpoint.
    if flask.request.method == 'POST':
        if flask.request.files.get("image"):
            score_th = 0.35
            image = flask.request.files["image"].read()
            img = np.frombuffer(image, dtype=np.uint8)
            decimg = img.reshape(array_size)
            # decimg = cv.imdecode(img, cv.IMREAD_COLOR)

            frame = decimg[:, :, [2, 1, 0]]  # BGR2RGB
            image_np_expanded = np.expand_dims(frame, axis=0)
            output = run_inference_single_image(image_np_expanded, model)
            score = output['detection_scores'][0]
            class_id = output['detection_classes'][0].astype(np.int)
            print(score)
            if score < score_th:
                class_id = 15

            data['result'] = int(class_id)
            data["success"] = True

    # Return the data dictionary as a JSON response.
    return flask.jsonify(data)


app.run(host='0.0.0.0', port=7878, threaded=True)
