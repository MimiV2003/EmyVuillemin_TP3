from maya import cmds
import random



def frame_step(tool_window):
    duration = int(tool_window.nbr_frame.value())
    step = int(tool_window.nbr_step.value())

    cmds.playbackOptions(min=0, max=duration)

    if duration <= 0:
        return [0]

    if step <= 0:
        return [0,duration]

    frame = list(range(0, duration + 1, step))

    if frame[-1] != duration:
        frame.append(duration)

        return frame




#Fonction pour animation aux objets-------------------------------------------------------------------------------------------------------
def animation_object(tool_window):
    cmds.undoInfo(openChunk=True)
    
    try:
        cmds.playbackOptions(min=0, max=tool_window.duration.value())

        selection=cmds.ls(selection=True, long=True)
        if not selection:
            return

        frame = frame_step(tool_window)
        cmds.cutKey(selection, clear=True)

        time=0
        for loop in range(3):
            cmds.setKeyframe(selection, attribute="translateX",value=random.randint(tool_window.translate_minimum_negative_x(),tool_window.translate_maximum_x.value()), time=time)
            cmds.setKeyframe(selection, attribute="translateY",value=random.randint(tool_window.translate_minimum_negative_y(),tool_window.translate_maximum_y.value()), time=time)
            cmds.setKeyframe(selection, attribute="translateZ",value=random.randint(tool_window.translate_minimum_negative_z(),tool_window.translate_maximum_z.value()), time=time)

            time=time + tool_window.step.value()

    finally:

        cmds.undoInfo(closeChunk=True)
