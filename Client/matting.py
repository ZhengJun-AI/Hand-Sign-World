import torch
import os
import numpy as np


# return a pretrained model and according precision
def load_model(model_path, img_size='1080p'):
    device = torch.device('cuda')
    fp = model_path.split('_')[-1].split('.')[0]
    precision = torch.float16 if fp == 'fp16' else torch.float32

    assert os.path.exists(model_path), f'{model_path} not exist!'
    model = torch.jit.load(model_path)
    if img_size == '1080p':
        model.backbone_scale = 0.25
        model.refine_mode = 'sampling'
        model.refine_sample_pixels = 80_000
    elif img_size == '720p':
        model.backbone_scale = 0.25
        model.refine_mode = 'sampling'
        model.refine_sample_pixels = 40_000

    model = model.to(device)
    return model, precision


# input model, precision and RGB original image, background, new background
# return RGB image with new background
def matting(model, precision, src, bgr, new_bgr):
    device = torch.device('cuda')
    src, bgr,  new_bgr= torch.from_numpy(src/255.), torch.from_numpy(bgr/255.), torch.from_numpy(new_bgr/255.)
    src = src.to(precision).to(device).permute(2,0,1).unsqueeze(0)
    bgr = bgr.to(precision).to(device).permute(2,0,1).unsqueeze(0)
    new_bgr = new_bgr.to(precision).to(device).permute(2,0,1).unsqueeze(0)

    pha, fgr = model(src, bgr)[:2]
    com = pha * fgr + (1 - pha) * new_bgr
    com=com.squeeze().permute(1,2,0).cpu().numpy()
    com = 255.*com
    return com.astype(np.uint8)
