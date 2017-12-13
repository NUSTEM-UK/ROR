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

## Update
I ran into a slight problem, Network Manager sets a 'default' network which is the one that is expected to be connected to the internet. You need to change the default to the network that is connected to the internet. 

Do this by right clicking the Network Icons, then Edit Connections. From here select the non-inernet WiFi network and click Edit. In the ipV4 setting, click routes and then check "Use this connection only for resources on this network". Save and reboot.