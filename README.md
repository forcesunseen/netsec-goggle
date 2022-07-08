# Netsec Goggle

![](https://media.giphy.com/media/P7s5baPQ6mrrq/giphy.gif)

Goggles are a way to alter the ranking in a search engine. Brave is behind this technology and you should [read more about it](https://github.com/brave/goggles-quickstart).

We were really curious if this could help us to break through all the SEO spam and garbage on the internet and help us be more productive in the information security space. So we used submissions from /r/netsec as our source to build this Goggle.

You can also read more about this on Forces Unseen's blog: [Make Search Engines Great Again!](https://blog.forcesunseen.com/make-search-engines-great-again)

## How do I use this?
It's super easy! Just go [here](https://search.brave.com/goggles?goggles_id=https://github.com/forcesunseen/netsec-goggle/blob/master/netsec.goggle) and start searching!

If you like it you can click on "follow" to add it to your Goggles. Once it's added you'll get any updates we make to the Goggle.

## How are you generating this?

We created [narwhalizer](https://github.com/forcesunseen/narwhalizer) which can be used to generate Goggles for any subreddit(s).

## What algorithm are you using?

You can take a look at `netsec.env` to see the narwhalizer configuration.

Here is what we are doing from a high level:

1. Take the URLs with scores of 20 or higher from /r/netsec
2. Parse just the domains (no subdomains)
3. Add up the scores for each unique domain
4. Exclude domains that are in the top 1k
5. Sort by cumulative domain scores
6. Split up the list into thirds and assign a boost of either 4, 3, or 2

We also add some additional items directly into the Goggle to surface technical documentation. This Goggle doesn't have a global `$discard` which means that we will still get other results that don't specifically match. Of course, they will be lower rank over what we boost.
