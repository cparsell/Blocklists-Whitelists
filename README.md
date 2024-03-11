# Blocklists-Whitelists

This is a reference repository for web filtering (ads, tracking, etc). The files listed are some lists I've made - they are specific to things I've either blocked or whitelisted so they will not work perfectly for you but they might be a place to start. As a general rule, host lists should be updated regularly so do not use host lists that have not been updated recently (within days or weeks).

### Whitelist

The whitelist I've included is what I've built up over time for myself. If you want to add it, or another whitelist, into Pihole there is no way to import an entire list. So I wrote a very short Python script for this. It will run through a downloaded text file and push each line into Pihole.

Other whitelists:

- Anudeep ND Whitelist ([domains](https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt)) ([homepage](https://github.com/anudeepND/whitelist))
- [Commonly whitelisted domains - Pi-hole Forum](https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212)
- [hl2guide's Adguard Home Whitelist](https://github.com/hl2guide/AdGuard-Home-Whitelist) and some block lists as well

## Types of blocklists

### Hosts lists (Pihole, Adguard Home, and PfBlockerNG compatible)

Below are some lists I've used. I've experimented with Pihole, PfBlockerNG(for pfSense), AdGuard Home, as well as browser-based filtering like Brave Browser or Adguard extension. So I've included lists of different formats.

"Hosts lists" just list domains. Use these for DNS blockers like Pihole, Adguard Home, or PfBlockerNG.

> 0.0.0.0 www.pixel.ad
>
> www.pixel.ad
> Both of these ways are used in hosts lists. They both should be able to be interpreted by DNS blockers.

### Filter lists (browser-based)

Browser-based adblockers are able to filter content _within webpages_ as they are being loaded. So these are lists of patterns in websites themselves. This allows things like blocking annoying cookie messages or popups telling you that you are using and adblocker. For this reason, I use a browser-based blocker as well as a DNS blocker. Brave Browser's built-in adblocker, AdGuard browser extension, and AdBlock Plus are ones I've used.

These are typical of these kind of filtering rule lists. These are not compatible with Pihole, PfBlockerNG, or AdGuard Home (DNS blockers):

> .adnetwork.$domain=~adnetwork.ie|~adnetwork.sk

> /ad_display.

> /banners/ads/\*

### IP Block Lists (pfBlockerNG for pfSense)

These are lists of IP addresses. The firewall (pfSense) will refuse outbound or inbound connections to any IP adddresses in the list. One can use cybersecurity feeds as a preventative measure against trojans, botnet malware, and other garbage.

### Regex Filters

It takes longer for systems to process regex filters than to search through a tree structure database of millions of domains. See [this post](https://discourse.pi-hole.net/t/collection-of-regex-for-blacklisting/43178/10) for some explanation of why. Still, this is comparing sub-millisecond timing to a handful of milliseconds. But for this reason, I still only try to use regex filters that are relevant to me. I have a collection of many regex filters I've found around the internet, but my "pared down" file is of ones that match domains in my own logs.

Regex lists: [mmoti](https://github.com/mmotti/pihole-regex/blob/master/regex.list), [Smart TV regex](https://perflyst.github.io/PiHoleBlocklist/regex.list)

Tools: [Regex101](https://regex101.com/), [Regexr](https://regexr.com/)

## Lists

### Lists of lists

- [Firebog](https://firebog.net/) - Adblocking, malicious site lists, tracking, etc.
- [Developer Dan](https://www.github.developerdan.com/hosts/)
- [Developer Dan's blocklist search tool](https://blocklist-tools.developerdan.com/entries/search) - use to search for a domain name to see if it exists in any of the major blocklists out there
- [Blocklist.site](https://blocklist.site/)
- [OISD](https://oisd.nl/)
- [Nocturnal Archives](https://github.com/nocturnalarchives/BlockLists) - some niche lists like Amazon blocklist, Netflix, a decent regex rule list
- [Avoid the Hack](https://avoidthehack.com/best-pihole-blocklists)

### Host Lists

- [AdGuard DNS list](https://v.firebog.net/hosts/AdguardDNS.txt) - formatted as a hosts list
- [Steven Black hostslist](https://github.com/StevenBlack/hosts/raw/master/hosts) - A standard
- [Easylist, just the domains](https://v.firebog.net/hosts/Easylist.txt)
- [Developer Dan's Ad & Tracking list](https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt)
- [OISD Big](https://big.oisd.nl/domains) - a list made of many other blocklists, hosts list formatted
- [OISD Small](https://small.oisd.nl/domains) - a smaller list made of many other lists, hosts list - formatted
- [YouTube Ad blocklist](https://raw.githubusercontent.com/Ewpratten/youtube_ad_blocklist/master/blocklist.txt) (hasn't been updated in 2 yrs)
- [Dan Pollock's host list](https://someonewhocares.org/hosts/zero/hosts)
- [Adaway adblock host list](https://adaway.org/hosts.txt)
- [AnudeepND adblock list](https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt)
- [Firebog suspicious hosts list](https://v.firebog.net/hosts/static/w3kbl.txt)
- [DoH Great Wall](https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall.txt) - some software will use DNS-over-HTTPS to route around Pihole/etc
- [DNS-over-HTTPS blocklist](https://github.com/curl/curl/wiki/DNS-over-HTTPS) - another DoH blocklist
- [Public DNS servers](https://raw.githubusercontent.com/nocturnalarchives/BlockLists/master/public-dns-servers.txt)
- [Developer Dan's Google AMP host list](https://www.github.developerdan.com/hosts/lists/amp-hosts-extended.txt) ([article about why they're bad](https://www.theregister.com/2017/05/19/open_source_insider_google_amp_bad_bad_bad/))
- [Threat hostlists](https://github.com/PeterDaveHello/threat-hostlist)
- [urlhaus](https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-hosts-online.txt) host lists - see [urlhaus gitlab page](https://gitlab.com/malware-filter/urlhaus-filter) for browser filter lists, versions for PiHole, AdGuard, etc.

## AdGuard Home filters

-

### Browser-based Filtering

- [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb)
- [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- [AdGuard _browser extension_](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg)
- [Brave Browser](https://brave.com/download/)
  uBlock Origin and AdBlock Plus are very customizable. Brave Browser is as well (**brave://adblock** in the browser). In Brave Browser, you can add filter lists, however there is a custom filters area that seems to be non-functional at the time of writing.
- [AdGuard DNS list](https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt)
- [Easylist](https://easylist.to/easylist/easylist.txt)
- [Easylist - no adult](https://easylist-downloads.adblockplus.org/easylist_noadult.txt) variant without rules for adult sites
- [Easyprivacy](https://easylist.to/easylist/easyprivacy.txt) is an optional supplementary filter list that completely removes all forms of tracking from the internet
- [Easylist Cookie List](https://secure.fanboy.co.nz/fanboy-cookiemonster.txt) blocks cookies banners, GDPR overlay windows, etc.
- [Fanboy's Social Blocking List](https://easylist.to/easylist/fanboy-social.txt) - removes like buttons and othe social media widgets from websites
- [Fanboy's Annoyance List](https://secure.fanboy.co.nz/fanboy-annoyance.txt) - blocks Social Media content, in-page pop-ups and other annoyances
- [Adblock Warning Removal List](https://easylist-downloads.adblockplus.org/antiadblockfilters.txt) specifically removes obtrusive messages and warnings targeted to users who use an adblocker.
- [Mobile Ads](https://raw.githubusercontent.com/YanFung/Ads/master/Mobile) # Mobile Ads - does have some domains so it might be useable with DNS blockers

### IP Block Lists

- [Public DNS servers](https://public-dns.info/nameservers.txt)
- [DoH Great Wall IP list](https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall_ipv4)
- [Spamhaus DROP (Don't Route or Peer) List](https://www.spamhaus.org/drop/drop.txt) consists of netblocks that are "hijacked" or leased by professional spam or cyber-crime operations (used for dissemination of malware, trojan downloaders, botnet controllers).
- [Spamhaus EDROP List](http://www.spamhaus.org/drop/edrop.txt)
- [DShield Most Active Attacking IPs](http://feeds.dshield.org/top10-2.txt)
