cmake_minimum_required ( VERSION 2.6 )

project ( minidom )

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/../../cmakes")

include(xplatform)

set( DEFAULT_ENCODING utf-8
    CACHE STRING "Set your default encoding."
    )

set( ENABLE_TEST OFF
    CACHE BOOL "Set on to apply tests"
    )

set( ENABLE_ICONV OFF
    CACHE BOOL "Set on to apply xml encodings with iconv library."
    )

set( ENABLE_DUMP ON
    CACHE BOOL "Set on to enable method that dump(save) dom into string or file."
    )

set( TEMP_BUFFER_SIZE 4096
    CACHE STRING "Buffer size for element name and its value while minidom parsing & dumping."
    )

set( SUPPORT_DOCTYPE XML;INI;JSON
    CACHE STRING "Build with specified doctypes, separate with semicolon. XML;INI;JSON;HTTP;NKV are supported."
    )

set( BUILD_SHARED_LIBS OFF
    CACHE BOOL "Turn on if you want to build shared(dylib,so,dll) libraries."
    )

if( ENABLE_ICONV )
    include_directories("${PROJECT_SOURCE_DIR}/../iconv-1.14/__build")
    include_directories("${PROJECT_SOURCE_DIR}/../iconv-1.14")
    link_directories("${PROJECT_SOURCE_DIR}/../iconv-1.14")
endif( ENABLE_ICONV )

add_subdirectory( minidom )

if( ENABLE_TEST )
    enable_testing()
    add_subdirectory( tests )
endif( ENABLE_TEST )
