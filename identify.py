import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model('image_classifier/imageclassifier.keras')

def identify(uploaded_file):
    image = Image.open(uploaded_file)

    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        alpha = image.split()[-1]
        bg = Image.new("RGB", image.size, (255, 255, 255))
        bg.paste(image, mask=alpha)
        image = bg

    image = ImageOps.grayscale(image)
    image = ImageOps.invert(image)

    image = image.resize((28, 28), Image.Resampling.LANCZOS)

    image_array = img_to_array(image) / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)

    predictions = tf.nn.softmax(predictions).numpy()

    return np.argmax(predictions)