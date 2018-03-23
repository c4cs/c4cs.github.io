---
---
ffmpeg
----

`ffmpeg` is a multimedia framework used to record, convert, and stream audio and video.

<!-- minimal example -->
~~~ bash
# Convert between filetypes
$ ffmpeg -i input.mp4 output.avi
~~~

<!--more-->

### Useful Options / Examples

``` bash
$ ffmpeg -i input.mp4 output.avi
```

A simple command to convert from one encoding format to another.

``` bash
$ ffmpeg -i input.mp3 output.wav
```

The same as above, but with audio instead of video.

``` bash
$ ffmpeg -i input.avi -r 24 output.avi
```

the `-r` flag specifies the desired output framerate in fps. This example is converting whatever framerate `input.avi` is to a 24fps .avi output.

``` bash
$ ffmpeg -i input.mp4 -vf fps=1/60 screenshot%d.png
```

This gets stills of a .mp4 every second and call them `screenshot[NUM].png`. It stores them in the current directory.

``` bash
$ ffmpeg -f image2 -pattern_type glob -framerate 12 -i 'still-*.jpeg' -s WxH output.avi
```

Alternatively, you can turn a bunch of images that you have into a video. Here `image2` is a required format, a 12 fps video `output.avi` is being created from all images that follow the file naming pattern `still-*.jpeg`.

``` bash
$ ffmpeg -i input.mp4 -ss 00:00:25 -codec copy -t 40 output.mp4
```

This cuts the video file into a clip. The `-ss` tells it the starting time, here 25 seconds, and the `-t` tells it how much of the clip you want, so here 40 seconds.

This can also work to split the whole file into multiple smaller files as shown below.

``` bash
$ ffmpeg -i input.mp4 -t 00:00:41 -c copy part1.mp4 -ss 00:00:59 -codec copy part2.mp4
```

In this case `-t 00:00:41` shows a part that is created from the start of the video to the 41st second of video. `-ss 00:00:59` shows the starting time stamp for the video. It means that the 2nd part will start from the 59th second and will continue up to the end of the original file.

You can also join various video/audio files together.

``` bash
$ ffmpeg -f concat -i file-list.txt -c copy output.mp4
```

where `file-list.txt` is a list of files **with the same codec** that are to be joined together, eg.

```
file '/Users/USER_NAME/Documents/movie_parts/part1.mp4'
file '/Users/USER_NAME/Documents/movie_parts/part2.mp4'
file '/Users/USER_NAME/Documents/movie_parts/part3.mp4'
file '/Users/USER_NAME/Documents/movie_parts/part4.mp4'
```
