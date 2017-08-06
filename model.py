import csv
import cv2
import numpy as np

lines =[]
with open('./video_data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
measurements = []
for line in lines:
    source_path = line[0]
    filename = source_path.spli('/')[-1]
    current_path = 'video_data/IMG/' + filename
    image = cv2.imread(current_path)
    measurement = float(line[3])
    measurements.append(measurement)


from keras.models import Sequential
from keras.layers import Flatten, Dense

X_train = np.array(images)
y_train = np.array(measurements)

model = Sequential()
model.add(Flatten(input_shape=(160,320,3)))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True)

# Save the model
model.save('model.h5')
