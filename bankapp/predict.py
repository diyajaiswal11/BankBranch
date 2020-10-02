import torch
from torchvision import transforms
from PIL import Image


img_size = 224
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

transform = transforms.Compose([
    transforms.Resize((img_size, img_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])

model = torch.load('model.pth', map_location=device)

def predict(img_path):
    img = Image.open(img_path)
    img = transform(img)
    img = img.view(1, 3, img_size, img_size)
    out = model(img)
    prob, pred = torch.max(torch.softmax(out, dim=1), dim=1)
    labels = ['Benign', 'Malignant']
    return labels[pred], prob.item() * 100