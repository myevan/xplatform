cmake_minimum_required(VERSION 2.8)
project (libpng-1.6.16)

macro(macro_add_definition_if FOUND_VAR)
    if (${FOUND_VAR})
        add_definitions(-D${FOUND_VAR}=1)
    endif(${FOUND_VAR})
endmacro(macro_add_definition_if)

include(CheckIncludeFiles)
include(CheckFunctionExists)

check_include_files("dlfcn.h" HAVE_DLFCN_H)
check_include_files("inttypes.h" HAVE_INTTYPES_H)
#check_include_files("libm.h" HAVE_LIBM_H)
check_include_files("memory.h" HAVE_MEMORY_H)
check_include_files("stdint.h" HAVE_STDINT_H)
check_include_files("stdlib.h" HAVE_STDLIB_H)
check_include_files("strings.h" HAVE_STRINGS_H)
check_include_files("string.h" HAVE_STRING_H)
check_include_files("sys/stat.h" HAVE_SYS_STAT_H)
check_include_files("sys/types.h" HAVE_SYS_TYPES_H)
check_include_files("unistd.h" HAVE_UNISTD_H)

check_function_exists(memset HAVE_MEMSET)
check_function_exists(pow HAVE_POW)

# PNG_ARM_NEON_API_SUPPORTED
# PNG_ARM_NEON_CHECK_SUPPORTED
# PNG_ARM_NEON_OPT
# STDC_HEADERS 
# TM_IN_SYS_TIME_
# restrict 
# size_t

macro_add_definition_if(HAVE_DLFCN_H)
macro_add_definition_if(HAVE_INTTYPES_H)
macro_add_definition_if(HAVE_LIBM_H)
macro_add_definition_if(HAVE_MEMORY_H)
macro_add_definition_if(HAVE_STDINT_H)
macro_add_definition_if(HAVE_STDLIB_H)
macro_add_definition_if(HAVE_STRINGS_H)
macro_add_definition_if(HAVE_STRING_H)
macro_add_definition_if(HAVE_SYS_STAT_H)
macro_add_definition_if(HAVE_SYS_TYPES_H)
macro_add_definition_if(HAVE_UNISTD_H)

macro_add_definition_if(HAVE_MEMSET)
macro_add_definition_if(HAVE_POW)

include_directories("${PROJECT_SOURCE_DIR}/../zlib-1.2.8")
link_directories("${PROJECT_SOURCE_DIR}/../zlib-1.2.8")
add_definitions(-DHAVE_LIBZ_H=1)

add_library(png png.c pngerror.c pngget.c pngmem.c pngpread.c pngread.c pngrio.c pngrtran.c pngrutil.c pngset.c pngtrans.c pngwio.c pngwrite.c pngwtran.c pngwutil.c)

set(TEST_SAMPLES
    ${CMAKE_CURRENT_SOURCE_DIR}/pngtest.png
)

add_executable(pngtest pngtest.c)
target_link_libraries(pngtest png z)
add_test(pngtest ./pngtest ${TEST_SAMPLES})

set(PUBLIC_HEADERS
  png.h
  pngconf.h
  ${CMAKE_CURRENT_SOURCE_DIR}/pnglibconf.h
)

install(FILES ${PUBLIC_HEADERS} DESTINATION include)
install(FILES ${TEST_SAMPLES}   DESTINATION bin)

install(TARGETS png pngtest 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
