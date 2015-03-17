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

#### How to Build 

POSIX

    $ cd ports
    $ ./manage.py build $PACKAGE_DIR

OS X

    $ cd ports
    $ ./manage.py build_osx $PACKAGE_DIR

iOS (Universal: i386+armv7+armv7s+arm64)

    $ cd ports
    $ ./manage.py build_ios $PACKAGE_DIR


#### How to clean

    $ cd ports
    $ ./manage.py clean $PACKAGE_DIR


