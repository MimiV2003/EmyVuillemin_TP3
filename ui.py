from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QSpinBox,
    QPushButton,
    QGridLayout,
)

class RandomAnimationGenerator(QWidget):
    
    def __init__(self):
        super().__init__()

    #--------------------------------------------------------------------------------------------------------------------------------------------
    def build_ui(self):
        #Creation du windows
        self.setWindowTitle("Random Animation Generator")
        self.setMinimumWidth(400)
        self.layout = QVBoxLayout(self)

        #Premiere section----------------------------------------------------------------------------------------------------------------
        #Animation Timing/ Temps animation-----------------------------------------------------------------------------------------------

        animation_timing = QGroupBox("Animation Timing")
        animation_timing_layout = QGridLayout(animation_timing)

        #Boite pour la duree avec fleche-------------------------------------------------------------------------------------------------------------

        self.nbr_frame = QSpinBox()
        self.nbr_frame.setRange(0, 1000)
        self.nbr_frame.setValue(100)

        #Boite pour etape avec fleche----------------------------------------------------------------------------------------------------------------

        self.nbr_step = QSpinBox()
        self.nbr_step.setRange(0, 1000)
        self.nbr_step.setValue(30)

        animation_timing_layout.addWidget(QLabel("Durations (Frames):"), 0, 0)# ===>Ordre pour le layout (QLabel ou "Nom", 0, 0)
        animation_timing_layout.addWidget(self.nbr_frame, 0, 1)
        animation_timing_layout.addWidget(QLabel("Step (Frames):"), 0, 2)
        animation_timing_layout.addWidget(self.nbr_step, 0, 3)

        self.layout.addWidget(animation_timing)
        #--------------------------------------------------------------------------------------------------------------------------------
        #Deuxieme section----------------------------------------------------------------------------------------------------------------

        #Translate Parameters/ Parametre du x,y,z----------------------------------------------------------------------------------------
        translate_parameters = QGroupBox("Translate Parameters")
        translate_parameters_layout = QGridLayout(translate_parameters)

        #Minimum X,Y,Z-------------------------------------------------------------------------------------------------------
        #Minimum X en negatif
        self.minimum_negative_x = QSpinBox()
        self.minimum_negative_x.setRange(-1000, 1000)
        self.minimum_negative_x.setValue(-5)
        #Minimum Y en negatif
        self.minimum_negative_y = QSpinBox()
        self.minimum_negative_y.setRange(-1000, 1000)
        self.minimum_negative_y.setValue(-5)
        #Minimum Z en negatif
        self.minimum_negative_z = QSpinBox()
        self.minimum_negative_z.setRange(-1000, 1000)
        self.minimum_negative_z.setValue(-5)
        #-------------------------------------------------------------------------------------------------------------------
        #Maximum X,Y,Z------------------------------------------------------------------------------------------------------

        #Maximum X
        self.maximum_x = QSpinBox()
        self.maximum_x.setRange(0, 1000)
        self.maximum_x.setValue(5)
        #Maximum Y
        self.maximum_y = QSpinBox()
        self.maximum_y.setRange(0, 1000)
        self.maximum_y.setValue(5)
        #Maximum Z
        self.maximum_z = QSpinBox()
        self.maximum_z.setRange(0, 1000)
        self.maximum_z.setValue(5)
        #---------------------------------------------------------------------------------------------------------------------
        #Ranger 0
        translate_parameters_layout.addWidget(QLabel("min x:"), 0, 0)
        translate_parameters_layout.addWidget(self.minimum_negative_x, 0, 1)
        translate_parameters_layout.addWidget(QLabel("min y:"), 0, 2)
        translate_parameters_layout.addWidget(self.minimum_negative_y, 0, 3)
        translate_parameters_layout.addWidget(QLabel("min z:"), 0, 4)
        translate_parameters_layout.addWidget(self.minimum_negative_z, 0, 5)
        #Ranger 1
        translate_parameters_layout.addWidget(QLabel("max x:"), 1, 0)
        translate_parameters_layout.addWidget(self.maximum_x, 1, 1)
        translate_parameters_layout.addWidget(QLabel("max y:"), 1, 2)
        translate_parameters_layout.addWidget(self.maximum_y, 1, 3)
        translate_parameters_layout.addWidget(QLabel("max z:"), 1, 4)
        translate_parameters_layout.addWidget(self.maximum_z, 1, 5)
        #----------------------------------------------------------------------------------------------------------------------
        self.layout.addWidget(translate_parameters)
        #---------------------------------------------------------------------------------------------------------------------
        #Troisieme section----------------------------------------------------------------------------------------------------

        rotate_parameters = QGroupBox("Rotate Parameters")
        rotate_parameters_layout = QGridLayout(rotate_parameters)

        #Minimum X,Y,Z Rotate--------------------------------------------------------------------------------------------------
        #Minimum X en negatif
        self.minimum_negative_rotate_x = QSpinBox()
        self.minimum_negative_rotate_x.setRange(-1000, 1000)
        self.minimum_negative_rotate_x.setValue(-180)
        #Minimum Y en negatif
        self.minimum_negative_rotate_y = QSpinBox()
        self.minimum_negative_rotate_y.setRange(-1000, 1000)
        self.minimum_negative_rotate_y.setValue(-180)
        #Minimum Z en negatif
        self.minimum_negative_rotate_z = QSpinBox()
        self.minimum_negative_rotate_z.setRange(-1000, 1000)
        self.minimum_negative_rotate_z.setValue(-180)

        #Maximum X,Y,Z Rotate---------------------------------------------------------------------------------------------------
        #Maximum X
        self.maximum_rotate_x = QSpinBox()
        self.maximum_rotate_x.setRange(0, 1000)
        self.maximum_rotate_x.setValue(180)
        #Maximum Y
        self.maximum_rotate_y = QSpinBox()
        self.maximum_rotate_y.setRange(0, 1000)
        self.maximum_rotate_y.setValue(180)
        #Maximum Z
        self.maximum_rotate_z = QSpinBox()
        self.maximum_rotate_z.setRange(0, 1000)
        self.maximum_rotate_z.setValue(180)
        #-------------------------------------------------------------------------------------------------------------------------
        #Ranger 0
        rotate_parameters_layout.addWidget(QLabel("min x:"), 0, 0)
        rotate_parameters_layout.addWidget(self.minimum_negative_rotate_x, 0, 1)
        rotate_parameters_layout.addWidget(QLabel("min y:"), 0, 2)
        rotate_parameters_layout.addWidget(self.minimum_negative_rotate_y, 0, 3)
        rotate_parameters_layout.addWidget(QLabel("min z:"), 0, 4)
        rotate_parameters_layout.addWidget(self.minimum_negative_rotate_z, 0, 5)
        #Ranger 1
        rotate_parameters_layout.addWidget(QLabel("max x:"), 1, 0)
        rotate_parameters_layout.addWidget(self.maximum_rotate_x, 1, 1)
        rotate_parameters_layout.addWidget(QLabel("max y:"), 1, 2)
        rotate_parameters_layout.addWidget(self.maximum_rotate_y, 1, 3)
        rotate_parameters_layout.addWidget(QLabel("max z:"), 1, 4)
        rotate_parameters_layout.addWidget(self.maximum_rotate_z, 1, 5)
        #-----------------------------------------------------------------------------------------------------------------------------
        self.layout.addWidget(rotate_parameters)
        #-----------------------------------------------------------------------------------------------------------------------------
        #Quatrieme section------------------------------------------------------------------------------------------------------------

        scale_parameters = QGroupBox("Scale Parameters")
        scale_parameters_layout = QGridLayout(scale_parameters)

        #Minimum X,Y,Z Scale-------------------------------------------------------------------------------------------------------------
        #Minimum X en negatif
        self.minimum_scale_x = QSpinBox()
        self.minimum_scale_x.setRange(0, 1000)
        self.minimum_scale_x.setValue(1)
        #Minimum Y en negatif
        self.minimum_scale_y = QSpinBox()
        self.minimum_scale_y.setRange(0, 1000)
        self.minimum_scale_y.setValue(1)
        #Minimum Z en negatif
        self.minimum_scale_z = QSpinBox()
        self.minimum_scale_z.setRange(0, 1000)
        self.minimum_scale_z.setValue(1)
        #Maximum X,Y,Z Scale-----------------------------------------------------------------------------------------------------------
        #Maximum X
        self.maximum_scale_x = QSpinBox()
        self.maximum_scale_x.setRange(0, 1000)
        self.maximum_scale_x.setValue(2)
        #Maximum Y
        self.maximum_scale_y = QSpinBox()
        self.maximum_scale_y.setRange(0, 1000)
        self.maximum_scale_y.setValue(2)
        #Maximum Z
        self.maximum_scale_z = QSpinBox()
        self.maximum_scale_z.setRange(0, 1000)
        self.maximum_scale_z.setValue(2)
        #-----------------------------------------------------------------------------------------------------------------------------
        #Ranger 0
        scale_parameters_layout.addWidget(QLabel("min x:"), 0, 0)
        scale_parameters_layout.addWidget(self.minimum_scale_x, 0, 1)
        scale_parameters_layout.addWidget(QLabel("min y:"), 0, 2)
        scale_parameters_layout.addWidget(self.minimum_scale_y, 0, 3)
        scale_parameters_layout.addWidget(QLabel("min z:"), 0, 4)
        scale_parameters_layout.addWidget(self.minimum_scale_z, 0, 5)
        #Ranger 1
        scale_parameters_layout.addWidget(QLabel("max x:"), 1, 0)
        scale_parameters_layout.addWidget(self.maximum_scale_x, 1, 1)
        scale_parameters_layout.addWidget(QLabel("max y:"), 1, 2)
        scale_parameters_layout.addWidget(self.maximum_scale_y, 1, 3)
        scale_parameters_layout.addWidget(QLabel("max z:"), 1, 4)
        scale_parameters_layout.addWidget(self.maximum_scale_z, 1, 5)
        #--------------------------------------------------------------------------------------------------------------------------------
        self.layout.addWidget(scale_parameters)
        #--------------------------------------------------------------------------------------------------------------------------------
        
        # button
        self.button = QPushButton("Generate")
        self.layout.addWidget(self.button)