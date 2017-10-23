import torch.nn as nn
import os
import argparse
import torch
import numpy as np
import PIL as Image
from scipy.misc import imresize
import torch.utils.data as data
import torchvision 
import transforms
import meter

from resnet.inceptionresnetv2 import InceptionResNetV2

parser = argparse.ArgumentParser()
parser.add_argument("--load_weights", default='imagenet', type=str)
parser.add_argument("-img_dir", default="../imgdata/train/", type=str)
args = parser.parse_args()

model = InceptionResNetV2(pretrained=True)
num_ftrs = model.classif.in_features
model.classif = nn.Linear(num_fts, 5)


######################################
## Custom data transforms
#####################################


data_transforms = {
    'train': transforms.Compose([
            Scale(299)
            ToTensor()
            normalize([0.122,0.122,0.122], [0.250,0.250,0.250])
    ])
    'test': transforms.Compose([
            Scale(299)
            ToTensor()
            normalize([0.122,0.122,0.122], [0.250,0.250,0.250])
    ])
}


#####################################
## Load Data
#####################################

data_dir = '../imgdata'
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

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    if use_gpu:
        model = nn.DataParallel(model, device_ids=[0,1,2,3]).cuda()

    best_model_wts = model.state_dict()
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)
        confusion_matrix = meter.ConfusionMeter(5) #I have 5 classes here
        # Each epoch has a training and validation phase
        for phase in ['train', 'test']:
            if phase == 'train':
                scheduler.step()
                model.train(True)  # Set model to training mode
            else:
                model.train(False)  # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for data in dataloaders[phase]:
                # get the inputs
                inputs, labels = data

                # wrap them in Variable
                if use_gpu:
                    inputs = Variable(inputs.cuda())
                    labels = Variable(labels.cuda())
                else:
                    inputs, labels = Variable(inputs), Variable(labels)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                outputs = model(inputs)

                if phase == 'test':
                    confusion_matrix.add(outputs.data.squeeze())
                    print confusion_matrix.conf

                _, preds = torch.max(outputs.data, 1)
                loss = criterion(outputs, labels)

                # backward + optimize only if in training phase
                if phase == 'train':
                    loss.backward()
                    optimizer.step()

                # statistics
                running_loss += loss.data[0]
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'test' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = model.state_dict()

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model

if args.load_weights:
    print("Loaded weights from {}".format(args.load_weights))
    in_res.load_weights(args.load_weights)


opt = optim.SGD(model.parameters(), lr=0.001, momentum=0.5)
criterion = nn.CrossEntropyLoss()
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)
model = train_model(model, criterion, optimizer_ft, exp_lr_scheduler, num_epochs=5)
