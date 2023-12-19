from PIL import Image
import numpy as np
import torch
from scipy.special import softmax
import torchvision
import torchvision.transforms as transforms
from torchvision import models
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim


def execute_model_p1(model_path, image_path):
    images = preprocess_image_p1(image_path)

    model = models.resnet50(pretrained=False)
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 18)

    if not torch.cuda.is_available():
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    else:
        model.load_state_dict(torch.load(model_path))

    model.eval()

    outputs = []
    for image in images:
        batch = torch.unsqueeze(image, 0)

        with torch.no_grad():
            output = model(batch)
        output_np = output.numpy()
        outputs.append(softmax(output_np))

    avg_predictions = np.mean(outputs, axis=0)
    print(avg_predictions)
    predicted = np.argmax(avg_predictions)
    max_prob = np.max(avg_predictions)
    return predicted, avg_predictions, max_prob

def execute_model_p2(model_path, image_path):
    image = preprocess_image_p2(image_path)
    batch = torch.unsqueeze(image, 0)

    model = models.resnet50(pretrained=False)
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 18)

    if not torch.cuda.is_available():
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    else:
        model.load_state_dict(torch.load(model_path))

    model.eval()

    with torch.no_grad():
        output = model(batch)

    _, predicted = torch.max(output, 1)
    predicted = predicted.item()
    probs = softmax(output)
    max_prob = np.max(probs)

    return predicted, probs, max_prob

def preprocess_image_p1(image_path):
    images_squared = resize_and_crop(image_path)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        # zmienic jesli model trenowany od zera
    ])

    images = [transform(image_squared) for image_squared in images_squared]
    return images


def preprocess_image_p2(image_path):
    image_squared = pad_image_to_square(image_path)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        # zmienic jesli model trenowany od zera
    ])

    image = transform(image_squared)
    return image


def resize_and_crop(image_path):
    """
    Generates and saves overlapping 224x224 cropped images from a given image.
    """

    # Load the image
    image = Image.open(image_path)

    if image.width < 224 or image.height < 224:
        return None

    # Resize the image such that the smaller dimension is 224
    aspect_ratio = image.width / image.height
    if aspect_ratio > 1:
        # Image is wider than tall
        new_height = 224
        new_width = int(aspect_ratio * new_height)
    else:
        # Image is taller than wide
        new_width = 224
        new_height = int(new_width / aspect_ratio)

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    if new_height == new_width:
        return [resized_image]

    # Determine number of crops along the longer dimension and calculate the overlap
    longer_dimension_size = max(new_width, new_height)
    num_crops = longer_dimension_size // 224
    if longer_dimension_size % 224 != 0:
        num_crops += 1

    # Calculate the overlap to evenly distribute the remaining space
    total_overlap = (224 * num_crops) - longer_dimension_size
    overlap_per_image = total_overlap // (num_crops - 1)

    # Generate and save the overlapping 224x224 images
    cropped_images = []
    for i in range(num_crops):
        if new_width >= new_height:
            # Overlapping images along the width
            left = max(i * 224 - i * overlap_per_image, 0)
            upper = 0
            right = left + 224
            lower = 224
        else:
            # Overlapping images along the height
            left = 0
            upper = max(i * 224 - i * overlap_per_image, 0)
            right = 224
            lower = upper + 224

        # Ensure we don't go beyond the image boundary
        if right > new_width:
            right = new_width
            left = new_width - 224
        if lower > new_height:
            lower = new_height
            upper = new_height - 224

        # Crop the image to create the overlapping 224x224 images
        cropped_image = resized_image.crop((left, upper, right, lower))
        cropped_images.append(cropped_image)

    return cropped_images


def pad_image_to_square(image_path, target_size=(224, 224)):
    # Open the image
    image = Image.open(image_path)

    if image.size[0] < 224 or image.size[1] < 224:
        raise ValueError("Image too small")

    # Determine the desired size for the square image
    max_dim = max(image.size)
    new_size = (max_dim, max_dim)

    # Create a new square image with black background
    squared_image = Image.new("RGB", new_size, (0, 0, 0))

    # Calculate the position to paste the original image
    paste_x = (max_dim - image.width) // 2
    paste_y = (max_dim - image.height) // 2

    # Paste the original image onto the square canvas
    squared_image.paste(image, (paste_x, paste_y))

    squared_image = squared_image.resize(target_size, Image.Resampling.LANCZOS)

    return squared_image