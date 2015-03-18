XPlatform
=========

크로스 플랫폼을 위한 CMake 포트와 문서 모음입니다. 


CMake Ports
-----------

#### 요구 사항

* cmake-2.8 이상
* python-2.7 이상


#### 지원 빌더

* Windows: Visual Studio (msvc)
* OS X: Xcode (clang)
* Linux: GNU C/C++


#### 빌드 방법

POSIX 

    $ ./manage.py build $PORT_NAME

OS X

    $ ./manage.py build_osx $PORT_NAME

iOS (Universal: i386+armv7+armv7s+arm64)

    $ ./manage.py build_ios $PORT_NAME

Windows

    $ ./manage.py build_win $PORT_NAME


#### 클린 방법

    $ cd ports
    $ ./manage.py clean $PORT_NAME


