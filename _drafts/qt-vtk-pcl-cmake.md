---
title: PCL and Qt on Mac
location: Lisbon, Portugal
excerpt: Hacking my way into a QT-VTK-PCL Mac helloworld application
date: 2016-07-13
tags: [qt, vtk, pcl, cmake]
categories: [tutorials]
output: false
toc: true
toc_label: "Contents"
---

## Introduction

Hi everyone. The purpose of this tutorial is to exemplify how to integrate your [Point Cloud Library][pcl] (PCL) visualization code into [Qt][qt].
It's been a while since I started thinking I should learn something about Qt, and I also want to address a number of questions that occasionally pop in pcl-users mailing list, on how to compile projects that integrate PCL and Qt specific code. Our goto response is always to "handle everything through [CMake][cmake]", but people seem to be somewhat reluctant of going down that path. I'm hoping this provides a simple and quick boilerplate that allows everyone to have their projects up and running in no time.

[Qt][qt] is a powerful cross-platform graphical user interface (GUI) framework, which allows developers to quickly create cross-platform GUI applications with relative ease, by abstracting them from the complexity of having to do platform dependent code.

[VTK][vtk] is a cross-platform visualization framework but most importantly, it is the back end of the [```pcl::visualization```][pcl_vis] module. VTK is very powerful and provides extensive functionalities to visualize 2D and 3D data, the latter being clearly the most relevant in PCL, as well as providing interaction with keyboard and mouse controllers.

