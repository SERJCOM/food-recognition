import torch
import torchvision.models as models
import torch.nn as nn

from food_recognition import tools


class FoodRecognition:
    
    def __init__(self, using_cuda = False) -> None:
        self.model = models.resnet18(weights = models.ResNet18_Weights.IMAGENET1K_V1)
        num_ftrs = self.model.fc.in_features

        # self.classes = ["Seafood", "Fried food", "Vegetable-Fruit", "Meat", "Rice", "Soup", "Dairy product", "Egg", "Bread", "Noodles-Pasta", "Dessery"]
        self.classes = ["sushi", "steak", "rissoto", "pizza"]


        self.model.fc = nn.Linear(num_ftrs, len(self.classes))

        if using_cuda:
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        self.model.load_state_dict(torch.load("assets/net_prototype_92_2604_1.trch", self.device))

        self.model.eval()

        
        self.image_size = (224, 224)
        
    def eval(self, image_path : str) -> tuple:
        img_tensor = tools.create_tensor_from_image_file(image_path, self.device, self.image_size)

        img_tensor = tools.transform_image(img_tensor, self.device)

        img_tensor = img_tensor.unsqueeze(0)

        outputs = self.model(img_tensor)

        _, predicted = torch.max(outputs.data, 1)

        return (self.classes[predicted.item()], predicted.item())
        
    def get_classes(self) -> list:
        return self.classes

