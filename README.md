# Blocklists-Whitelists

This is a reference repository for adblocking tools and settings (ads, tracking, etc). The text files are backups of filter lists I've uses in Pi-Hole, AdGuard, pfBlockerNG, and uBlock. So they are specific to to my setup - they may not work perfectly for you but they might be a place to start.

As a general rule, if you find a blocklist that has not been updated recently (within days or weeks) then it's probably not being maintained anymore. Move on to ones that are well maintained.

## Whitelist

Whitelists tell the adblock what not to block. The whitelist I've included is what I've built up over time for myself.

In Pi-hole there is no way to import an entire whitelist. So I've included a very short Python script that automates this. It will run through a downloaded text file and push each line into Pi-hole's whitelist.

#### Other whitelists:

- Anudeep ND Whitelist ([domains](https://raw.githubusercontent.com/anudeepND/whitelist/master/domains/whitelist.txt)) ([homepage](https://github.com/anudeepND/whitelist))
- [Commonly whitelisted domains - Pi-hole Forum](https://discourse.pi-hole.net/t/commonly-whitelisted-domains/212)
- [hl2guide's Adguard Home Whitelist](https://github.com/hl2guide/AdGuard-Home-Whitelist) and some block lists as well

## Hosts files (**Pihole**, **Adguard Home**, and **PfBlockerNG** compatible)

Every OS has a file called `Hosts` that it uses to map hostnames to IP addresses. Rewriting a hostname to 0.0.0.0 makes it inaccessible, blocking it. You can use these with DNS blockers like Pihole, Adguard Home, or PfBlockerNG.

**Hosts file example**

```
# Comment
0.0.0.0 www.pixel.ad
127.0.0.1 my.selfhosted.lan
```

**Domain lists are simply text files with domains in them**

```
# Comment
www.pixel.ad
```

### Hosts files and domain lists

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

## Browser-based Filtering (for **web browser adblockers**)

**Filter lists** are lists of patterns within webpages themselves. This allows things like blocking cookie messages, popups, or social media "like" buttons. Using a DNS blocker and a browser adblocker together works well. Brave Browser's built-in adblocker, AdGuard browser extension, and AdBlock Plus are ones I've used.

These are typical of these kind of filtering rule lists. These are not compatible with Pi-hole, PfBlockerNG, or AdGuard Home (DNS blockers):

**Filters**

```
! Comment
.adnetwork.$domain=~adnetwork.ie|~adnetwork.sk
/ad_display.
/banners/ads/\*
/admanager/*$~object,domain=~admanager.line.biz|~blog.google|~sevio.com
###aniview--player
||netinsight.co.kr^$third-party
bleedingcool.com##.post_content_spacer
```

### Browser Adblockers

- [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb)
- [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- [AdGuard _browser extension_](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg)
- [Brave Browser](https://brave.com/download/)
  uBlock Origin and AdBlock Plus are very customizable. Brave Browser is as well (`brave://adblock` in the browser). There you can add you can add filter lists as well as individual custom filters.

### Filter lists:

- [AdGuard DNS list](https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt)
- [Easylist](https://easylist.to/easylist/easylist.txt)
- [Easylist - no adult](https://easylist-downloads.adblockplus.org/easylist_noadult.txt) variant without rules for adult sites
- [Easyprivacy](https://easylist.to/easylist/easyprivacy.txt) is an optional supplementary filter list that completely removes all forms of tracking from the internet
- [Easylist Cookie List](https://secure.fanboy.co.nz/fanboy-cookiemonster.txt) blocks cookies banners, GDPR overlay windows, etc.
- [Fanboy's Social Blocking List](https://easylist.to/easylist/fanboy-social.txt) - removes like buttons and othe social media widgets from websites
- [Fanboy's Annoyance List](https://secure.fanboy.co.nz/fanboy-annoyance.txt) - blocks Social Media content, in-page pop-ups and other annoyances
- [Adblock Warning Removal List](https://easylist-downloads.adblockplus.org/antiadblockfilters.txt) specifically removes obtrusive messages and warnings targeted to users who use an adblocker.
- [Mobile Ads](https://raw.githubusercontent.com/YanFung/Ads/master/Mobile) # Mobile Ads - does have some domains so it might be useable with DNS blockers

## IP Block Lists (pfBlockerNG for pfSense)

These are lists of IP addresses. The firewall (pfSense) will refuse outbound or inbound connections to any IP adddresses in the list. One can use cybersecurity feeds as a preventative measure against trojans, botnet malware, and other garbage.

```
# Some are listed as singular IP addresses
1.117.3.64
1.12.254.218
1.12.60.59

# Some are listed as IP subnet masks
5.42.92.0/24

# Some are written as IP ranges
193.41.206.0	193.41.206.255	24	749	-	-	-
167.94.145.0	167.94.145.255	24	707	CENSYS-ARIN-02	US	None
194.169.175.0	194.169.175.255	24	706	AS-MATRIXTELECOM	GB	>>UNKNOWN<<
```

### IP Blocklists:

- [Public DNS servers](https://public-dns.info/nameservers.txt)
- [DoH Great Wall IP list](https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall_ipv4)
- [Spamhaus DROP (Don't Route or Peer) List](https://www.spamhaus.org/drop/drop.txt) consists of netblocks that are "hijacked" or leased by professional spam or cyber-crime operations (used for dissemination of malware, trojan downloaders, botnet controllers).
- [Spamhaus EDROP List](http://www.spamhaus.org/drop/edrop.txt)
- [DShield Most Active Attacking IPs](http://feeds.dshield.org/top10-2.txt)

## Regex Filters

Some DNS blockers allow the use of regular expressions in order to describe patterns of hostnames. For example, `/lgad.*/` will block `lgad.foo.com` as well as `foo.lgad.bar.net`.

It is a good idea to be minimal about how many regex filters you use. It takes longer for systems to process regex filters than to search through millions of domains. See [this post](https://discourse.pi-hole.net/t/collection-of-regex-for-blacklisting/43178/10) for more a detailed explanation. I only try to use regex filters that are relevant to me.

Regex lists:

- [mmoti](https://github.com/mmotti/pihole-regex/blob/master/regex.list),
- [Smart TV regex](https://perflyst.github.io/PiHoleBlocklist/regex.list)

Tools:

- [Regex101](https://regex101.com/),
- [Regexr](https://regexr.com/)

## Lists of lists

- [Firebog](https://firebog.net/) - Adblocking, malicious site lists, tracking, etc.
- [Developer Dan](https://www.github.developerdan.com/hosts/)
- [Developer Dan's blocklist search tool](https://blocklist-tools.developerdan.com/entries/search) - was a helpful tool that allowed searching for a domain in most of the popular blocklists. It was helpful if I was going through my own network query log to see if something is blocked by any of the lists out there. It seems to no longer be maintained. The https://github.com/blocklist-tools is available.
- [Blocklist.site](https://blocklist.site/)
- [OISD](https://oisd.nl/)
- [Nocturnal Archives](https://github.com/nocturnalarchives/BlockLists) - some niche lists like Amazon blocklist, Netflix, a decent regex rule list
- [Avoid the Hack](https://avoidthehack.com/best-pihole-blocklists)
