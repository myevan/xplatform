cmake_minimum_required(VERSION 2.8)
project (libjpeg-9.1)

# Copyright (C) 2007-2012 LuaDist.
# Created by Peter Kapec, David Manura
# Redistribution and use of this file is allowed according to the terms of the MIT license.
# For details see the COPYRIGHT file distributed with LuaDist.
# Please note that the package source code is licensed under its own license.

include ( cmake/dist.cmake )

include ( CheckIncludeFile )
check_include_file ( stddef.h HAVE_STDDEF_H )
check_include_file ( stdlib.h HAVE_STDLIB_H )
if ( WIN32 AND NOT CYGWIN )
  #improve? see jconfig.*
  set ( TWO_FILE_COMMANDLINE true )
  # jconfig.h
endif ( )

configure_file ( jconfig.h.cmake jconfig.h )

include_directories ( ${CMAKE_CURRENT_BINARY_DIR} )
# jconfig.h

set ( HEADERS jerror.h jmorecfg.h jpeglib.h ${CMAKE_CURRENT_BINARY_DIR}/jconfig.h )

set ( SRC jmemnobs.c jaricom.c jcapimin.c jcapistd.c jcarith.c jccoefct.c jccolor.c 
  jcdctmgr.c jchuff.c jcinit.c jcmainct.c jcmarker.c jcmaster.c jcomapi.c jcparam.c 
  jcprepct.c jcsample.c jctrans.c jdapimin.c jdapistd.c jdarith.c jdatadst.c jdatasrc.c 
  jdcoefct.c jdcolor.c jddctmgr.c jdhuff.c jdinput.c jdmainct.c jdmarker.c jdmaster.c 
  jdmerge.c jdpostct.c jdsample.c jdtrans.c jerror.c jfdctflt.c jfdctfst.c jfdctint.c 
  jidctflt.c jidctfst.c jidctint.c jquant1.c jquant2.c jutils.c jmemmgr.c cderror.h 
  cdjpeg.h jdct.h jinclude.h jmemsys.h jpegint.h jversion.h transupp.h )

add_library ( jpeg ${SRC} ${HEADERS} )

add_executable ( cjpeg cdjpeg.c cjpeg.c rdbmp.c rdgif.c rdppm.c rdrle.c rdtarga.c 
  rdswitch.c )
add_executable ( djpeg cdjpeg.c djpeg.c wrbmp.c wrgif.c wrppm.c wrrle.c wrtarga.c 
  rdcolmap.c )
add_executable ( jpegtran jpegtran.c cdjpeg.c rdswitch.c transupp.c )
add_executable ( rdjpgcom rdjpgcom.c )
add_executable ( wrjpgcom wrjpgcom.c )
target_link_libraries ( cjpeg jpeg )
target_link_libraries ( djpeg jpeg )
target_link_libraries ( jpegtran jpeg )

install_header ( ${HEADERS} )
install_doc ( README install.txt usage.txt wizard.txt example.c libjpeg.txt structure.txt coderules.txt filelist.txt change.log )

install(TARGETS jpeg cjpeg djpeg jpegtran rdjpgcom wrjpgcom
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
