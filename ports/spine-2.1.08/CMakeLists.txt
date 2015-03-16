cmake_minimum_required(VERSION 2.8)
project (spine-2.1.08)

FILE(GLOB SOURCES 
    RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/spine-c/src/spine/*.c
)

FILE(GLOB PUBLIC_HEADERS 
    RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/spine-c/include/spine/*.h
)

include_directories(spine-c/include)

add_library(spine ${SOURCES})

install(FILES ${PUBLIC_HEADERS} DESTINATION include/spine)

install(TARGETS spine
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
