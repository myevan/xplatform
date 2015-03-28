cmake_minimum_required(VERSION 2.8)

project (tinyxml)

set(VERSION "2.6.2")

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/../../cmakes")

set(LIB_SOURCES
    tinystr.cpp
    tinyxml.cpp
    tinyxmlerror.cpp
    tinyxmlparser.cpp)

set(TEST_SOURCES
    xmltest.cpp)

set(PUBLIC_HEADERS
    tinystr.h
    tinyxml.h)

include(xplatform)

add_library(tinyxml_static STATIC ${LIB_SOURCES})

set_target_properties(tinyxml_static PROPERTIES OUTPUT_NAME tinyxml)

install(FILES ${PUBLIC_HEADERS} DESTINATION include)

install(TARGETS tinyxml_static
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)

