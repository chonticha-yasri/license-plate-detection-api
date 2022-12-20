import torch

def get_yolov5(confident_val):     
   model = torch.hub.load('./yolov5', 'custom', path='./model/best.pt', source='local')
   model.conf = confident_val    
   return model