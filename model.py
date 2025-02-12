import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model('skin_cancer_model_VGG16_v1.h5')
    return model