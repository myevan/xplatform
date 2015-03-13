cmake_minimum_required(VERSION 2.8)
project (zlib-1.2.8)

set(SRC_Z adler32.c crc32.c deflate.c infback.c inffast.c inflate.c inftrees.c trees.c zutil.c)

SET(SRC_G compress.c uncompr.c gzclose.c gzlib.c gzread.c gzwrite.c)

add_library(z ${SRC_Z} ${SRC_G})

include_directories(${PROJECT_SOURCE_DIR})

add_executable(example test/example.c)
target_link_libraries(example z)

add_executable(example64 test/example.c)
target_link_libraries(example64 z)
