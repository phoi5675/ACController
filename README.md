# ACController
turn on / off samsung AC w/ arduino and raspi
# Overview
turn on, off or set low temperature remotely


use raspi as a server, arduino for controlling IR sensors to turn AC on


used iphone shortcuts app to get access to raspi through ssh, and run python file

(e.g. to turn AC on, ssh -> python3 ~/.../ac.py <<< '1')

for input '0', turn AC off, '1' for turn AC on, and '2' for set AC lower temperature
# Requirements
- software requirements
 - python 3
 - serial
- hardware requirements
 - raspberry pi
 - arduino
