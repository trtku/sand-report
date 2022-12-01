
import os
import json
from pxr import Usd
from pxr import UsdGeom
from compas.geometry import Transformation
from compas_xr.pxr import gfmatrix4d_from_transformation
from animation import TransformAnimation
from helpers import map_range

HERE = os.path.dirname(__file__)

filepath = os.path.join(HERE, "animations.json")
with open(filepath, 'r') as fp:
    data = json.load(fp)
animations = [TransformAnimation.from_data(d) for d in data]
filepath = os.path.join(HERE, "camera.json")
with open(filepath, 'r') as fp:
    camera_data = json.load(fp)

filename = os.path.splitext(os.path.basename(__file__))[0] + ".usda"
filepath = os.path.join(HERE, filename)
print(filepath)

stage = Usd.Stage.CreateNew(filepath)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

stage.SetStartTimeCode(0)

num_frames = []
for j, anim in enumerate(animations):
    print(anim)
    camera = UsdGeom.Camera.Define(stage, '/Camera%d' % j)
    camera.GetPrim().GetAttribute('focalLength').Set(
        camera_data['focal_length'])
    usd_anim = camera.AddTransformOp(opSuffix="anim%d" % j)

    total_num_frames = int(anim.duration) * anim.frames_per_second
    num_frames.append(total_num_frames)
    for i, frame in enumerate(anim.frames):
        t = round(map_range(i, 0, len(anim.frames) - 1, 0, total_num_frames))
        M = gfmatrix4d_from_transformation(Transformation.from_frame(frame))
        usd_anim.Set(time=t, value=M)
print(num_frames)
stage.SetEndTimeCode(max(num_frames))
stage.Save()
