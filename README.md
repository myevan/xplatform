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

Prepare

    $ cd ports
    $ ./manage.py prepare $PACKAGE_DIR
    $ cd ../sources/$PACKAGE_DIR/build
    $ cmake ..

Build 

    $ make

Intall

    $ make install

#### Xcode Build

Prepare

    $ cd ports
    $ ./manage.py prepare $PACKAGE_DIR
    $ cd ../sources/$PACKAGE_DIR/build
    $ cmake -G Xcode ..

Build

    ... 

Install 

    ...
