from maya import cmds
import random



def frame_step(tool_window):
    duration = int(tool_window.nbr_frame.value())
    step = int(tool_window.nbr_step.value())

    cmds.playbackOptions(min=0, max=duration)

    if duration <= 0:
        return [0]

    if step <= 0:
        return [0, duration]

    frames = list(range(0, duration + 1, step))

    if frames[-1] != duration:
        frames.append(duration)

    return frames




#Fonction pour animation aux objets-------------------------------------------------------------------------------------------------------
def animation_object(tool_window):

    selection_maya = cmds.ls(selection=True, long=True)

    cmds.undoInfo(openChunk=True)
    
    try:


        cmds.playbackOptions(min=0, max=tool_window.nbr_frame.value())

        for selection in selection_maya:

            if not selection:
                return

            frame = frame_step(tool_window)
            cmds.cutKey(selection, clear=True)

            #-----------------------------------------
            #VALEUR POUR TRANSLATE, ROTATION, SCALE
            #-----------------------------------------

            #Translate----------------------------------------------------------------------------------------
            tx = random.randint(tool_window.minimum_negative_x.value(), tool_window.maximum_x.value())
            ty = random.randint(tool_window.minimum_negative_y.value(), tool_window.maximum_y.value())
            tz = random.randint(tool_window.minimum_negative_z.value(), tool_window.maximum_z.value())

            #Rotation-----------------------------------------------------------------------------------------
            rx = random.randint(tool_window.minimum_negative_rotate_x.value(), tool_window.maximum_rotate_x.value())
            ry = random.randint(tool_window.minimum_negative_rotate_y.value(), tool_window.maximum_rotate_y.value())
            rz = random.randint(tool_window.minimum_negative_rotate_z.value(), tool_window.maximum_rotate_z.value())

            #Scale--------------------------------------------------------------------------------------------
            sx = random.randint(tool_window.minimum_scale_x.value(), tool_window.maximum_scale_x.value())
            sy = random.randint(tool_window.minimum_scale_y.value(), tool_window.maximum_scale_y.value())
            sz = random.randint(tool_window.minimum_scale_z.value(), tool_window.maximum_scale_z.value())

            #--------------------------------------------------------------------------------------------------------

            #-----------------------------------------
            #KEYFRAME POUR TRANSLATE, ROTATION, SCALE
            #-----------------------------------------

            #Translate keyframe----------------------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="translateX", value=tx, time=frame[0])
            cmds.setKeyframe(selection, attribute="translateY", value=ty, time=frame[0])
            cmds.setKeyframe(selection, attribute="translateZ", value=tz, time=frame[0])

            #Rotation keyframe-----------------------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="rotateX", value=rx, time=frame[0])
            cmds.setKeyframe(selection, attribute="rotateY", value=ry, time=frame[0])
            cmds.setKeyframe(selection, attribute="rotateZ", value=rz, time=frame[0])

            #Scale keyframe--------------------------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="scaleX", value=sx, time=frame[0])
            cmds.setKeyframe(selection, attribute="scaleY", value=sy, time=frame[0])
            cmds.setKeyframe(selection, attribute="scaleZ", value=sz, time=frame[0])

            #------------------------------------------------------------------------------------------------------

            #------------------------------
            #TEMPS EN FRAME
            #------------------------------

            for t in frame[1:-1]:

                #Translate
                cmds.setKeyframe(selection, attribute="translateX", value=random.randint(tool_window.minimum_negative_x.value(), tool_window.maximum_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="translateY", value=random.randint(tool_window.minimum_negative_y.value(), tool_window.maximum_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="translateZ", value=random.randint(tool_window.minimum_negative_z.value(), tool_window.maximum_z.value()), time=t)

                #Rotation
                cmds.setKeyframe(selection, attribute="rotateX", value=random.randint(tool_window.minimum_negative_rotate_x.value(), tool_window.maximum_rotate_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="rotateY", value=random.randint(tool_window.minimum_negative_rotate_y.value(), tool_window.maximum_rotate_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="rotateZ", value=random.randint(tool_window.minimum_negative_rotate_z.value(), tool_window.maximum_rotate_z.value()), time=t)

                #Scale
                cmds.setKeyframe(selection, attribute="scaleX", value=random.randint(tool_window.minimum_scale_x.value(), tool_window.maximum_scale_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="scaleY", value=random.randint(tool_window.minimum_scale_y.value(), tool_window.maximum_scale_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="scaleZ", value=random.randint(tool_window.minimum_scale_z.value(), tool_window.maximum_scale_z.value()), time=t)

            #Translate
            cmds.setKeyframe(selection, attribute="translateX", value=tx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="translateY", value=ty, time=frame[-1])
            cmds.setKeyframe(selection, attribute="translateZ", value=tz, time=frame[-1])

            #Rotation
            cmds.setKeyframe(selection, attribute="rotateX", value=rx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="rotateY", value=ry, time=frame[-1])
            cmds.setKeyframe(selection, attribute="rotateZ", value=rz, time=frame[-1])

            #Scale
            cmds.setKeyframe(selection, attribute="scaleX", value=sx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="scaleY", value=sy, time=frame[-1])
            cmds.setKeyframe(selection, attribute="scaleZ", value=sz, time=frame[-1])

            #Apparaitre le graph editor dans maya
            cmds.GraphEditor()
            
    finally:
        #Ctrl + z
        cmds.undoInfo(closeChunk=True)
