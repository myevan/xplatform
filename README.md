XPlatform
=========

Crossplatform Ports & Documents

CMake Ports
-----------

#### Requirements

* cmake-2.8~
* python-2.7~

#### Builders

* Windows: Visual Studio (msvc)
* OS X: Xcode (clang)
* Linux: GNU C/C++

#### POSIX Usage

Build 

    $ cd ports
    $ ./manage.py make $PACKAGE_DIR

Intall to prebuilts

    $ cd ../sources/$PACKAGE_DIR/build
    $ make install

    $ cd ../prebuilts/$PACKAGE_DIR/
    

#### Xcode Usage

Prepare

    $ cd ports
    $ ./manage.py xcode $PACKAGE_DIR

Build

    $ cd ../sources/$PACKAGE_DIR/build
    $ xcodebuild 

Install

    ...
