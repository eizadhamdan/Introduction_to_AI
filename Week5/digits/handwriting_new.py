import sys
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, AveragePooling2D


# Use MNIST handwriting dataset
mnist = tf.keras.datasets.mnist

# Prepare data for training
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
# dividing by 255 to put the values in a 0 - 1 range so that it is easy to train our model

y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)
x_train = x_train.reshape(
    x_train.shape[0], x_train.shape[1], x_train.shape[2], 1
)
x_test = x_test.reshape(
    x_test.shape[0], x_test.shape[1], x_test.shape[2], 1
)

# Create a convolutional neural network
model = Sequential([
    # Convolutional Layer 1
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),  # 6 filters, 5x5 kernel
    AveragePooling2D(pool_size=(2, 2)),  # Average pooling

    # Convolutional Layer 2
    Conv2D(64, kernel_size=(3, 3), activation='relu'),  # 16 filters, 5x5 kernel
    AveragePooling2D(pool_size=(2, 2)),  # Average pooling

    # Flattening the output
    Flatten(),

    # Fully Connected Layer 1
    Dense(120, activation='relu'),  # 120 neurons

    # Fully Connected Layer 2
    Dense(84, activation='relu'),  # 84 neurons

    # Output Layer
    Dense(10, activation='softmax')  # 10 classes for digits 0-9
])

# Train neural network
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
model.fit(x_train, y_train, epochs=50, verbose=1)

# Evaluate neural network performance
model.evaluate(x_test,  y_test, verbose=2)

# Save model to file
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
#     model.save(filename)
#     print(f"Model saved to {filename}.")

filename = "digits_model.h5"
model.save(filename)
print(f"Model saved to {filename}.")
