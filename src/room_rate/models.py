'''Models to use as room raters'''
from torchvision import models
from torch import nn

class RegressionResNet(models.resnet.ResNet):
    """Resnet with single linear output (instead of classifier output)"""

    def __init__(self, layers=None):
        if layers is None:
            layers = 4*[2,] #resnet18
        super().__init__(models.resnet.BasicBlock, layers, 1) #1 output

#Below is lightly modified code from on finetuning vision models from:
#https://pytorch.org/tutorials/beginner/finetuning_torchvision_models_tutorial.html
def set_parameter_requires_grad(model, feature_extracting):
    '''
    if feature_extracting, turn off parameter updating
    for parameters currently in model
    '''
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

def get_resnet(num_classes=1,
               use_pretrained=True,
               feature_extract=True):
    '''
    Get a resnet18 with num_classes output classes
    use_pretrained uses pytorch pretrained model except last layer
    if feature_extract, only parameters in the last layer are updated
    '''
    model_ft = models.resnet18(pretrained=use_pretrained)
    set_parameter_requires_grad(model_ft, feature_extract)
    num_ftrs = model_ft.fc.in_features
    model_ft.fc = nn.Linear(num_ftrs, num_classes)
    return model_ft
