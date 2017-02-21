#!/usr/bin/env python3

import helper

OUT = 'ffconcat.txt'
IN_TIMES = 'times.txt'
IN_SLIDES = 'slides.txt'


def main():
    # Ignore first "time"
    times = helper.get_txt(IN_TIMES)[1:]
    slides = download_slides(helper.get_txt(IN_SLIDES))
    assert(len(times) == len(slides))
    last_time = 0
    out = ['ffconcat version 1.0']
    for time, slide in zip(times, slides):
        time = int(time)
        duration = time - last_time
        out.append("file {}\nduration {}".format(slide, duration))
        last_time = time

    with open(OUT, 'w') as f:
        f.write('\n'.join(out))


def download_slides(slides_remote):
    slides = []
    for slide in slides_remote:
        filename = "slides/{}".format(slide.split('/')[-1])
        helper.download_file(slide, filename)
        slides.append(filename)
    return slides


if __name__ == '__main__':
    main()