At this point you might be asking - "If VTK is already that good, why do I also need to use Qt?" - and the answer is that Qt can be seen as an extension to VTK. Qt will provide you with that "usual" [windowed-based application native look and feel](http://4.bp.blogspot.com/-PXJmnj81qU4/Tx9U37_2fbI/AAAAAAAAHf4/drNRyZ6im2Q/s1600/xfce-qt_2.png), providing standard controls like [text boxes](http://sector.ynet.sk/qt4-tutorial/tutorial/my-first-qt-gui-application/designer02.png), [sliders](http://www.loaditup.de/files/588035.png), [radio buttons](http://doc.qt.io/qt-5/images/groupbox-example.png), and a bunch of other elements that you're used to see in GUIs. This is definitely something you'll be wanting to look into, in case you're trying to give a more "professional" look into your PCL-based applications.

The interaction between VTK and Qt is made possible through the [Qt plugin system](http://doc.qt.io/qt-5/plugins-howto.html), and it is implemented by [QVTKWidget](https://fossies.org/dox/VTK-7.0.0/classQVTKWidget.html).

## Installing Dependencies

Before we begin I feel its important to make the following disclaimer: throughout my early experiments, I noticed that **things vary somewhat along different versions of Qt, VTK and CMake combined**. This means that some of the things I might state in the tutorial might not be applicable to the particular version you might have on your development environment, and I'm too lazy to cover all cases, especially considering that I cannot actually test them. Fortunately there are a number of resources you check in the web and I list a number of them at the [end of the post](#refs).

To start off we need PCL, VTK, Qt and CMake and given that we're working on a Mac, let's use [Homebrew][brew] to ease up that job.

### Homebrew

To install Homebrew follow the instructions provided on their [website][brew], that at the time of writing this tutorial is done by launching your terminal and executing the following line.

```shell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you want to know more about what that does, their [homepage][brew] pretty much covers it all.

### All in one go

In theory if you issue the following command

```shell
$ brew install pcl --with-qt
```

this will ensure PCL, CMake, VTK and Qt4 are all installed, since the they're all dependencies of PCL. I haven't exactly tested this, since I installed each manually at some point in the past and I tend to work with the git-master when it comes to PCL. Nevertheless, the following sections detail each of the dependencies individually and I specifically state which version I have on my development environment.

### CMake

```shell
$ brew install cmake
$ brew info cmake
cmake: stable 3.5.2 (bottled), devel 3.6.0-rc3, HEAD
Cross-platform make
https://www.cmake.org/
/usr/local/Cellar/cmake/3.4.1 (1,980 files, 27.4M) *
  Poured from bottle on 2015-12-04 at 00:20:45
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/cmake.rb
==> Dependencies
Build: sphinx-doc ✘
==> Options
--with-completion
	Install Bash completion (Has potential problems with system bash)
--without-docs
	Don't build man pages
--devel
	Install development version 3.6.0-rc3
--HEAD
	Install HEAD version
==> Caveats
Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/cmake

```

I'm running CMake 3.4.1.

### Qt

```shell
$ brew install qt
$ brew info qt
qt: stable 4.8.7 (bottled), HEAD
Cross-platform application and UI framework
https://www.qt.io/
/usr/local/Cellar/qt/4.8.7_1 (2,816 files, 113M) *
  Poured from bottle on 2015-10-04 at 04:12:47
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/qt.rb
==> Dependencies
Required: openssl ✘
Optional: dbus ✘, mysql ✘, postgresql ✘
==> Options
--with-dbus
	Build with dbus support
--with-docs
	Build documentation
--with-mysql
	Build with mysql support
--with-postgresql
	Build with postgresql support
--with-qt3support
	Build with deprecated Qt3Support module support
--without-webkit
	Build without QtWebKit module
--HEAD
	Install HEAD version
==> Caveats
We agreed to the Qt opensource license for you.
If this is unacceptable you should uninstall.

Qt Designer no longer picks up changes to the QT_PLUGIN_PATH environment
variable as it was tweaked to search for plug-ins provided by formulae in
  /usr/local/lib/qt4/plugins

.app bundles were installed.
Run `brew linkapps qt` to symlink these to /Applications.
```

I'm running a (Homebrew) patched version of Qt 4.8.7. Take notice of the where Qt got installed to ```/usr/local/Cellar/qt/4.8.7_1```, since we'll need to copy VTK's widget into its designer's plugin folder in the near future.

### VTK

```shell
$ brew install vtk --with-qt
$ brew info vtk
homebrew/science/vtk: stable 7.0.0 (bottled), HEAD
Toolkit for 3D computer graphics, image processing, and visualization.
http://www.vtk.org
/usr/local/Cellar/vtk/6.3.0 (3,446 files, 120.5M) *
  Built from source on 2015-11-07 at 18:23:15 with: --with-qt
From: https://github.com/Homebrew/homebrew-science/blob/master/vtk.rb
==> Dependencies
Build: cmake ✘
Recommended: boost ✘, fontconfig ✘, hdf5 ✘, jpeg ✔, libpng ✘, libtiff ✘
Optional: qt ✘, qt5 ✘
==> Options
--c++11
	Build using C++11 mode
--with-examples
	Compile and install various examples
--with-matplotlib
	Enable matplotlib support
--with-python3
	Build with python3 support
--with-qt
	Build with qt support
--with-qt-extern
	Enable Qt4 extension via non-Homebrew external Qt4
--with-qt5
	Build with qt5 support
--with-tcl
	Enable Tcl wrapping of VTK classes
--with-x11
	Build with x11 support
--without-boost
	Build without boost support
--without-fontconfig
	Build without fontconfig support
--without-hdf5
	Build without hdf5 support
--without-jpeg
	Build without jpeg support
--without-legacy
	Disable legacy APIs
--without-libpng
	Build without libpng support
--without-libtiff
	Build without libtiff support
--without-python
	Build without python2 support
--HEAD
	Install HEAD version
==> Caveats
Even without the --with-qt option, you can display native VTK render windows
from python. Alternatively, you can integrate the RenderWindowInteractor
in PyQt, PySide, Tk or Wx at runtime. Read more:
    import vtk.qt4; help(vtk.qt4) or import vtk.wx; help(vtk.wx)
```

Notice that I passed the ```--with-qt``` additional option in the install command. I'm currently running VTK 6.3.0. Before we install PCL, lets copy the QVTKWidget designer plugin, the standard Qt plugins' folder.

```shell
$ cp /usr/local/Cellar/vtk/6.3.0/plugins/designer/libQVTKWidgetPlugin.dylib /usr/local/Cellar/qt/4.8.7_1/plugins/designer/lib
```

*Your paths might be slightly different due to **different versions** of VTK and/or Qt.*

### PCL

```shell
$ brew install pcl --with-qt
$ brew info pcl
homebrew/science/pcl: stable 1.8.0 (bottled), HEAD
Library for 2D/3D image and point cloud processing
http://www.pointclouds.org/
Not installed
From: https://github.com/Homebrew/homebrew-science/blob/master/pcl.rb
==> Dependencies
Build: cmake ✘, pkg-config ✘
Required: boost ✘, eigen ✔, flann ✔, cminpack ✔, qhull ✘, libusb ✔, glew ✘
Recommended: vtk ✘
Optional: qt ✘, qt5 ✘, openni ✔, openni2 ✔
==> Options
--with-cuda
	Build with cuda support
--with-examples
	Build pcl examples.
--with-openni
	Build with openni support
--with-openni2
	Build with openni2 support
--with-qt
	Build with qt support
--with-qt5
	Build with qt5 support
--without-apps
	Build without apps.
--without-tools
	Build without tools.
--without-vtk
	Build without vtk support
--HEAD
	Install HEAD version
```

For PCL, I'm compiling the trunk from source and that's why Homebrew is reporting it as uninstalled. Nevertheless, version 1.8.0 (and likely others prior to it) should be acceptable. 

## Qt Designer

Time to do pretty things! Locate your Qt Designer app:

1. ```CMD + Space``` into awesomeness and type ```designer``` on spotlight. If spotlight is not catching anything relevant go to step 2.
2. Open Finder. ```CMD + Shift + G```, type ```/usr/local/Cellar/qt/<your_version_here>```. Double click on the the ```Designer.app```.

If everything went well you should seen something like this

(images for the post)

save the ui file

show what uic does

go to the cmake file and show the command which will invoke it

https://wiki.qt.io/Qt_for_Beginners
main.cpp skeleton

moc's for Q_OBJECT macros

sintax between cmake, vtk and qt versions for Qt has chanes somewhat so pay attention to the versions you have installed.


<h1 id="refs">Additional Material</h1>

http://www.vtk.org/Wiki/VTK/Tutorials/QtSetup
http://www.vtk.org/Wiki/VTK/Examples/Cxx/Qt/RenderWindowUISingleInheritance
https://wiki.qt.io/Using_CMake_build_system
http://doc.qt.io/qt-4.8/uic.html
https://wiki.qt.io/Qt_for_Beginners

[pcl]: http://pointclouds.org/
[qt]: https://www.qt.io/
[cmake]: https://cmake.org/
[vtk]: http://www.vtk.org/
[pcl_vis]: http://docs.pointclouds.org/trunk/namespacepcl_1_1visualization.html
[brew]: http://brew.sh/
