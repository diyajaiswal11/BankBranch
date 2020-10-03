import keras
from keras.preprocessing import image
import numpy as np

model=keras.models.load_model('./model.h5')


def predict(img_path):
    img=image.load_img(img_path,target_size=(299,299))
    img=image.img_to_array(img)/255
    img=img.reshape(1,299,299,3)
    out = model.predict_proba(img)
    prob=np.max(out)
    return prob * 100
