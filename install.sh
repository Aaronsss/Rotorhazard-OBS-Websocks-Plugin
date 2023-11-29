#Install script for OBS websocks plugin
mv ~/Rotorhazard-OBS-Websocks-Plugin-main/OBS_Websocks/ ~/RotorHazard/src/server/plugins/

# Do this if the user installed using the old venv setup
cd ~
if [ -d "./RotorHazard/src/server/venv/" ]; then
    source ./RotorHazard/src/server/venv/bin/activate
fi

# Do this if the user is using the latest venv setup
if [ -d "./venv/" ]; then
    source ./venv/bin/activate
fi

pip install -r ./RotorHazard/src/server/plugins/OBS_Websocks/requirements.txt

# Reboot the RH server
sudo systemctl restart rotorhazard.service

# Clean up
rm ./main.zip
rm -R ./Rotorhazard-OBS-Websocks-Plugin-main/
