# OBS_Websocks

This plugin allows for the automation of recordings and scene changes in OBS based on race events that occur. This is useful if live streaming your race
 
 ### Install
 
Make sure you have OBS running and have the OBS websock plugin installed. OBS websocket is included by default in OBS > 28.0.0 but the repository can be found here if you need it: https://github.com/obsproject/obs-websocket

Log in via SSH and then execute the following commands if you have a venv folder is ~/RotorHazard/src/server/venv

```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/ ~/RotorHazard/src/server/plugins/
pip install -r ./RotorHazard/src/server/plugins/OBS_Websocks/requirements.txt
sudo systemctl restart rotorhazard.service
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/
rm ./main.zip
```


if the above doesnt work or you have the following folder on your pi ~/RotorHazard/src/server/venv run the following commands
```
cd ~
wget https://github.com/Aaronsss/Rotorhazard-OBS-Websocks-Plugin/archive/refs/heads/main.zip
unzip ./main.zip
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/ ~/RotorHazard/src/server/plugins/
source ./RotorHazard/src/server/venv/bin/activate
pip install -r ./RotorHazard/src/server/plugins/OBS_Websocks/requirements.txt
deactivate
sudo systemctl restart rotorhazard.service
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/
rm ./main.zip
```

On the Settings page in RotorHazard you will see OBS actions section, expand this and complete the details to connect to OBS websocks, make sure you click the Save Connection Settings button when done. You will also need to restart RotorHazard for the settings to take effect.

Once restarted you will be able to setup OBS messages in the Event Actions section of the settings page to be performed on certain timer events 
