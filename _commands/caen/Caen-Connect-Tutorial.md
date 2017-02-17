---
---

Caen Connect Tutorial
-------

Caen Connect Tutorial walks through with you the way to sync your local project folder to your remote CAEN (Linux) machine instantly using SFTP, so you could ssh into CAEN, and do the stuff that you want CAEN to do.


<!--more-->

***NOTE: BEFORE you read the rest of the tutorial, MAKE SURE that you are a student attending the University of Michigan, Ann Arbor (preferably a College of Engineering student). Though this tutorial may also apply to other similar situations, it will be your responbility to learn to adapt. Cheers =P***

<img src="http://mobileapps.its.umich.edu/sites/all/themes/umzentwo/images/umich-app-icon.png" alt="Umich" style="width: 100px; height: 100px;"><br>

## Introduction

**Caen Connect Tutorial** walks through with you the way to sync your local project folder to your remote CAEN (Linux) machine **instantly** using **SFTP**, so you could ssh into CAEN, and do the stuff that you want CAEN to do.

## Possible Cases of Usage

Possible scenarios of use including:

- You are sitting in your dorm, developing your EECS484 project 01/02/03/04, and you want to develop **locally** using you favorite text editor (let's say [sublime text](https://www.sublimetext.com)) due to its reach functionality in auto-completion, syntax highlighting, auto-correction, auto-write-the-whole-project-so-I-could-just-sit-there-and-do-nothing, etc. But, sadly, you can only run your code on CAEN since only CAEN can run ***sqlplus***. You are too lazy to get out of the couch, go to duder/BBB and get a CAEN machine, and start working. But you have to get your code there. Shoot!
- You are, again, writing your C++ code for EECS281/482/483/4xx projects **locally**. At the end of the spec, the instructor want you to run your code in this specific version of ***g++*** (let's say 4.8.5) on a Linux machine (possibly using some Linux system calls so a Mac/PC is simply not going to get you there). But you don't have Linux installed locally. Even if you do, you find that the **g++** version is 5.1.5 and there is no way for you to downgrade it. ONLY CAEN runs **g++** 4.8.5. Shoot!
- You have a remote Linux machine that is so so so powerful, why installing my own Linux? But how do I get my code up there? Shoot!

## Make It Happen

Now, to make this happen, all you need is a [sublime text](https://www.sublimetext.com) editor (More text editor options are to come as soon as I figure them out).


#### Some Preparations
1. Go ahead to [www.sublimetext.com](https://www.sublimetext.com) to get the latest version of sublime text installed on your machine (Mac/PC/Linux). Note that it doesn't matter whether you install version 2 or 3. They all works. (Skip if you already have done it in the past.)
2. Install **Package Control**. [Here](https://packagecontrol.io/installation)'s how you could do it, or you could google it by yourself. (Skip if you already have done it in the past.)
3. Hit `Cmd-Shift-P` if you are working on a Mac (`Ctrl-Shift-P` on PC) to open up the prompt. Type `Install Package` and hit `Enter`. In the next prompt, type **`SFTP`** and hit `Enter`. The installation will perform automatically. Restart your editor after this.

#### Real Magic
1. **Configurations**

	Open up your **root/parent project directory** (where you put all your project folders for this course) and create a new json file named **`sftp-config.json`**. Open it up, and copy-paste in [this](https://github.com/lxieyang/caen-connect-tutorial/blob/master/sftp-config.example.json) piece of code.

	<img src="https://image.ibb.co/bNvvfa/json.png" style="width: 100%" alt="sync">


	Then, change all instances of `your-uniqname`s to your actual **uniqname**, change all instances of `your-password` to your **CAEN password**, change all instances of `path/to/your/project/folder` to where you want to put your project on CAEN. Now, go ahead and save it.

	A sample config file can also be found here: [sftp-config.example.json](https://raw.githubusercontent.com/lxieyang/caen-connect-tutorial/master/sftp-config.example.json)

	To explain a bit:
	- `upload_on_save` will automatically upload the entire root/parent project folder to CAEN.

	- `user` specifies whose CAEN account to upload your project to

	- `password` specifies your password to CAEN

	- `remote_path` specifies where your project folder is located on CAEN

	- More configurations could be found here: [Sublime SFTP Settings](https://wbond.net/sublime_packages/sftp/settings#Settings)

2. **Upload on save**

	Now, congratulations! You are almost there! Open up your root/parent project directory in sublime text. Actually create a project folder to hold all your project files (let's say `eecs484-project-01`). Change directory into it, create a file in it, do some edits, and click **File => Save** (or **`Cmd-S`** in Mac). This will automatically upload the file you just created to CAEN. Automatically. Automatically. ***(No need to email yourself the code and download it from CAEN / push your code to github and pull it on CAEN / copy your file into a flash drive and stick it onto a CAEN machine / etc)***.

3. **Sync Local -> Remote**

	Note that `upload_on_save` will dumbly upload each file you saved to CAEN. But if you delete it / rename it locally, the version on CAEN persists. This may cause serious problems like ***multiple includes, naming conflict, etc***. To save, you could use the **Sync** functionality of **Sublime SFTP**. To do this: **Right click** on your project folder, select **SFTP/FTP** => **Sync Local -> Remote**. It's illustrated below:

	<img src="https://image.ibb.co/cQ2nrF/sync.jpg" style="width: 100%" alt="sync">

	Go ahead and select `Yes` when asked for confirmation. This syncs the local folder with the remote one on CAEN, meaning, everything in your project folder on CAEN machine is now **identical** to the ones in your local project folder. Yay!

4. **Run your project on CAEN**

	Now is the time you **ssh**(remote log in) onto CAEN Linux and run your porjects! To remote log in your CAEN Linux account, please type the following script into your terminal:

	```sh
	ssh your-uniqname@login-course.engin.umich.edu
	```

	Please change `your-uniqname` to your actual **uniqname**. I assume you could take it from here =P

5. **Other possibilities**

	Note that there are other possibilities to explore with ***Sublime SFTP***. What I gave you is just the **[MVP](https://en.wikipedia.org/wiki/Minimum_viable_product)**, so you could get going on the rest of your journey.


## Things to Keep in Mind

#### Version Control
Please do not forget to do version controls, such as [git](https://en.wikipedia.org/wiki/Git), when working with SFTP. Somewhere down the line, when you accidently chose to ***Sync Remote -> Local*** or whatever operations that completely messes up / wipes out your local **repo** (notice that I use the word **repo** here, and you should know what I mean by that), **git** will save you. ***Please refrain from any impulse to curse me if you don't have your project git-ted. I told you to git it. I told you.***

When using git, please add `sftp-config.json` to your `.gitignore` file before you commit to a remote repository ***(you don't want to expose your password to other folks right?)***.

#### Your ideas?
Please shoot me an [email](mailto:lxieyang@umich.edu) to remind me of anything you can think of that should be kept in mind when using SFTP. I would update this tutorial regularly and rest assured your contribution will be referenced and highlighted. I truly appreciate your effort in helping more folks live their life more easily.

## Quick Start
To practice before messing up with your code/projects, you could:

- Instal Sublime Text
- Install Package Control
- Clone this repo, and change the filename `sftp-config.example.json` to `sftp-config.json`. Modify its content according to the instructions above.
- **Git** the folder!
- Play with the stuff in [`sample-project`](https://github.com/lxieyang/caen-connect-tutorial/tree/master/sample-project) on CAEN! Best wishes!


## Contributors
- Special thanks to **Joshua Agby** for:
	- pointting out that the name of the plugin is actually `SFTP` instead of `Sublime SFTP`. So please type `SFTP` when searching for the plugin in your package control.
	- providing an alternative `remote_path` in case of the `Folder does not exist` error, which is `/your-uniqname/path/to/your/project/folder`.

## About
I created this tutorial when I was TAing **EECS484 Database Management Systems** at the University of Michigan, Ann Arbor. I would expect less situations where we helped you modify the code and you want to run it right afterwards, so you ~~email the latest version to yourself, log into CAEN using VNC, open up a browser, download it, put into the right directory, and then~~ run it.

Hope this could somehow make your life easier.

Best,

[Xieyang](http://lxieyang.github.io)

Last updated: 02/16/2017 19:49:59 EST
