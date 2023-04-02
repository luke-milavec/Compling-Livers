import numpy as np
import config
import os
import torch
from random import randrange
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from torchvision.utils import save_image


class MapDataset(Dataset):
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.list_files = os.listdir(self.root_dir)

    def __len__(self):
        return len(self.list_files)

    def __getitem__(self, index):
        img_file = self.list_files[index]
        img_path = os.path.join(self.root_dir, img_file)
        image = np.array(Image.open(img_path))
        convert_tensor = transforms.ToTensor()
        xi = randrange(934) +256
        yi = randrange(421) +256
        input_image = image[yi:yi + 512, xi:xi+512, :]
        xi -= 128
        yi -= 128
        target_image = image[yi:yi+256, 1446+xi:xi+1446+256, :]

        augmentations = config.both_transform(image=input_image, image0=target_image)
        input_image = augmentations["image"]
        target_image = augmentations["image0"]
        input_image  = convert_tensor(input_image)
        target_image = convert_tensor(target_image)
        return input_image, target_image


if __name__ == "__main__":
    dataset = MapDataset("data/train/")
    loader = DataLoader(dataset, batch_size=None)
    for x, y in loader:
        
        save_image(x,"x.png")
        save_image(y,"y.png")
        import sys

        sys.exit()