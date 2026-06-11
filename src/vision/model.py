import torch.nn as nn
from torchvision import models
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import NUM_CLASSES

class EfficientNet(nn.Module):
    def __init__(self):
        super().__init__()
        backbone = models.efficientnet_b0(weights=None)
        in_features = backbone.classifier[1].in_features
        backbone.classifier = nn.Identity()
        self.backbone = backbone
        self.head = nn.Sequential(
            nn.Linear(in_features, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, NUM_CLASSES),
        )

    def forward(self, x):
        return self.head(self.backbone(x))