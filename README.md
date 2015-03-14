XPlatform
=========

Crossplatform Ports & Documents

CMake Ports
-----------

#### Requirements

* cmake-2.8~
* python-2.7~

#### Compilers

* Windows: Visual Studio (msvc)
* OS X: Xcode (clang)
* Linux: GNU C/C++

#### POSIX Build

Build 

    $ cd ports
    $ ./manage.py make $PACKAGE_DIR

Intall

    $ cd ../sources/$PACKAGE_DIR/build
    $ make install

#### Xcode Build

Prepare

    $ cd ports
    $ ./manage.py xcode $PACKAGE_DIR

Build

    $ cd ../sources/$PACKAGE_DIR/build
    $ xcodebuild 

Install

    ...
