import os
import json
import xr_paths
from pxr import Usd, UsdGeom
#import omni.usd
#import omni.timeline
import asyncio
import aioconsole

HERE = os.path.dirname(os.path.abspath(__file__))
HERE = r"C:\Users\rustr\workspace\projects\camera_anim_presentation"

keys = ['a', 's', 'd', 'f', 'g']
frame_numbers = [192, 216, 456, 216, 216]

frames_per_second = 24.

# TODO url
url='omniverse://localhost/Users/rr/walls/walls.project.usd'

async def echo():
    stdin, stdout = await aioconsole.get_standard_streams()
    async for line in stdin:
        stdout.write(line)
        if line[0] == 'a':
            print("yes")


async def open_stage(url):
    """Opens the stage.
    """
    omni.client.usd_live_set_default_enabled(True)
    await omni.usd.get_context().open_stage_async(url)
    context = omni.usd.get_context()
    context.set_stage_live(omni.usd.StageLiveModeType.ALWAYS_ON)
    return context.get_stage()


def play_animation_between_frames(start_frame, end_frame):
    interface = omni.timeline.get_timeline_interface()
    interface.set_start_time(start_frame/frames_per_second)
    interface.set_end_time(end_frame/frames_per_second)
    interface.set_looping(False)
    interface.set_auto_update(True)
    interface.play()

async def wait_for_frame(number):
    interface = omni.timeline.get_timeline_interface()
    while interface.get_current_time() < number:
        #print(interface.get_current_time())
        await asyncio.sleep(1)

async def run():

    stage = await open_stage(url)

    #asyncio.ensure_future(echo())

    # set correct endtime
    stage.SetStartTimeCode(0)
    stage.SetEndTimeCode(700)

    # select camera view
    viewport_window = omni.kit.viewport.get_default_viewport_window()
    #print(viewport_window)
    #print(viewport_window.get_active_camera())

    for i in range(5):
        viewport_window.set_active_camera("/Camera%d" % i)

        camera = stage.GetPrimAtPath("/Camera%d" % i)
        ts = camera.GetAttribute("xformOp:transform:anim%d" % i).GetTimeSamples()
        play_animation_between_frames(ts[0], ts[-1])
        print("Awaiting for", ts[-1)])
        await wait_for_frame(ts[-1])


    # start keyboard listener

    #await asyncio.sleep(1)
    #print(interface.get_current_time())
    #interface.pause()
        
    #while interface.get_current_time() < 192:
    #   interface.forward_one_frame()
    

if __name__ == "__main__":
    asyncio.ensure_future(run())



















