---
title: Compiling Parallel Tracking and Mapping (PTAM) on Mac OS X 10.8.x
location: Lisbon, Portugal
excerpt: Lately, I've been trying to compile numerous Visual SLAM and/or SfM implementations whose source code is publicly available. It has been troublesome, to say the least, and therefore I'm sharing the successful cases, detailing the steps involved.
date: 2013-09-08 03:39
tags: [ptam, slam, computer vision]
categories: [tutorials]
---

Hello all,

Lately, I've been trying to compile numerous Visual SLAM and/or SfM implementations whose source code is publicly available. It has been troublesome, to say the least, and therefore I'm sharing the successful cases, detailing the steps involved.

For my first post, I went for  with PTAM by George Klein and David Murray, released in the proceedings of ISMAR 2007 with the title ["Parallel Tracking and Mapping for Small AR Workspaces"][ptam].

A little disclaimer: 

1. I've only decided to compose this post following the successful compilation of PTAM, so there's a considerable risk that I might not recall some of the steps.
2. Most of this was trial and error, so there may be better aways of accomplish this task (i.e. without installing so many "dependencies")
3. Much of what I did was inspired by this helpful post.

Things to recall throughout the process

* Compile everything for 32 bits i.e. ```./configure CC="gcc -arch i386" CXX="g++ -arch i386"``` is your friend
* Macports is also your friend. A clean way to install and uninstall things. 

## X11

Apple dropped X11 in Mountain Lion, so you need to get the suggested substitute XQuartz from [here][xquartz]. 

## libdc1394

From what I could understand, it is an API to work with IEEE1394 cameras and PTAM uses it. 

1. Download source code from here.
2. Extract and navigate into extracted folder via terminal
3. 
```shell
./configure CC="gcc -arch i386" CXX="g++ -arch i386"
make
sudo make install
```

## Macports

This is a very useful tool. Get it from here. The packages I recall having to install during the process were: ```readline```, ```gstreamer010```, ```gstreamer010-gst-plugins-base``` and ```opencv```.
Some of these take a long time to fetch and compile due to the numerous amount of dependencies. Install them as needed. 

To install a package simply enter in the terminal window

```shell
sudo port install [package_name] +universal
```

The '+universal' is very important, as it will tell macports to also compile 32bit versions of the packages.
Combo: PTAM + Toon + libcvd + gvars3

Get PTAM from [BeLioN repository on github][belion_repo]. In terminal, enter (you need git for this, which can be found in [here][git])

```shell
git clone https://github.com/BeLioN-github/PTAM.git
```

Open and actually read the ```README.txt`` file :) The compile order will be 

1. Toon
2. libcvd
3. gvars3
4. PTAM

## Toon

```shell
cd /<path_to>/PTAM/3rdparty.old/TooN/
./configure CC="gcc -arch i386" CXX="g++ -arch i386" 
make
sudo make install
```
(this may be totally useless since there's nothing to compile ^_^)

## libcvd

This one proved to be troublesome and it is definitely a milestone. If you get past this one, you're halfway there.

1. Get it from: ```git clone git://git.savannah.nongnu.org/libcvd.git```
2. Go to ```/<path_to>/libcvd/cvd/```
3. Edit ```./gl_helpers.h``` and change the lines with 

```c
#include <GL/gl.h> 
#include <GL/glu.h>
```
to

```c
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
```
<ol start="4">
  <li>In the terminal </li>
</ol>


```shell
export CXXFLAGS=-D_REENTRANT
./configure CC="gcc -arch i386" CXX="g++ -arch i386" --without-ffmpeg --x-libraries=/usr/X11/lib --x-includes=/usr/X11/include
make
sudo make install
```

## gvars3

Go to ```/<path_to>/PTAM/3rdparty.old/gvars3/```

```shell
./configure CC="gcc -arch i386" CXX="g++ -arch i386" --disable-widgets
make
sudo make install
```

## PTAM

This was the part where I was forced to install the aforementioned macport packages. Install them as needed. The errors that show up during compilation will give you hints regarding which ones you may be missing.

1. Go to ```/<path_to>/PTAM/Build/OSX/``` and copy the contents to ```/<path_to>/PTAM/```
2. Backup the original ```MAKEFILE``` and open it for edit. 
3. Replace the original lines 6-8 with these

```make
CC = g++ -arch i386
COMPILEFLAGS = ${CPPFLAGS} -D_LINUX -D_REENTRANT -Wall  -O3 -march=nocona -msse3 -I/opt/local/include -I/usr/local/include -I/opt/X11/include 
LINKFLAGS = ${LDFLAGS}  -lblas -llapack -lGVars3 -lcvd -L/usr/X11/lib -L/opt/X11/lib -L/usr/local/lib -framework OpenGL
```
<ol start="4">
  <li>Save</li>
</ol>
```make```

With a little luck, this should be it! Let's hope I didn't miss any step.


Cheers

Sérgio


[ptam]: http://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf
[xquartz]: https://www.xquartz.org/
[belion_repo]: https://github.com/BeLioN-github/PTAM
[git]: https://git-scm.com/downloads