# Dual homing your Raspberry Pi
For this project we need the Pi to access two networks:
- our office wifi for access to twitter
- our internal (non-web) network

This tutorial come from giox069 and can be found [here](https://raspberrypi.stackexchange.com/questions/29783/how-to-setup-network-manager-on-raspbian).

This isn't easy using the baked-in network manager software on Raspbian Stretch. So we need to install `Network-Manager`.

This installation is overkill - but I'm not clever enough to work out which packages I don't need.

```sudo apt install network-manager network-manager-gnome openvpn openvpn-systemd-resolved network-manager-openvpn network-manager-openvpn-gnome```

Then we need to purge the old network management software:

`sudo apt purge openresolv dhcpcd5`

And then replace a config file with a symlink to another:

`sudo ln -sf /lib/systemd/resolv.conf /etc/resolv.conf`

Finally, right click the tool bar at the top of the screen, open 'Panel Settings' > 'Panel Applets, removes "Wireless & Wired Networks". Then `reboot`.

Once rebooted the new settings can be found in the new icon at the top-right. If you are using two wifi networks, the one you want internet from must be set as default.