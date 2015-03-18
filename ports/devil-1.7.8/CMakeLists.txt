cmake_minimum_required(VERSION 2.8)

PROJECT(DevIL C)

option(BUILD_SHARED_LIBS "Build with shared (.DLL .SO) libraries." ON)

set(VERSION "1.7.8")

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

include(cmake/configure.cmake)
configure_file(include/IL/config.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/include/IL/config.h)

add_definitions(-DHAVE_CONFIG_H)

set(IL_HEADERS
    include/IL/config.h
    include/IL/devil_internal_exports.h
    include/IL/il.h
    include/IL/il_wrap.h
    include/IL/ilu.h
    include/IL/ilu_region.h
    include/IL/ilut.h
)

include_directories(include)
include_directories(include/IL)
include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR}/IL/)
include_directories("${PROJECT_SOURCE_DIR}/../zlib-1.2.8")
include_directories("${PROJECT_SOURCE_DIR}/../libjpeg-9.1/__build")
include_directories("${PROJECT_SOURCE_DIR}/../libjpeg-9.1")
include_directories("${PROJECT_SOURCE_DIR}/../libpng-1.6.16")

link_directories("${PROJECT_SOURCE_DIR}/../zlib-1.2.8")
link_directories("${PROJECT_SOURCE_DIR}/../libjpeg-9.1")
link_directories("${PROJECT_SOURCE_DIR}/../libpng-1.6.16")

include_directories(src-IL/include)

file(GLOB LIBIL_SRCS "src-IL/src/*.c")
if(NOT ALTIVEC_GCC)
    list(REMOVE_ITEM LIBIL_SRCS 
        ${CMAKE_CURRENT_SOURCE_DIR}/src-IL/src/altivec_common.c 
        ${CMAKE_CURRENT_SOURCE_DIR}/src-IL/src/altivec_typeconversion.c)
endif()

add_library(il ${LIBIL_SRCS})
set_source_files_properties(src-il/src/il_jpeg.c PROPERTIES COMPILE_FLAGS "-DXMD_H")
set_source_files_properties(src-il/src/il_mng.c PROPERTIES COMPILE_FLAGS "-DXMD_H")
target_link_libraries(il z jpeg png16)
if(MINGW)
    set_target_properties(il 
        PROPERTIES #LINK_FLAGS "-Wl,--add-stdcall-alias -Wl,--kill-at"
        LINK_FLAGS "-Wl,--add-stdcall-alias" #LINK_FLAGS "-Wl,--kill-at"
        CLEAN_DIRECT_OUTPUT 1)
endif()

#SUBDIRS(src-IL src-ILU src-ILUT)


# need to check for vc6 or vc2003 output dir
#IF(BUILD_SHARED_LIBS)
#    SET(DEVIL_LIB_DEST_DIR  ${CMAKE_CURRENT_SOURCE_DIR}/lib/ )
#ELSE(BUILD_SHARED_LIBS)
#    SET(DEVIL_LIB_DEST_DIR  ${CMAKE_CURRENT_SOURCE_DIR}/lib/ )
#ENDIF(BUILD_SHARED_LIBS)

#EXPORT_LIBRARY_DEPENDENCIES(CMakeDepends.txt)

install(TARGETS il 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
