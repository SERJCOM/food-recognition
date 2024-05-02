import torch
import cv2

def transform_image(image_tensor : torch.Tensor, device : torch.device) -> torch.Tensor:
    img_tensor = image_tensor.to(device)
    img_tensor = img_tensor.float()
    img_tensor = img_tensor / 255
    img_tensor = img_tensor.permute(2, 0, 1)

    return img_tensor

def create_tensor_from_image_file(img_path : str, device : torch.device, img_size : tuple) -> torch.Tensor:
    img = cv2.imread(img_path)
    img_dim = img_size
    img = cv2.resize(img, img_dim)
    img_tensor = torch.from_numpy(img)
    img_tensor = img_tensor.to(device)

    return img_tensor

def create_tensor_from_image(img, device : torch.device, img_size : tuple) -> torch.Tensor:
    img = cv2.imread(img_path)
    img_dim = img_size
    img = cv2.resize(img, img_dim)
    img_tensor = torch.from_numpy(img)
    img_tensor = img_tensor.to(device)

    return img_tensor

    # return transform_image(img_tensor, device)


