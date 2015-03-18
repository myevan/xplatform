# Copyright (C) 2007-2012 LuaDist.
# Created by Peter Drahoš
# Redistribution and use of this file is allowed according to the terms of the MIT license.
# For details see the COPYRIGHT file distributed with LuaDist.
# Please note that the package source code is licensed under its own license.

cmake_minimum_required(VERSION 2.8)

project (libiconv-1.14)

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

include ( cmake/dist.cmake )
include ( cmake/configure.cmake )

# Options
option ( ENABLE_EXTRA "Enable a few rarely used encodings" OFF)
option ( ENABLE_NLS "Translation of program messages to the user's native language is requested" OFF)
#option ( ENABLE_RELOCATABLE "The package shall run at any location in the file system" ON )


# iconv.h
set ( USE_MBSTATE_T 1 )
set ( BROKEN_WCHAR_H 0 )
set ( HAVE_WCHAR_T 0)

configure_file ( config.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/config.h )
configure_file ( include/iconv.h.build.in ${CMAKE_CURRENT_SOURCE_DIR}/include/iconv.h )
configure_file ( libcharset/include/libcharset.h.in ${CMAKE_CURRENT_SOURCE_DIR}/include/libcharset.h )
configure_file ( srclib/uniwidth.in.h ${CMAKE_CURRENT_SOURCE_DIR}/srclib/uniwidth.h )
configure_file ( srclib/unitypes.in.h ${CMAKE_CURRENT_SOURCE_DIR}/srclib/unitypes.h )

# Dirty fix for MinGW
if ( MINGW )
  add_definitions ( -DELOOP=0 -DHAVE_DECL_STRERROR_R=0 )
  configure_file ( srclib/alloca.in.h ${CMAKE_CURRENT_SOURCE_DIR}/srclib/alloca.h )
endif ()

# Force MT for MSVC
if ( MSVC )
	set( CompilerFlags
        CMAKE_CXX_FLAGS
        CMAKE_CXX_FLAGS_DEBUG
        CMAKE_CXX_FLAGS_RELEASE
        CMAKE_C_FLAGS
        CMAKE_C_FLAGS_DEBUG
        CMAKE_C_FLAGS_RELEASE)

	foreach(CompilerFlag ${CompilerFlags})
	  string(REPLACE "/MD" "/MT" ${CompilerFlag} "${${CompilerFlag}}")
	endforeach()
endif ()

include_directories ( ${CMAKE_CURRENT_SOURCE_DIR} include srclib )
add_definitions ( -Dset_relocation_prefix=libcharset_set_relocation_prefix -Drelocate=libcharset_relocate -DHAVE_CONFIG_H -DINSTALLPREFIX=NULL -DNO_XMALLOC -DBUILDING_LIBCHARSET -DINSTALLDIR="" -DLIBDIR="" -DENABLE_RELOCATABLE=1 -DIN_LIBRARY )
# FOR_BUILD_SHARED_LIBS: add_definitions ( -DBUILDING_DLL )

# libcharset
set ( SRC_LIBCHARSET
  libcharset/lib/localcharset.c
  libcharset/lib/relocatable.c
)

add_library ( charset STATIC ${SRC_LIBCHARSET} )
set_target_properties ( charset PROPERTIES COMPILE_FLAGS -DBUILDING_LIBCHARSET)

# libicrt
set ( SRC_LIBICRT 
  srclib/allocator.c
  srclib/areadlink.c
  srclib/careadlinkat.c
  srclib/malloca.c
  srclib/progname.c
  srclib/safe-read.c
  srclib/uniwidth/width.c
  srclib/xmalloc.c
  srclib/xstrdup.c
  srclib/xreadlink.c
  srclib/canonicalize-lgpl.c
  srclib/error.c
  srclib/lstat.c
  srclib/readlink.c
  srclib/stat.c
  srclib/strerror.c
  srclib/strerror-override.c  
)

# libiconv
set ( SRC_LIBICONV
  lib/iconv.c
)

add_library ( iconv STATIC ${SRC_LIBICONV} )
target_link_libraries ( iconv charset )
# FOR_BUILD_SHARED_LIBS set_target_properties ( iconv PROPERTIES COMPILE_FLAGS -DBUILDING_LIBICONV)

install_header ( include/iconv.h )
install_data ( README AUTHORS COPYING )

install(TARGETS iconv charset
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)

# for iconvcli
# add_library ( icrt STATIC ${SRC_LIBICRT} )
# add_executable ( iconvcli src/iconv_no_i18n.c )
# target_link_libraries ( iconvcli iconv icrt charset )
# set_target_properties ( iconvcli PROPERTIES OUTPUT_NAME iconv )
# install(TARGETS iconvcli RUNTIME DESTINATION bin))))
