# Use a regular RC remote to control FRC robot

This project Only give you some rough idea. **This could create a run away robot. Use with caution.** Incomplete but might give you some idea.

# Hardware requirement

 - Raspberry Pico W board 
 - i-Bus compliant remote kit (Tested with Flysky
   FS-i6X and FS-iA10B) 
 - Coprocessor that could run Python (Raspberry pi
   4 or Jetson Nano)

# Hardware Hookup

 - Receiver i-Bus TX to Pico Pin 7 
 - [Pico Hookup Tutorial](https://www.youtube.com/watch?time_continue=668&v=_Fz9lJXu2DE&embeds_referring_euri=https://www.penguintutor.com/&source_ve_path=MTM5MTE3LDEyNzI5OSwxMjcyOTksMTI3Mjk5LDIzODUx&feature=emb_title)
 - Receiver VCC and GND to Pico 5V and GND 
 - Pico USB to Coprocessor
 - Coprocessor to robot network

It might be possible to hook Pico directly on roboRIO, but my RIO's USB port is full. This would be using a different approach on decoding Serial data directly on roboRIO without using NetworkTables

# Robot still need to be enabled to have motor power output.

Do this with regular DS or use [FakeDS](https://github.com/sikaxn/fakeDS-Python) on coprocessor if you want your robot to be headless. It is strongly recommand to test your robot with regular DS before moving on to FakeDS.

# RC setup

Please setup failsafe accordingly in RC Rx menu. Better bring all value to 0. Read your RC controller's manual for more info

# Acknowledgement

Some of the code and idea is borrowed from penguintutor's # [Radio Control for the Raspberry Pi Pico - using I-Bus](http://www.penguintutor.com/news/electronics/rc-pico-ibus).
