import pickle
from torchvision import transforms
from PIL import Image

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


img_size = 224
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

transform = transforms.Compose([
    transforms.Resize((img_size, img_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225])
])

model = pickle.load(open('./new_model.sav', 'rb'))

def predict(img_path):
    img = Image.open(img_path)
    img = transform(img)
    img = img.view(1, 3, img_size, img_size)
    out = model(img)
    out=out.detach().numpy()
    a=softmax(out)
    prob, pred = np.max(a),np.argmax(a)
    labels = ['Benign', 'Malignant']
    return pred, prob * 100
