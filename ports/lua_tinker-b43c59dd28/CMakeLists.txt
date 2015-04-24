cmake_minimum_required(VERSION 2.8)
project (lua_tinker)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/../../cmakes")

set(SAMPLE_NAMES
    sample1
    sample2
    sample3
    sample4
    sample5
    sample6)

include_directories("${PROJECT_SOURCE_DIR}/include")
include_directories("${PROJECT_SOURCE_DIR}/../lua-5.1.5/src")
link_directories("${PROJECT_SOURCE_DIR}/../lua-5.1.5/__build")

add_library(lua_tinker_static STATIC src/lua_tinker.cpp)

install(TARGETS lua_tinker_static
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(FILES include/lua_tinker.h DESTINATION include)

if(POSIX)
    foreach(SAMPLE_NAME ${SAMPLE_NAMES}) 
        add_executable(${SAMPLE_NAME} samples/${SAMPLE_NAME}.cpp)
        target_link_libraries(${SAMPLE_NAME} lua_tinker_static lua_static)

    endforeach(SAMPLE_NAME)

    file(GLOB SAMPLE_LUA_FILES "samples/*.lua")
    install(FILES ${SAMPLE_LUA_FILES} DESTINATION bin)
    install(TARGETS ${SAMPLE_NAMES} RUNTIME DESTINATION bin)
endif()
