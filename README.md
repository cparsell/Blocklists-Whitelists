# Blocklists-Whitelists 
 
 This is a reference repository for web filtering (ads, tracking, etc). The files listed are some lists I've made - they are specific to things I've either blocked or whitelisted so they will not work perfectly for you but they might be a place to start.

 ### Whitelist
 The whitelist I've included is what I've built up over time for myself. If you want to add it, or another whitelist, into Pihole there is no way to import an entire list. So I wrote a very short Python script for this. It will run through a downloaded text file and push each line into Pihole. 

 Other whitelists:
 - Anudeep ND Whitelist ([domains](https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt)) ([homepage](https://github.com/anudeepND/whitelist))
 - [Commonly whitelisted domains - Pi-hole Forum](https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212)
 
## Types of blocklists

 ### Hosts lists (Pihole, Adguard Home, and PfBlockerNG compatible)
Below are some lists I've used. I've experimented with Pihole, PfBlockerNG(for pfSense), AdGuard Home, as well as browser-based filtering like Brave Browser or Adguard extension. So I've included lists of different formats. 

"Hosts lists" are lists that just list domains. Use these for DNS blockers like Pihole, Adguard Home, or PfBlockerNG. 
> 0.0.0.0 www.pixel.ad
> 
> www.pixel.ad
Both of these ways are used in hosts lists. They both should be able to be interpretted by DNS blockers.

### Filter lists (browser-based)
Browser-based adblockers are able to filter content *within webpages* as they are being loaded. So these are lists of patterns in websites themselves. This allows things like blocking annoying cookie messages or popups telling you that you are using and adblocker. For this reason, I use a browser-based blocker as well as a DNS blocker. Brave Browser's built-in adblocker, AdGuard browser extension, and AdBlock Plus are ones I've used.

These are typical of these kind of filtering rule lists. These are not compatible with Pihole, PfBlockerNG, or AdGuard Home (DNS blockers):
> .adnetwork.$domain=~adnetwork.ie|~adnetwork.sk
>
> /ad_display.
>
> /banners/ads/*

### Regex Filters
It takes longer for systems to process regex filters than to search through a tree structure database of millions of domains. See [this post](https://discourse.pi-hole.net/t/collection-of-regex-for-blacklisting/43178/10) for some explanation of why. Still, this is comparing sub-millisecond timing to a handful of milliseconds. But for this reason, I still only try to use regex filters that are relevant to me. I have a collection of many regex filters I've found around the internet, but my "pared down" file is of ones that match domains in my own logs.

Regex lists: [mmoti](https://github.com/mmotti/pihole-regex/blob/master/regex.list), [Smart TV regex](https://perflyst.github.io/PiHoleBlocklist/regex.list)
Tools: [Regex101](https://regex101.com/), [Regexr](https://regexr.com/)



## Lists
### Lists of lists
- [Firebog](https://firebog.net/)   # Adblocking, malicious site lists, tracking, etc.
- [Developer Dan](https://www.github.developerdan.com/hosts/)
- [Developer Dan's blocklist search tool](https://blocklist-tools.developerdan.com/entries/search) - use to search for a domain name to see if it exists in any of the major blocklists out there
- [Blocklist.site](https://blocklist.site/)
- [OISD](https://oisd.nl/)
- [Nocturnal Archives](https://github.com/nocturnalarchives/BlockLists) - some niche lists like Amazon blocklist, Netflix, a decent regex rule list
- [Avoid the Hack](https://avoidthehack.com/best-pihole-blocklists)

### Host Lists
- https://v.firebog.net/hosts/AdguardDNS.txt   # AdGuard DNS list, formatted as a hosts list
- https://github.com/StevenBlack/hosts/raw/master/hosts      # Steven blackcake
- https://v.firebog.net/hosts/Easylist.txt # Easylist, just the domains
- https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt  # Developer Dan's Ad & Tracking list
- https://big.oisd.nl/domains # OISD Big - a list made of many other blocklists, hosts list formatted
- https://small.oisd.nl/domains # OISD Small - a smaller list made of many other lists, hosts list - formatted
- https://raw.githubusercontent.com/Ewpratten/youtube_ad_blocklist/master/blocklist.txt # YouTube Ad blocklist (hasn't been updated in 2 yrs)
- https://someonewhocares.org/hosts/zero/hosts # Dan Pollock's host list
- https://adaway.org/hosts.txt # Adaway adblock host list
- https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt # AnudeepND adblock list
- https://v.firebog.net/hosts/static/w3kbl.txt # Firebog suspicious hosts list
- https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall.txt # DoH Great Wall some software will use DNS-over-HTTPS to route around Pihole/etc
- https://github.com/curl/curl/wiki/DNS-over-HTTPS # DNS-over-HTTPS servers - another DoH blocklist
- https://raw.githubusercontent.com/nocturnalarchives/BlockLists/master/public-dns-servers.txt # Public DNS servers
- https://www.github.developerdan.com/hosts/lists/amp-hosts-extended.txt # Developer Dan's Google AMP host list ([article about why they're bad](https://www.theregister.com/2017/05/19/open_source_insider_google_amp_bad_bad_bad/))

## AdGuard Home filters
- https://big.oisd.nl  # OISD Big list - a list made of many other blocklists, formatted for AdBlock Home filtering rules

### Browser-based Filtering
Adblock Plus, AdGuard *browser extension*, Brave Browser (**brave://adblock** in the browser)
- https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt   # AdGuard DNS list
- https://easylist.to/easylist/easylist.txt  # Easylist
- https://easylist-downloads.adblockplus.org/easylist_noadult.txt # Easylist variant without rules for adult sites
- https://easylist.to/easylist/easyprivacy.txt # Easyprivacy  is an optional supplementary filter list that completely removes all forms of tracking from the internet
- https://secure.fanboy.co.nz/fanboy-cookiemonster.txt # Easylist Cookie List - blocks cookies banners, GDPR overlay windows, etc.
- https://easylist.to/easylist/fanboy-social.txt # Fanboy's Social Blocking List - removes like buttons and othe social media widgets from websites
- https://secure.fanboy.co.nz/fanboy-annoyance.txt # Fanboy's Annoyance List - blocks Social Media content, in-page pop-ups and other annoyances
- https://easylist-downloads.adblockplus.org/antiadblockfilters.txt # Adblock Warning Removal List specifically removes obtrusive messages and warnings targeted to users who use an adblocker.
- https://raw.githubusercontent.com/YanFung/Ads/master/Mobile   # Mobile Ads - does have some domains so it might be useable with DNS blockers

### IP Block Lists
- https://public-dns.info/nameservers.txt # Public DNS servers
- https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall_ipv4 # DoH Great Wall IP list
 
