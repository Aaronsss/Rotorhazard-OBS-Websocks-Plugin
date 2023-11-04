# OBS_Websocks

This plugin allows for the automation of recordings and scene changes in OBS based on race events that occur. This is useful if live streaming your race
 
 ### Install
 
Make sure you have OBS running and have the OBS websock plugin installed OBS websocket is included by default in OBS > 28.0.0 but the repository can be found here if you need to download it: https://github.com/obsproject/obs-websocket

Place the OBS_Websocks folder in the rotorhazrd plugins directory
 
Run the requirements install in the directory using the following command
 
pip install -r .requirements.txt
 
Start / restart rotorhazard 

On the Settings page you will see OBS actions section, expand this and complete the details to connect to OBS websocks, make sure you click the Save Connection Settings button when done. You will also need to restart RotorHazard for the settings to take effect.

You will now be able to setup OBS messages in the Event Actions section of the settings page to be performed on certain timer events 
