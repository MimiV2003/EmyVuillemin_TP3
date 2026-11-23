#Section pour animation random-------------------------------------------------------------------
#Celui la a beaucoup de ligne de code, je ne sais pas si cest possible de rendre les lignes plus court
#----------------------------------------------------------------------------------------------------

#Import
from maya import cmds
import random


#Fonction pour les frames et les steps-----------------------------------------------------------
def frame_step(tool_window):
    duration = int(tool_window.nbr_frame.value())
    step = int(tool_window.nbr_step.value())

    cmds.playbackOptions(min=0, max=duration)#debute de 0 jusqu a la duration selectionner

    if duration <= 0:
        return [0]

    if step <= 0: #retourne la frame du debut et la frame de fin 
        return [0, duration]

    frames = list(range(0, duration + 1, step))#Liste des frames pour commencer a 0 jusqu a duration (+1 pour mettre une limite)
    #Exemple si je veux sa termine a 100, je dois demander la limite de 101 pour pouvoir atteindre le 100.

    if frames[-1] != duration:#assure de bien terminer sur la bonne frame (Step est par 30 ==> 30,60,90 et ensuite 120)
        frames.append(duration)#120 est bloquer (a cause de la limite de 100 duration)alors les steps s arrete au 90, mais il reste encore 10 de duration
        #le frames[-1] != duration ==> verifie frame differente(!=) que duration + ajoute pour faire la boucle

    return frames

#-------------------------------------------------------------------------------------------------------


#Fonction pour animation aux objets-------------------------------------------------------------------------------------------------------
def animation_object(tool_window):

    selection_maya = cmds.ls(selection=True, long=True)#selectionne les objets dans maya (s'assure que chaque objet est different)

    cmds.undoInfo(openChunk=True)#regroupe pour pouvoir faire ctrl+z d un coup
    
    try:

        for selection in selection_maya:# prend un objet a la fois dans la liste et execute (==> fait une animation random pour chaque objet)

            if not selection:
                return

            frame = frame_step(tool_window)#cmds.playbackOptions(min=0, max=duration)
            cmds.cutKey(selection, clear=True)#efface les anciennes keys animation avant de mettre une nouvelle animation

            #-------------------------------------------------------------------------------------------------
            #Valeur pour translate, rotation, scale------------------------------------------------------------
        
            #Pour cette section: cest tout les translates, rotation et scale (x,y,z) ==> du minimum jusqu au maximum. Random de valeurs avec des limites
            #Random.randint = piocher un nbr entier aleatoire
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

            #------------------------------------------------------------------------------------------------------------
            #Keyframe pour translate, rotation, scale---------------------------------------------------------------------
            
            #Cette section est pour les keyframes du debut (0 frame)
            #selection = l objet selectionner dans maya
            #attribute="translateX" c'est le nom exacte de attribut sur maya ==> qui perment de faire les keysframe
            #value= est la valeur piocher au hasard
            #time= frame que la key est mis (premier element)

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

            #---------------------------------------------------------------------------
            #Le temps en frame------------------------------------------------------------

            #Cette section cest les keyframes entre le 0 (frame[0]) et derniere frame (frame[-1])
            #Alors la boucle commence avec le premier step et termine au dernier step (max) ==> ex: (30, 60, 90)
            # t = prend une frame, t=time ==> mets une keys dans cette frame (exemple: 1 frame par step ==> 30, 60, 90)
            #Grace a cette boucle, ne touche pas au premier key et derniere key ex:(0, 100)

            for t in frame[1:-1]:

                #Translate----------------------------------------------------------------------------------------------
                cmds.setKeyframe(selection, attribute="translateX", value=random.randint(tool_window.minimum_negative_x.value(), tool_window.maximum_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="translateY", value=random.randint(tool_window.minimum_negative_y.value(), tool_window.maximum_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="translateZ", value=random.randint(tool_window.minimum_negative_z.value(), tool_window.maximum_z.value()), time=t)

                #Rotation----------------------------------------------------------------------------------------------------
                cmds.setKeyframe(selection, attribute="rotateX", value=random.randint(tool_window.minimum_negative_rotate_x.value(), tool_window.maximum_rotate_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="rotateY", value=random.randint(tool_window.minimum_negative_rotate_y.value(), tool_window.maximum_rotate_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="rotateZ", value=random.randint(tool_window.minimum_negative_rotate_z.value(), tool_window.maximum_rotate_z.value()), time=t)

                #Scale-------------------------------------------------------------------------------------------------------
                cmds.setKeyframe(selection, attribute="scaleX", value=random.randint(tool_window.minimum_scale_x.value(), tool_window.maximum_scale_x.value()), time=t)
                cmds.setKeyframe(selection, attribute="scaleY", value=random.randint(tool_window.minimum_scale_y.value(), tool_window.maximum_scale_y.value()), time=t)
                cmds.setKeyframe(selection, attribute="scaleZ", value=random.randint(tool_window.minimum_scale_z.value(), tool_window.maximum_scale_z.value()), time=t)

            #----------------------------------------------------------------------------------------
            #Keyframe translate, rotation, scale (dernier)-------------------------------------------

            #Cette section cest le dernier keyframe de l animation
            #time=frame[-1] ==>cible le dernier de frame
            #value= prends meme valeur que le premier keyframe ex:(0, 100) (Avant frame[0]) ==> pas besoin de mettre un random.randint

            #Translate--------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="translateX", value=tx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="translateY", value=ty, time=frame[-1])
            cmds.setKeyframe(selection, attribute="translateZ", value=tz, time=frame[-1])

            #Rotation-----------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="rotateX", value=rx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="rotateY", value=ry, time=frame[-1])
            cmds.setKeyframe(selection, attribute="rotateZ", value=rz, time=frame[-1])

            #Scale-------------------------------------------------------------------------
            cmds.setKeyframe(selection, attribute="scaleX", value=sx, time=frame[-1])
            cmds.setKeyframe(selection, attribute="scaleY", value=sy, time=frame[-1])
            cmds.setKeyframe(selection, attribute="scaleZ", value=sz, time=frame[-1])

            #Apparaitre le graph editor dans maya---------------------------------------
            cmds.GraphEditor()
            
    finally:

        #Ctrl + z---------------------
        cmds.undoInfo(closeChunk=True)
