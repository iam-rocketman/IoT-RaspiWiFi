import os

os.system('sudo mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.OLD')
os.system('sudo rm -f /usr/share/configure_wifi/tmp/*')
os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/dhcpcd.conf.aphost /etc/dhcpcd.conf')
os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/hostapd.conf /etc/hostapd/')
os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/dnsmasq.conf /etc/dnsmasq.conf')
os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/default_hostapd /etc/default/hostapd')
os.system('sudo cp /usr/share/configure_wifi/Reset_Device/static_files/rc.local.aphost /etc/rc.local')
os.system('sudo systemctl enable hostapd')
os.system('sudo systemctl enable dnsmasq')
os.system('sudo reboot')
