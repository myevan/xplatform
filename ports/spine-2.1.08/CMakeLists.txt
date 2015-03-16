cmake_minimum_required(VERSION 2.8)
project (spine-2.1.08)

FILE(GLOB SRCS
    RELATIVE ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/spine-c/src/spine/*.c
)

include_directories(spine-c/include)

add_library(spine ${SRCS})
