XPlatform
=========

크로스 플랫폼을 위한 CMake 포트와 문서 모음입니다. 


요구 사항
---------
* cmake-2.8 이상
* python-2.7 이상


지원 컴파일러
-------------
* Windows: Visual Studio (msvc)
* OS X: Xcode (clang)
* Linux: GNU C/C++


POSIX 빌드
----------

Makefile 생성

    $ cd ports
    $ ./manage.py prepare $PACKAGE_DIR
    $ cd ../sources/$PACKAGE_DIR/build
    $ cmake ..

빌드 

    $ make

설치

    $ make install


Xcode 빌드
----------

Xcode 프로젝트 생성

    $ cd ports
    $ ./manage.py prepare $PACKAGE_DIR
    $ cd ../sources/$PACKAGE_DIR/build
    $ cmake -G Xcode ..
    

