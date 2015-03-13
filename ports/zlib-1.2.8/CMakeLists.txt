cmake_minimum_required(VERSION 2.8)
project (zlib-1.2.8)

set(SRC_Z adler32.c crc32.c deflate.c infback.c inffast.c inflate.c inftrees.c trees.c zutil.c)

set(SRC_G compress.c uncompr.c gzclose.c gzlib.c gzread.c gzwrite.c)

macro(macro_add_definition_if FOUND_VAR)
    if (${FOUND_VAR})
        add_definitions(-D${FOUND_VAR}=1)
    endif(${FOUND_VAR})
endmacro(macro_add_definition_if)

include(CheckIncludeFiles)

check_include_files("stdarg.h" HAVE_STDARG_H)
check_include_files("unistd.h" HAVE_UNISTD_H)

macro_add_definition_if(HAVE_STDARG_H)
macro_add_definition_if(HAVE_UNISTD_H)

add_library(z ${SRC_Z} ${SRC_G})

include_directories(${PROJECT_SOURCE_DIR})

add_executable(example test/example.c)
target_link_libraries(example z)

add_executable(example64 test/example.c)
target_link_libraries(example64 z)

install(FILES zlib.h DESTINATION include)
install(FILES zconf.h DESTINATION include)

install(TARGETS z example example64 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
