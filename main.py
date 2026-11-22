#EmyVuillemin TP3----------------------------------------------------------------------------------------------------------

#import
import animator
import random
import ui
from maya import cmds
#Grace au importlib ==> mon graph editor marche enfin!------
import importlib
importlib.reload(ui)
importlib.reload(animator)
#----------------------------------------------------------

#Quand je clique sur le bouton generate==>print generete et ouvre animator.py + (fonction)
def on_clicked():
    print("Generate")
    animator.animation_object(tool_window)    
        
#---------------------------------------------------------------------------------------------------------------------------------------------

def main():
    global tool_window #Fenetre disparait pas
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.RandomAnimationGenerator()
    tool_window.build_ui()
    tool_window.button.clicked.connect(on_clicked)

    tool_window.show()#affiche


#Doit faire un ctrl + z ----------------------------------------------
cmds.undoInfo(openChunk=True)



main()