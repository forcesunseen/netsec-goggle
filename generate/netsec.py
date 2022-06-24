#!/usr/bin/env python3

import tldextract
from collections import defaultdict

GOGGLE_HEADER = """! name: Netsec
! description: High signal information security sources.
! public: true
! author: Forces Unseen
! avatar: #01ebae
! homepage: https://github.com/forcesunseen/netsec-goggle

! Additional boost items
$boost=2,site=github.io
$boost=2,site=github.com
$boost=2,site=stackoverflow.com
/blog.$boost=2
/blog/$boost=2
/docs.$boost=2
/docs/$boost=2
/doc/$boost=2
/Doc/$boost=2
/manual/$boost=2
"""


def boost(amt):
    """Boost a site by an integer amount.
    """
    return f'$boost={amt},site='

def sort_domains(csv):
    """Parse URLs and return sorted list of domains with exclusions.
    """
    with open('top_1k.txt', 'r') as excludefile:
        exclude_list = excludefile.read().splitlines()
        domains = defaultdict(lambda: 0)
        for item in csv:
            score, url = item.split(', ')
            extracted = tldextract.extract(url)

            # Double check that we have a real domain
            if extracted[1] and extracted[2]:
                domain = '.'.join(extracted[1:]).lower()
                if domain not in exclude_list:
                    domains[domain] += int(score)
    sorted_domains = sorted(
        domains.items(), key=lambda item: item[1], reverse=True)
    return sorted_domains


def generate(domains):
    """Generate rankings in goggle format.
    """
    print(GOGGLE_HEADER, end='')
    entries = len(domains)

    print('\n! Boost /r/netsec submissions')
    for item in range(len(domains)):
        domain = domains[item][0]
        place = item/entries
        if place <= 0.33:
            print(boost(4) + domain)
        elif place <= 0.66:
            print(boost(3) + domain)
        else:
            print(boost(2) + domain)


# Start here
with open('urls.txt', 'r') as csvfile:
    csv = csvfile.read().splitlines()
    sorted_domains = sort_domains(csv)
    generate(sorted_domains)
