# uBlock Origin Filters

These are some useful filters for cleaning up certain parts of the internet. uBlock already comes with filters that do this sort of thing, like removing cookie notifications or social media hooks added on to other sites (like buttons, comment boxes, etc.)

Add these by specifying the raw file location (will enable all the rules) or by pasting them into "My Filters" in uBlock. The latter method will allow you to remove some bits selectively.

## yt-neuter

[yt-neuter](https://github.com/mchangrh/yt-neuter) contains a lot of filters that disable many components within YouTube. Suggested content, shorts on the main page, the voice search button, popups, surveys. What you're left with is just the videos.

I myself disable some of the filters such as:

- "save to playlist" button
- the "categories" list at the top of the page.

## Youtube adblock filters

[aidenwebb/ublock-origin-youtube-filters](https://github.com/Aidenwebb/ublock-origin-youtube-filters) provides a small set of filters that might have to do with ads or popups. I haven't really tested these much.

## mtxadmin/ublock

[mtxadmin/uBlock](https://github.com/mtxadmin/ublock) is a collection of uBlock Origin filters. Here are ones I'm trying:

- [Microsoft](https://github.com/mtxadmin/ublock/raw/master/filters/microsoft)
- [google filters](https://github.com/mtxadmin/ublock/raw/master/filters/google)
- [stackexchange](https://raw.githubusercontent.com/mtxadmin/ublock/master/filters/stackexchange) filters removes the sidebar (Home, questions, tags, etc), the footer, and maybe some other things I haven't noticed. I removed all the stuff related to Russian versions of the site since I'll never be viewing those. This came from mtxadmin/ublock (see below)
- [third party ad network cookies](https://github.com/mtxadmin/ublock/raw/master/filters/_cookies)
- [URL parameters](https://github.com/mtxadmin/ublock/raw/master/filters/_removeparams) removes parameters from URLs related to ads and tracking
