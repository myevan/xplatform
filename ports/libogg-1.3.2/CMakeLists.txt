cmake_minimum_required(VERSION 2.8)

project(libogg-1.3.2)

# CMakeLists.txt to build static libogg for Polycode

if(NOT CMAKE_BUILD_TYPE)
    # set(CMAKE_BUILD_TYPE "Debug")
    set(CMAKE_BUILD_TYPE "Release")
    message("No CMAKE_BUILD_TYPE specified, defaulting to ${CMAKE_BUILD_TYPE}") 
endif(NOT CMAKE_BUILD_TYPE)

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

set(OGG_SOURCES src/bitwise.c src/framing.c)
set(OGG_HEADERS include/ogg/ogg.h include/ogg/os_types.h)

include_directories(include)

if(MSVC)
    add_definitions(/D_UNICODE /DUNICODE)
    list(APPEND OGG_SOURCES win32/ogg.def)
endif (MSVC)

if("${CMAKE_SYSTEM_NAME}" STREQUAL "LinuX")
    # libogg expects configure to be called on linux to
    # generate config_types.h
    list(APPEND OGG_HEADERS include/ogg/config_types.h)

    add_custom_command(OUTPUT include/ogg/config_types.h
        COMMAND ./configure
        DEPENDS include/ogg/ogg.h # Hopefully if the libogg version changes, so does this file
        # so configure_types.h will be regenerated.
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        )
else()
    include(cmake/configure.cmake)
    configure_file(config.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/config.h)
    configure_file(include/ogg/config_types.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/include/ogg/config_types.h)
    add_definitions(-DHAVE_CONFIG_H)
endif()

add_library(ogg STATIC ${OGG_SOURCES})

install(TARGETS ogg
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib/static)

install(FILES ${OGG_HEADERS} DESTINATION include/ogg)

