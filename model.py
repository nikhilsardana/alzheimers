import torch.nn as nn
import os
import argparse
import torch
import numpy as np
import PIL as Image
from scipy.misc import imresize
import torch.utils.data as data
import torchvision import transforms

from resnet.inceptionresnetv2 import InceptionResNetV2

f = InceptionResNetV2.forward

def forward(self, x):
    x = f(self, x)
    x = self.act(x)
    x = self.last(x)
    return x

InceptionResNetV2.foward = forward

parser = argparse.ArgumentParser()
parser.add_argument("--load_weights", default=None, type=str)
parser.add_argument("-img_dir", default="imgdata/train/", type=str)
args = parser.parse_args()

in_res = InceptionResNetV2()
in_res.act=nn.ReLU(inplace=False)
in_res.last = nn.Linear(1000, 13)


######################################
## Custom data transforms
#####################################

class Scale(object):
    def __call__(self, sample):
        x = imresize(sample['image'], (299,299))
        return {'image':x, 'labels': sample['labels']}

data_transforms = {
    'train': transforms.Compose([
            Scale()
            transforms.toTensor()
            #normalize(mean, std)
    ])
    'test': transforms.Compose([
            Scale()
            transforms.toTensor()
            #normalize(mean, std)
    ])
}


#####################################
## Load Data
#####################################

data_dir = 'imgdata'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                    data_transforms[x]) for x in ['train', 'test']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                    shuffle=True, num_workers=4) for x in ['train', 'test']}
dataset_sizes= {x: len(image_datasets[x]) for x in ['train', 'test']}
classnames = image_datasets['train'].classes

use_gpu = torch.cuda.is_available()

####################################
## End Data Loading
####################################


####################################
## Train Model
####################################
def train_model(model, criterion, optimizer, scheduler, num_epochs=10):



if args.load_weights:
    print("Loaded weights from {}".format(args.load_weights))
    in_res.load_weights(args.load_weights)



def train

