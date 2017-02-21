# infoq Download

If you don't want to watch [infoq](https://www.infoq.com) videos on the website, you can download the slides with this tool and merge the slides with the audio to a video.

## Instructions

- Download the mp3 of the talk you want to see (for example for this excellent talk [Simple made easy](https://www.infoq.com/presentations/Simple-Made-Easy)). Click _Download mp3_ beneath the video and log in to download it.
- Put the downloaded `mp3` file into the `data` folder in this repo
- Execute `./create-video https://www.infoq.com/presentations/Simple-Made-Easy filename_of_the_mp3.mp3 video_filename_you_can_choose.mp4`. (The `mp3` filename is without the `data` prefix)
- The video will reside in `data/video_filename_you_can_choose.mp4`
- Watch the talk