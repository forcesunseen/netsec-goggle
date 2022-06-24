# Netsec Goggle

![](https://media.giphy.com/media/P7s5baPQ6mrrq/giphy.gif)

Goggles are a way to alter the ranking in a search engine. Brave is behind this technology and you should [read more about it](https://github.com/brave/goggles-quickstart).

We were really curious if this could help us to break through all the SEO spam and garbage on the internet and help us be more productive in the information security space. As a starting point we used submissions from /r/netsec to build this Goggle. We intend to incorporate additional sources that give us a strong signal/noise ratio. Currently the Goggle is updated manually, but we plan to automate the process to have an up-to-date Goggle.

## How do I use this?
It's super easy! Just go [here](https://search.brave.com/goggles?goggles_id=https://github.com/forcesunseen/netsec-goggle/blob/master/netsec.goggle) and start searching!

If you like it you can click on "follow" to add it to your Goggles. Once it's added you'll get any updates we make to the Goggle.

## Where are you getting the data from?
Reddit's API is horrible and super limited and after some trial and error using the API and [pushshift.io](https://pushshift.io/) we just couldn't get a full list of submissions with up to date data. Luckily someone has went through the trouble of combining the archive from pushshift.io with updates from the Reddit API into a tool.

We owe it all to [voussoir](https://github.com/voussoir) for the amazing tool, [timesearch](https://github.com/voussoir/timesearch). Thank you so much!

## What algorithim are you using?

You can just take a look within `generate/netsec.py`.

Otherwise, here is what we are doing:

1. Take the URLs with scores of 20 or higher from /r/netsec
2. Parse just the domains (no subdomains)
3. Add up the scores for each unique domain
4. Exclude domains that are in the top 1k
5. Sort by cumulative domain scores
6. Split up the list into thirds and assign a boost of either 4, 3, or 2

This seemed to work pretty well from our testing, but if we come across a better technique maybe we'll update it. We also add some additional items directly into the Goggle to surface technical documentation. This Goggle doesn't have a global `$discard` which means that we will still get other results that don't specifically match. Of course, they will be lower rank over what we boost.

## Can I generate this myself?
Sure, everything you need to generate the Goggle is in this repository. We will try to keep the `generate/urls.txt` file up to date with data from timesearch. The goal will be to create a docker container that will combine all of this. Feel free to play around!

`generate/netsec.py` - Just cd into the directory and run.

`generate/top_1k.txt` - We exclude the top 1k domains. We got this from [here](https://github.com/brave/goggles-quickstart/blob/main/goggles/1k_short.goggle).

`generate/urls.txt` - URLs pulled from submissions on /r/netsec.

## Getting URLs from timesearch
After running timesearch you will have a local SQLite database containing the submissions for /r/netsec. We currently use the following query to pull data: `select score,url from submissions where score >= 20`. As you can see we only pull URLs with a score of 20 or higher to keep low quality content out. We may play around with this value to see if something else works better.
