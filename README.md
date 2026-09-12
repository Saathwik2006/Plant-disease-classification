# Plant Disease Classification using CNN & Transfer Learning

An image classification project for detecting plant diseases from leaf images using a custom Convolutional Neural Network (CNN) and transfer learning with a pretrained ResNet model.

The project compares a CNN trained for the task with a pretrained ResNet-based approach and explores fine-tuning to adapt learned visual features to the PlantVillage dataset.

---

## Project Overview

Plant diseases can significantly affect crop yield and agricultural productivity. Automated image-based disease classification can assist in identifying diseases from visible symptoms on plant leaves.

In this project, a deep learning pipeline was developed to classify plant leaf images into healthy and diseased categories.

The project follows three main stages:

1. **CNN Baseline** – Train a CNN model specifically for the PlantVillage dataset.
2. **Transfer Learning** – Use a pretrained ResNet model to leverage features learned from large-scale image datasets.
3. **Fine-Tuning** – Unfreeze deeper layers of the pretrained network and adapt the learned visual features to plant disease classification.

---

## Dataset

### PlantVillage Dataset

The project uses the **PlantVillage dataset**, a large collection of labeled plant leaf images.

- **~54,000 images**
- **38 classes**
- **14 crop types**
- Healthy and diseased leaf categories
- Multi-class image classification problem

The dataset contains images of crops such as:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Peach
- Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

---

## Approach

### 1. Image Preprocessing

The input images are prepared before being passed to the models.

The preprocessing pipeline includes:

- Image resizing
- Pixel normalization
- Batch-based data loading
- Data augmentation
- Training/validation data preparation

Data augmentation is used to introduce variations in the training images and improve the model's ability to generalize.

---

### 2. CNN Baseline

A CNN model is trained from scratch as the baseline approach.

The CNN learns visual features directly from the plant leaf images, including patterns associated with:

- Leaf structure
- Spots
- Discoloration
- Lesions
- Texture
- Disease-specific visual patterns

The baseline provides a reference point for evaluating the benefits of transfer learning.

---

### 3. Transfer Learning with ResNet

A pretrained **ResNet** architecture is used to take advantage of visual features learned from a large image dataset.

Instead of training the entire network from scratch:

- A pretrained ResNet is loaded.
- The original classification head is replaced.
- The new classification head is adapted for the 38 PlantVillage classes.
- The classification head is trained on the plant disease dataset.

This allows the model to reuse useful low-level and high-level visual representations learned during pretraining.

---

### 4. Fine-Tuning

After training the new classification head, deeper layers of the pretrained ResNet model are unfrozen.

The model is then fine-tuned on the PlantVillage dataset to allow the learned visual representations to adapt specifically to plant leaf characteristics.

The fine-tuning stage helps bridge the difference between the original pretrained image domain and the plant disease classification task.

---

## Model Comparison

The project evaluates the progression from a model trained specifically for the task to a pretrained and fine-tuned model:

| Model | Training Strategy |
|---|---|
| CNN | Trained from scratch |
| ResNet | Transfer learning with pretrained weights |
| Fine-Tuned ResNet | Transfer learning + fine-tuning |

The models can be compared using classification performance on the validation/test data.

---

## Technologies Used

- **Python**
- **PyTorch / TensorFlow**
- **Keras**
- **NumPy**
- **CNN**
- **ResNet**
- **Transfer Learning**
- **Fine-Tuning**
- **Image Augmentation**
- **PlantVillage Dataset**

---

## Project Pipeline

```text
PlantVillage Dataset
        │
        ▼
Image Preprocessing
        │
        ├── Resizing
        ├── Normalization
        └── Data Augmentation
        │
        ▼
   ┌───────────────┐
   │  CNN Baseline │
   └───────┬───────┘
           │
           ▼
      Evaluation
           
           +

   ┌──────────────────────┐
   │ Pretrained ResNet    │
   └──────────┬───────────┘
              │
              ▼
       Train Classifier
              │
              ▼
         Fine-Tuning
              │
              ▼
          Evaluation
