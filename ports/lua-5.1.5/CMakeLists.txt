cmake_minimum_required(VERSION 2.8)
project (lua C)

set(VERSION "5.1.5")

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/../../cmakes")

set(CORE_SOURCES
    src/lapi.c 
    src/lcode.c 
    src/ldebug.c 
    src/ldo.c 
    src/ldump.c 
    src/lfunc.c 
    src/lgc.c 
    src/llex.c 
    src/lmem.c 
    src/lobject.c 
    src/lopcodes.c 
    src/lparser.c 
    src/lstate.c 
    src/lstring.c 
    src/ltable.c 
    src/ltm.c  
    src/lundump.c 
    src/lvm.c 
    src/lzio.c)

set(LIB_SOURCES
    src/lauxlib.c 
    src/lbaselib.c 
    src/ldblib.c 
    src/liolib.c 
    src/lmathlib.c 
    src/loslib.c 
    src/ltablib.c 
    src/lstrlib.c 
    src/loadlib.c 
    src/linit.c)

set(SHELL_SOURCES 
    src/lua.c)

set(COMPILER_SOURCES 
    src/luac.c 
    src/print.c)

set(PUBLIC_HEADERS
    src/lua.h
    src/lualib.h
    src/lauxlib.h
    src/luaconf.h)

include(xplatform)

add_library(lua_static STATIC ${CORE_SOURCES} ${LIB_SOURCES})
if (MSVC)
    set_target_properties(lua_static PROPERTIES OUTPUT_NAME liblua_static)
endif()

install(FILES ${PUBLIC_HEADERS} DESTINATION include)

if (IOS OR ANDROID)
    install(TARGETS lua_static
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION lib
            ARCHIVE DESTINATION lib)
else()
    add_library(lua_shared SHARED ${CORE_SOURCES} ${LIB_SOURCES})
    set_target_properties(lua_shared PROPERTIES OUTPUT_NAME lua)

    add_executable (lua_shell ${SHELL_SOURCES})
    target_link_libraries(lua_shell lua_static)
    set_target_properties(lua_shell PROPERTIES OUTPUT_NAME lua)

    add_executable (lua_compiler ${COMPILER_SOURCES})
    target_link_libraries(lua_compiler lua_static)
    set_target_properties(lua_compiler PROPERTIES OUTPUT_NAME luac)

    install(TARGETS lua_shared lua_static lua_shell lua_compiler
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION lib
            ARCHIVE DESTINATION lib)
endif()
