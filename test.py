from n_rex.model import DNN
import numpy as np
import matplotlib.pyplot as plt
import random

# Initialize the model (downloads weights if not present)
model = DNN("dnn-tiny")

# Path to MNIST CSV
csv_file = "mnist/train.csv"

# Pick a random sample
index = random.randint(0, 59999)
all_values = open(csv_file).readlines()[index].split(',')
image_array = np.asarray(all_values[1:], dtype=float).reshape((28,28))

# Show the image
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.title(f"Actual: {all_values[0]}")
plt.show()

# Prepare input and predict
inputs = (image_array.flatten() / 255 * 0.99 + 0.01).reshape(-1,1)
predicted = np.argmax(model.forward(inputs))

print("Predicted:", predicted)
print("Actual:", all_values[0])
