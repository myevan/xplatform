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

    $ ./manage.py build ports/$PORT_NAME

OS X

    $ ./manage.py build_osx ports/$PORT_NAME

iOS (Universal: i386+armv7+armv7s+arm64)

    $ cd ports
    $ ./manage.py build_ios ports/$PORT_NAME

Windows

    $ ./manage.py build_win ports/$PORT_NAME

#### How to clean

    $ cd ports
    $ ./manage.py clean ports/$PORT_NAME


