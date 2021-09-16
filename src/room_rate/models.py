from torchvision.models import resnet

class RaterResNet(resnet.ResNet):
    """Resnet with single linear output (instead of classifier output)"""

    def __init__(self, layers=None):
        if layers is None:
            layers = 4*[2,] #resnet18
        super().__init__(resnet.BasicBlock, layers, 1)
