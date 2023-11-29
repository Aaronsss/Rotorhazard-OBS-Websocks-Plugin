# OBS_Websocks

This plugin allows for the automation of recordings and scene changes in OBS based on race events that occur. This is useful if live streaming your race
 
 ### Install
 
Make sure you have OBS running and have the OBS websock plugin installed. OBS websocket is included by default in OBS > 28.0.0 but the repository can be found here if you need it: https://github.com/obsproject/obs-websocket

Log in via SSH and then execute the following commands

```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/ ~/RotorHazard/src/server/plugins/
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/
rm ./main.zip
pip install -r ./RotorHazard/src/server/plugins/OBS_Websocks/requirements.txt
sudo systemctl restart rotorhazard.service
```


if the above doesn't work or you have the following folder on your pi ~/RotorHazard/src/server/venv run the following commands
```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/ ~/RotorHazard/src/server/plugins/
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/
rm ./main.zip
source ./RotorHazard/src/server/venv/bin/activate
pip install -r ./RotorHazard/src/server/plugins/OBS_Websocks/requirements.txt
deactivate
sudo systemctl restart rotorhazard.service
```

On the Settings page in RotorHazard you will see OBS actions section, you will need to complete this section before you can use the plugin

1. You will need to find the IP or .local name of your OBS PC
2. Enter the port and password which can be found / set in OBS tools -> OBS Websocket Server Settings. 
3. Tick the enable OBS actions box to enable or disable the OBS plugin
4. Lastly click save connection settings and reboot rotorhazard / the raspberry pi
5. When the server has rebooted it should connect automatically to OBS and OBS will give you a pop up saying it has connected
6. You may connect or disconnect from OBS using the buttons
![image](https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/assets/23297034/65ff31ea-5713-428c-9ab8-16c74cbe8ae2)

Once restarted you will be able to setup OBS messages in the Event Actions section of the settings page to be performed on certain timer events 

The event actions page will show the following. 
1. Select the event you wish to use to trigger the OBS scene change. 
2. You will then need to type in the exact name of the scene that you want to change to in OBS. 
3. Lastly select what you want the recording to do from the drop down
![image](https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/assets/23297034/da39fb4d-994b-46ab-a178-d5ce56d2c294)
