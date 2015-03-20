cmake_minimum_required(VERSION 2.8)

project(sqlite C)

set(VERSION "3.8.8.3")

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

include(cmake/configure.cmake)

set(PUBLIC_HEADERS
    sqlite3.h
)

set(LIB_SOURCES
    sqlite3.c
)

set(EXE_SOURCES
    shell.c
)

add_library(sqlite3 SHARED ${LIB_SOURCES})
add_library(sqlite3_static STATIC ${LIB_SOURCES})
set_target_properties(sqlite3_static PROPERTIES OUTPUT_NAME sqlite3)

add_executable(sqlite3_shell ${EXE_SOURCES})
target_link_libraries(sqlite3_shell sqlite3 ${READLINE_LIBRARY})
set_target_properties(sqlite3_shell PROPERTIES OUTPUT_NAME sqlite3)

install(FILES ${PUBLIC_HEADERS} DESTINATION include)

install(TARGETS sqlite3 sqlite3_static sqlite3_shell 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
