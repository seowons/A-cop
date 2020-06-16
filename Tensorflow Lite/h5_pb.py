#h5 -> pb

from tensorflow import keras
model = keras.models.load_model('acop2.h5', compile=False)

export_path = 'save'
model.save(export_path, save_format="tf")
