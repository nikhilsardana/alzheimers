import numpy as np
import os
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.core import Flatten
from keras.callbacks import ModelCheckpoint
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from sklearn.metrics import classification_report
import mxnet as mx
import argparse


train_data_dir = os.getcwd() + "/../imgdata/train"
validation_data_dir = os.getcwd() + "/../imgdata/test"

nb_train_samples = 2029440
nb_validation_samples = 678720
epochs = 5
batch_per_gpu = 64
num_gpus = 4
batch_size = num_gpus * batch_per_gpu

train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(299, 299),
        batch_size=batch_size,
        shuffle = True,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(299, 299),
        batch_size=batch_size,
        class_mode='categorical')


model = InceptionResNetV2(include_top=True, weights=None, classes=5)

#categorical classifier


def backend_agnostic_compile(model, loss, optimizer, metrics, args):
    if keras.backend._backend == 'mxnet':
        gpu_list = ["gpu(%d)" % i for i in range(num_gpus)]
        model.compile(loss=loss,
            optimizer=optimizer,
            metrics=metrics, 
            context = gpu_list)
    else:
        if num_gpus > 1:
            print("Warning: num_gpus > 1 but not using MxNet backend")
        model.compile(loss=loss,
            optimizer=optimizer,
            metrics=metrics)

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

backend_agnostic_compile(
    model=model, loss='categorical_crossentropy', 
    optimizer=sgd, metrics=['accuracy'], args=args)

filepath="weight-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        callbacks = callbacks_list,
        validation_data=validation_generator,
        validation_steps=nb_validation_samples // batch_size)

model.save_weights('incresv2_model.h5')

predictions = model.predict_generator(validation_generator, steps=678720//32)
print(predictions)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = validation_generator.classes
class_labels = list(validation_generator.class_indices.keys())
print(class_labels)
report = classification_report(true_classes, predicted_classes, target_names=class_labels)
print(report)

#score = model.evaluate(x_test, y_test, batch_size)
