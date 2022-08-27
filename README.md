# Blocklists-Whitelists
 
 This is a repository of my own custom lists that I'm using with pfBlockerNG (for pfSense). Some lists might also be useful for Pihole.
 
 
 
 ## NoVPN
 The NoVPN list is a list I've developed for streaming services that don't allow VPN connections.  My entire network is connected to a VPN in pfSense so I've created rules that allow certain domains to bypass the VPN, allowing Amazon Prime Video, Hulu, etc. to keep working. 
 
 Amazon Prime is the most annoying about this because anytime you load the site, it connects to an unnecessary number of servers and if, to any of those servers, your IP is the VPN's, "sorry you're connected using a VPN you can't watch shit". The IP addresses of these many servers change CONSTANTLY So I usually have to run PfBlockerNG's Update > IP before I watch Amazon Prime Video. This is annoying but I don't watch things on Prime that much so fuck them. 
 

To add the list, go to pfBlockerNG > IP > IPv4. 
- Add a new list whose action is "Alias Native". 
- Source my NoVPN.txt (make sure to use the raw list), 
- update as frequently as possible. 
- Some of these servers in the list might be based on my location so, if it isn't working, you may need to add servers to the list. Use the "IPv4 Custom_List" at the bottom to add additional server names. 
- Save

- Go to PFBlockerNG > Update > Reload > IP. Now the Alias has been created.

Then create a rule in your LAN rules (or whichever interface is appropriate):
- action "pass"
- protocol "any", 
- source "any", 
- destination "single host or alias" "pfB_NoVPN_v4" should be what it is called, 
- Advanced Options > Gateway to "whatever your WAN gateway is called".

## Amazon AWS
It is also possible to create a bypass for all Amazon AWS IP addresses. I've experimented with using this but the NoVPN list is still most helpful for my purposes - streaming Prime Video.

Under PfBlockerNG > IP > IPv4, create a new list group called AmazonAWS.  Add 'https://ip-ranges.amazonaws.com/ip-ranges.json' as the source, state "on", format "auto". Action "alias native", update as needed.

Go to PFBlockerNG > Update > Reload > IP. Now the Alias has been created.

Create a rule in LAN rules:
- Action "pass", 
- protocol "any", 
- source "any", 
- destination "single host or alias" "pfB_AmazonAWS_v4" should be what it is called. 
- Advanced Options > Gateway to "whatever your WAN gateway is called". That should allow any AWS through your WAN without the VPN.
- Save
