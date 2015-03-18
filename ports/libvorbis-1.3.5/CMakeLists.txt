cmake_minimum_required(VERSION 2.8)

project(libvorbis-1.3.5)

include(cmake/configure.cmake)

configure_file ( config.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/config.h )

if(NOT CMAKE_BUILD_TYPE)
    #set(CMAKE_BUILD_TYPE "Debug")
    set(CMAKE_BUILD_TYPE "Release")
    message("No CMAKE_BUILD_TYPE specified, defaulting to ${CMAKE_BUILD_TYPE}") 
endif(NOT CMAKE_BUILD_TYPE)

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

include_directories("${PROJECT_SOURCE_DIR}/../libogg-1.3.2/include")
link_directories("${PROJECT_SOURCE_DIR}/../libogg-1.3.2")

message("CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}")

set(VORBIS_SOURCES
    lib/analysis.c
    lib/bitrate.c
    lib/block.c
    lib/codebook.c
    lib/envelope.c
    lib/floor0.c
    lib/floor1.c
    lib/info.c
    lib/lookup.c
    lib/lpc.c
    lib/lsp.c
    lib/mapping0.c
    lib/mdct.c
    lib/psy.c
    lib/registry.c
    lib/res0.c
    lib/sharedbook.c
    lib/smallft.c
    lib/synthesis.c
    lib/vorbisenc.c
    lib/window.c
)

set(VORBIS_HEADERS 
    lib/backends.h
    lib/bitrate.h
    lib/codebook.h
    lib/codec_internal.h
    lib/envelope.h
    lib/modes/floor_all.h
    lib/books/floor/floor_books.h
    lib/highlevel.h
    lib/lookup.h
    lib/lookup_data.h
    lib/lpc.h
    lib/lsp.h
    lib/masking.h
    lib/mdct.h
    lib/misc.h
    lib/os.h
    lib/psy.h
    lib/modes/psych_11.h
    lib/modes/psych_16.h
    lib/modes/psych_44.h
    lib/modes/psych_8.h
    lib/registry.h
    lib/books/coupled/res_books_stereo.h
    lib/books/uncoupled/res_books_uncoupled.h
    lib/modes/residue_16.h
    lib/modes/residue_44.h
    lib/modes/residue_44u.h
    lib/modes/residue_8.h
    lib/scales.h
    lib/modes/setup_11.h
    lib/modes/setup_16.h
    lib/modes/setup_22.h
    lib/modes/setup_32.h
    lib/modes/setup_44.h
    lib/modes/setup_44u.h
    lib/modes/setup_8.h
    lib/modes/setup_X.h
    lib/smallft.h
    lib/window.h
)

set(VORBIS_PUBLIC_HEADERS
    include/vorbis/codec.h
    include/vorbis/vorbisenc.h
    include/vorbis/vorbisfile.h)

include_directories("${PROJECT_SOURCE_DIR}")
include_directories("${PROJECT_SOURCE_DIR}/include")
include_directories("${PROJECT_SOURCE_DIR}/lib")

add_definitions(-DHAVE_CONFIG_H -DUSE_MEMORY_H)
add_definitions(-DFLOAT_LOOKUP)

# TODO: APPLE -DDARWIN -fno-common -force_cpusubtype_ALL -Wall -g -O3 -ffast-math -fsigned-char -Wdeclaration-after-statement 

if(MSVC)
    add_definitions(/D_UNICODE /DUNICODE)
    list(APPEND libvorbis_SRCS win32/vorbis.def)
endif(MSVC)

add_library(vorbis ${VORBIS_SOURCES})
add_library(vorbisfile lib/vorbisfile.c include/vorbis/vorbisfile.h)

install(TARGETS vorbis vorbisfile
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib/static
    LIBRARY DESTINATION lib)

install(FILES ${VORBIS_PUBLIC_HEADERS} DESTINATION include/vorbis)
