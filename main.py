#EmyVuillemin TP3----------------------------------------------------------------------------------------------------------

#import
import animator
import random
import ui
from maya import cmds


def on_clicked():
    print("Generate")
    animator.animation_object(tool_window)    
        
#---------------------------------------------------------------------------------------------------------------------------------------------

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui.RandomAnimationGenerator()
    tool_window.build_ui()
    tool_window.button.clicked.connect(on_clicked)

    tool_window.show()


#Doit faire un ctrl + z ----------------------------------------------
cmds.undoInfo(openChunk=True)



main()