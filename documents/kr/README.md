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

    $ cd ports
    $ ./manage.py build $PACKAGE_DIR

OS X

    $ cd ports
    $ ./manage.py build_osx $PACKAGE_DIR


iOS (Universal: i386+armv7+armv7s+arm64)

    $ cd ports
    $ ./manage.py build_ios $PACKAGE_DIR


#### 클린 방법

    $ cd ports
    $ ./manage.py clean $PACKAGE_DIR


