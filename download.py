#!/usr/bin/env python3

import helper
import re
import os
import argparse

URL = 'https://www.infoq.com/presentations/Simple-Made-Easy'

OUT_TIMES = 'times.txt'
OUT_SLIDES = 'slides.txt'

def main():
    if os.path.exists(OUT_TIMES) and os.path.exists(OUT_SLIDES):
        return

    parser = argparse.ArgumentParser(description="Download infoq slides/times for a video")
    parser.add_argument('url', default=URL)
    args = parser.parse_args()

    slides, times = get_slides_and_times_from_infoq(args.url)
    save(OUT_TIMES, '\n'.join(times))
    save(OUT_SLIDES, '\n'.join(slides))


def get_slides_and_times_from_infoq(url):
    html = helper.get_url(URL).text
    matches = re.findall(r'var slides = new Array\((.*?)\),(?:.*?)TIMES = new Array\((.*?)\)', html, flags=re.S)
    assert(len(matches) == 1)
    assert(len(matches[0]) == 2)
    slides, times = matches[0]
    slides = [x.replace("'", '') for x in split_and_remove_empty_lines(slides)]
    times = split_and_remove_empty_lines(times)
    return slides, times


def save(file, data):
    with open(file, 'w') as f:
        f.write(data)


def split_and_remove_empty_lines(l, delim=','):
    return [x.strip() for x in l.split(delim) if x.strip() != '']

if __name__ == '__main__':
    main()
