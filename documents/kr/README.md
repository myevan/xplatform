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


#### POSIX 사용법

빌드 

    $ cd ports
    $ ./manage.py make $PACKAGE_DIR

설치

    $ cd ../sources/$PACKAGE_DIR/build
    $ make install


#### Xcode 사용법

빌드

    $ cd ports
    $ ./manage.py xcode $PACKAGE_DIR
    $ cd ../sources/$PACKAGE_DIR/build
    $ xcodebuild

설치

    ...
   
 
#### 빌더 초기화

    $ cd ports
    $ ./manage.py clean $PACKAGE_DIR


