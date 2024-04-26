#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import os
import time
import logging
import ntcore
import subprocess
import wpimath 


class MyRobot(wpilib.TimedRobot):


    def robotInit(self):
        """Robot initialization function"""

        
        #ntcore initialization
        inst = ntcore.NetworkTableInstance.getDefault()
        table = inst.getTable("flyskyiBus")
        self.ibusCH1 = table.getDoubleTopic("ch1").subscribe(0)
        self.ibusCH2 = table.getDoubleTopic("ch2").subscribe(0)
        self.ibusCH3 = table.getDoubleTopic("ch3").subscribe(0)
        self.ibusCH4 = table.getDoubleTopic("ch4").subscribe(0)
        self.ibusCH5 = table.getDoubleTopic("ch5").subscribe(0)
        self.ibusCH6 = table.getDoubleTopic("ch6").subscribe(0)
        
    def teleopInit(self):
        pass

    def autonomousInit(self):

        pass
		
    def disabledInit(self):

        pass
        
    def DisabledPeriodic(self):
        
        pass

    def teleopPeriodic(self):
       
        print("ch1", self.ibusCH1.get())
        print("ch2", self.ibusCH2.get())
        print("ch3", self.ibusCH3.get())
        print("ch4", self.ibusCH4.get())
        print("ch5", self.ibusCH5.get())
        print("ch6", self.ibusCH6.get())
        
        pass
        
    def autonomousPeriodic(self):

        pass

    def RobotPeriodic(self):

        pass