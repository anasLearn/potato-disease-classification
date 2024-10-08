*Created with the help of ChatGPT*
# Training the Neural Network

## Data Extraction and Preparation

The first crucial step in training our neural network is to obtain and prepare the dataset. We accomplished this using TensorFlow, a powerful deep learning framework. This section outlines the process we followed:

### Data Extraction with TensorFlow

We used TensorFlow to extract and load the dataset. TensorFlow provides versatile tools for handling various data sources, making it an excellent choice for this task. For a detailed explanation of the data extraction process, please refer to the following YouTube video: [Data Extraction Tutorial](https://youtu.be/VFEOskzhhbc).

### Data Visualization

Before diving into training, it's essential to have a visual understanding of our data. We created visualizations to explore a sample of the images from the dataset. This helped us gain insights into the characteristics of the data.

### Data Splitting

To facilitate training and evaluation, we split our dataset into three distinct sets:

1. **Training Set:** This set comprises a significant portion of the data and is used to train the neural network. It is the foundation for the model's learning.

2. **Cross Validation Set:** This set is reserved for fine-tuning our model and validating its performance during the training process. It helps us prevent overfitting and assess generalization.

3. **Test Set:** The test set is used to assess the final performance of our trained neural network. It provides an unbiased evaluation of how well the model can generalize to unseen data.

By carefully splitting the data into these three sets, we ensure that our neural network is trained effectively and can perform well on unseen examples.

## Data Preprocessing

The next crucial step in our training process is data preprocessing. This step is essential for ensuring that the data is in a suitable format for training the neural network. Here's an overview of the data preprocessing steps we performed:

### 1. Prefetching and Caching

To optimize data loading during training, we implemented prefetching and caching. This technique helps minimize data pipeline bottlenecks and improves training efficiency. For a detailed explanation of prefetching and caching, please refer to the following YouTube video: [Prefetching and Caching Tutorial](https://youtu.be/MLEKEplgCas).

### 2. Resizing and Rescaling

We resized and rescaled the data to a consistent size and range. This ensures that all input data has the same dimensions and numerical characteristics, making it compatible with our neural network architecture.

### 3. Data Augmentation

Data augmentation is a powerful technique for increasing the diversity of the training dataset by applying various transformations to the data. This helps improve the model's robustness and generalization. For a detailed explanation of data augmentation principles, please refer to the following YouTube video: [Data Augmentation Tutorial](https://youtu.be/mTVf7BN7S8w?si=4etP0rU4kWnFdFsA).

By carefully preprocessing the data using these techniques, we prepare it for effective training, ensuring that our neural network can learn meaningful patterns from the data.

## Training a Convolutional Neural Network (CNN)

To achieve the best results for our task, we utilized a Convolutional Neural Network (CNN). CNNs are a powerful class of neural networks specifically designed for tasks involving images, such as image classification. Here's an overview of our CNN training process:

### Convolutional Neural Network Principles

Before delving into our specific training process, it's crucial to understand the principles behind Convolutional Neural Networks. We recommend watching the following educational videos in this order to gain a solid understanding of CNNs:

1. [CNN Introduction](https://youtu.be/zfiSAzpy9NM)
2. [CNN Architecture](https://youtu.be/7HPwo4wnJeA)
3. [CNN Training](https://youtu.be/oDAPkZ53zKk)

These videos will provide you with a comprehensive foundation in CNNs, which are essential for comprehending our training methodology.

Our CNN training process involved fine-tuning model hyperparameters, optimizing loss functions, and leveraging data augmentation techniques to achieve the best results. The trained CNN is capable of recognizing and classifying the patterns within our dataset accurately.

By employing CNNs and following best practices in training, we ensured our model's effectiveness in solving our specific task.

### Building and Training the Model

The model is built in a way that it contains the follwing layers:
* Preprocessing layers: resize, rescale and data augmentation.
* Convultional Network: Convolutional layer followed by pooling layer, repeated multiple times. Activation function is `relu`.
* Flattening layer: A layer that the output of the convolutional network.
* Dense netowrk: With activation function relu.
* Output layer: A dense network with activation function `softmax` to emulate probability.

#### Example

```Python
input_shape = (BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, CHANNELS)
n_classes = len(class_names)

model = tf.keras.Sequential([
    # Preprocessing
    resize_and_rescale,
    data_augmentation,

    # Convolutional Network
    layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),

    # Flattening the output of the convolutional network
    layers.Flatten(),

    # Dense neural network to make calculations
    layers.Dense(64, activation='relu'),

    # Output layer
    layers.Dense(n_classes, activation='softmax'),
])

model.build(input_shape=input_shape)
```

#### Training the model

The model is trained for a number of epochs (e.g. 50 epochs). After each epoch, the model is validated against the cross validation dataset to improve its accuracy.

### Testing the model

After the training, the model is tested against the test set that was created beforehand and wasn't involved in the training.

### Saving the model

The model can be saved to be deployed later with `model.save()`

### Further evaluation of the model

In the Jupyter notebook [wrong-predictions](./wrong-predictions.ipynb), we calculated the number of images that were incorrectly predicted by a model we load.

We also generated a confusion matrix. And calculated the precision, recall and F1-score.
