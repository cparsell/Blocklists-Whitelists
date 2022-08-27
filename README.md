﻿# Blocklists-Whitelists
 
 This is a repository of my own custom lists that I'm using with pfBlockerNG (for pfSense). Some lists might also be useful for Pihole.
 
 
 
 ## NoVPN
 The NoVPN list is a list I've developed for streaming services that don't allow VPN connections.  My entire network is connected to a VPN in pfSense so I've created rules that allow certain domains to bypass the VPN, allowing Amazon Prime Video, Hulu, etc. to keep working. 
 
 Amazon Prime is the most annoying about this because anytime you load the site, it connects to an unnecessary number of servers and if, to any of those servers, your IP is the VPN's, "sorry you're connected using a VPN you can't watch shit". The IP addresses of these many servers change CONSTANTLY So I usually have to run PfBlockerNG's Update > IP before I watch Amazon Prime Video. This is annoying but I don't watch things on Prime that much so fuck them. 

To use the list, go to pfBlockerNG > IP > IPv4. Add a new list whose "action" is "Alias Native". Source my NoVPN.txt (make sure to use the raw list), update as frequently as possible.