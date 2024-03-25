import os

def run_alphapose(folder, video):
    video = video
    folder = folder
    command = f"../fencingguienv/Scripts/python.exe scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x-duc.yaml --checkpoint pretrained_models/fast_421_res50-shuffle_256x192.pth --video \"{video}\" --outdir \"{folder}/output/\" --qsize 50 --detbatch 5 --posebatch 50 --gpus 0 --pose_track --save_video --showbox --vis_fast --debug"
    print(command)

    return command