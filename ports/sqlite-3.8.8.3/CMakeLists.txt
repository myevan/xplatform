cmake_minimum_required(VERSION 2.8)
project (sqlite-3.8.8.3)

find_path(READLINE_HEADER readline/readline.h)
if (READLINE_HEADER)
    message(STATUS "Found GNU readline: ${READLINE_LIBRARY}")
    add_definitions(-DHAVE_READLINE=1)
endif (READLINE_HEADER)

macro(macro_add_definition_if FOUND_VAR)
    if (${FOUND_VAR})
        add_definitions(-D${FOUND_VAR}=1)
    endif(${FOUND_VAR})
endmacro(macro_add_definition_if)

include(CheckIncludeFiles)
include(CheckFunctionExists)
include(CheckSymbolExists)

check_include_files("sys/types.h" HAVE_SYS_TYPES_H)
check_include_files("sys/stat.h" HAVE_SYS_STAT_H)
check_include_files("stdlib.h" HAVE_STDLIB_H)
check_include_files("string.h" HAVE_STRING_H)
check_include_files("memory.h" HAVE_MEMORY_H)
check_include_files("strings.h" HAVE_STRINGS_H)
check_include_files("inttypes.h" HAVE_INTTYPES_H)
check_include_files("stdint.h" HAVE_STDINT_H)
check_include_files("unistd.h" HAVE_UNISTD_H)
check_include_files("dlfcn.h" HAVE_DLFCN_H)

check_function_exists(usleep HAVE_USLEEP)
check_function_exists(localtime_r HAVE_LOCALTIME_R)
check_function_exists(gmtime_r HAVE_GMTIME_R)
check_function_exists(fdatasync HAVE_FDATASYNC)

check_symbol_exists(strerror_r "string.h" HAVE_DECL_STRERROR_R)
check_symbol_exists(strerror_r "string.h" HAVE_STRERROR_R) 

macro_add_definition_if(HAVE_SYS_TYPES_H)
macro_add_definition_if(HAVE_SYS_STAT_H)
macro_add_definition_if(HAVE_STDLIB_H)
macro_add_definition_if(HAVE_STRING_H)
macro_add_definition_if(HAVE_MEMORY_H)
macro_add_definition_if(HAVE_STRINGS_H)
macro_add_definition_if(HAVE_INTTYPES_H)
macro_add_definition_if(HAVE_STDINT_H)
macro_add_definition_if(HAVE_UNISTD_H)
macro_add_definition_if(HAVE_DLFCN_H)

macro_add_definition_if(HAVE_USLEEP)
macro_add_definition_if(HAVE_LOCALTIME_R)
macro_add_definition_if(HAVE_GMTIME_R)
macro_add_definition_if(HAVE_FDATASYNC)

macro_add_definition_if(HAVE_DECL_STRERROR_R)

add_library(sqlite3 sqlite3.c)

add_definitions(-D_REENTRANT=1 -DSQLITE_THREADSAFE=1 -DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_RTREE)

add_executable(sqlite3i shell.c)
target_link_libraries(sqlite3i sqlite3)

find_library(READLINE_LIBRARY NAMES readline) 
if (READLINE_LIBRARY)
    target_link_libraries(sqlite3i ${READLINE_LIBRARY})
endif (READLINE_LIBRARY)

install(FILES sqlite3.h DESTINATION include)

install(TARGETS sqlite3 sqlite3i 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
