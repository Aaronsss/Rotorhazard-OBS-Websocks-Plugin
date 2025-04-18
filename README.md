# OBS_Websocks

This plugin allows for the automation of recordings and scene changes in OBS based on race events that occur. This is useful if live streaming your race
 
 ### Install
 
Make sure you have OBS running and have the OBS websock plugin installed. OBS websocket is included by default in OBS > 28.0.0 but the repository can be found here if you need it: https://github.com/obsproject/obs-websocket

There are 4 ways you can install this plugin
1. Though RotorHazards community plugin manager on RotorHazard 4.3.0 or greater:  
   This can be found on your timer which must be connected to the internet by going to settings -> plugins -> Browse Community Plugins (online only) -> Streaming & Overlays then install the OBS Websocks plugin  

2. Log in via SSH and then execute the following commands

```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/custom_plugins/obs_websocks/ ~/RotorHazard/src/server/plugins/
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/
rm ./main.zip
pip install -r ./RotorHazard/src/server/plugins/obs_websocks/requirements.txt
sudo systemctl restart rotorhazard.service
```


3. if the above doesn't work or you have the following folder on your pi ~/RotorHazard/src/server/venv run the following commands
```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/custom_plugins/obs_websocks/ ~/RotorHazard/src/server/plugins/
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/
rm ./main.zip
source ./RotorHazard/src/server/venv/bin/activate
pip install -r ./RotorHazard/src/server/plugins/obs_websocks/requirements.txt
deactivate
sudo systemctl restart rotorhazard.service
```

4. Manually:  
  If you wish to install manually, place the custom_plugins/obs_websocks folder within the RotorHazard plugins folder Rotorhazard/src/server/plugins then start / restart the server  

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

### Troubleshooting
If you are unable to connect / the log file says the server is not active try the following:
1. Check OBS is running 
2. Confirm the OBS websocket server options has Enable OBS Websocket server selected within the OBS software
3. Confirm your credentials match those in the OBS websockets server update them and click save connection info
4. Try disabling your PC's firewall. If your firewall it set to public it may be blocking the connection.
5. Update to the latest version of this plugin

You will need to reboot rotorhazard after each of the above steps

If you suspect the requirements.txt has not installed correctly you can type pip list in the ssh console and check the requirements.txt depenancies and versions have been installed
