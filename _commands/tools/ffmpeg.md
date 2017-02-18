---
---
ffmpeg
----

`ffmpeg` is a command line tool that is used for converting and editing audio and video files. Its reference page can be found [here](https://ffmpeg.org/ffmpeg.html). Install by typing the following command:

~~~ bash
$ sudo apt install ffmpeg
~~~

### File Conversion
One of the simplest commands one can run using ffmpeg involves file type conversion. This is useful for scenarios in which you have, for example, a .mp4 and want to change it to a .avi. This can be done in the following way:

~~~ bash
$ ffmpeg -i sample.avi sample.mp4
~~~

**Break it down**

The first argument, `-i` tells ffmpeg that the next file is the input to the tool. The argument after the input is implicitly interpreted as the output of the program. ffmpeg can tell what type of file you want to convert to just by looking at the extension of the filename that you give it for output. This command does not delete your original file.

The conversion command works for other file types too, just as long as they are compatible (audio to audio, image to image, etc.).

### Converting File Quality
ffmpeg allows you to set how high of a quality you want your conversion to be. There are different settings depending on which file type you are writing to. For converting to .avi, use the `-q` argument followed by a value between 1 and 50. The lower the number, the higher the quality.

~~~ bash
$ ffmpeg -i sample.mp4 -q 12 sample.avi
~~~

If instead you wish to convert to a .mp4, you must use the `-crf` argument. 

~~~ bash
$ ffmpeg -i sample.avi -crf 2 sample.mp4
~~~

### Converting a Video to Many Images
It may be useful to take a video and cut it into a series of images. In order to do this, use the following command:

~~~ bash
$ ffmpeg -i sample.avi -r 1 -s [WxH] -f image2 sample-%d.jpeg
~~~ 

**Break it down**

-  `-i` in this command specifies the input file of sample.avi. 
-  `-r` specifies the framerate for the conversion, in this case we set it to one frame per second. `-s` is used to specify the desired width and height, denoted as [WxH]. So, for example, if you wanted a 1920x1080 image or video, you'd use the argument `-s 1920x1080`. 
-  `-f` tells ffmpeg that you want to **f**orce the file conversion to the specified format encoding, in this case we chose image2 which is used for .jpeg and .png among others.
-  `%d` is called a sequence pattern. This allows you to convert the video into many image files with the same prefix, in this case `sample-`. In our case, if you have a 60 second video, you would end up with 60 images labeled sample-1.jpeg through sample-60.jpeg. You can 0-pad these sequences by using `%d0N` where N - 1 is the number of 0's you want before the number. So if using `%d03` you would see sample-001 instead.

### Filters
The most powerful use of ffmpeg is its `-filter` flag. Let's look at a few examples.

**Volume**

~~~ bash
$ ffmpeg -i sample.avi -filter:a "volume=2" sample.avi
~~~

The `-filter:a` option specifically targets the audio channel of the video file. In this case, we are adjusting the volume by a multiplier of 2. Values smaller than 1 will reduce the volume of the file.

**Channel Remapping**

~~~ bash
$ ffmpeg -i sample.mp3 -filter:a "channelmap=0-0|0-1" sample.mp3
~~~

Again we are using the `-filter:a` flag to target the audio channel of the file. channelmap allows us to map the input of an audio file to a different channel in the output file. A 0 specifies the left channel and a 1 is the right. The format is this: `channelmap=input-input|output-output`. So, you can flip the audio channels by a mapping like this `channelmap=0-1|1-0`. This will take the input left and map it to the ouput right, and vice versa for the input right.

In the above case, we are taking the left input channel and mapping it to the output's left and right channel, which could be useful in "converting" a mono audio file to a stereo one.



