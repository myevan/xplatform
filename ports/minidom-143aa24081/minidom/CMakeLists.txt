set( HDRS
    minidom.h
    minidom_error.h
    minidom_xml_parser.h
    minidom_ini_parser.h
    minidom_json_parser.h
    minidom_nkv_parser.h
    minidom_http_parser.h
    )

set( SRCS
    minidom.cpp
    )

add_library( minidom ${SRCS} )

if( WIN32 )
    if( NOT BUILD_SHARED_LIBS )
        set_target_properties( minidom PROPERTIES OUTPUT_NAME libminidom_static )
    endif(NOT BUILD_SHARED_LIBS)
endif( WIN32 )


foreach( DOCTYPE ${SUPPORT_DOCTYPE} )
    add_definitions( -DMINIDOM_SUPPORT_${DOCTYPE} )
endforeach( DOCTYPE ${SUPPORT_DOCTYPE} )

add_definitions( -DMINIDOM_TARGET_ENCODING="${DEFAULT_ENCODING}" )
add_definitions( -DMINIDOM_BUFFER_SIZE=${TEMP_BUFFER_SIZE} )

if( ENABLE_STL_MAP )
    add_definitions( -DMINIDOM_ENABLE_MAP )
endif( ENABLE_STL_MAP )

if( ENABLE_DUMP )
    add_definitions( -DMINIDOM_ENABLE_DUMP )
endif( ENABLE_DUMP )

if( ENABLE_ICONV )
    add_definitions( -DMINIDOM_ENABLE_ICONV )
endif( ENABLE_ICONV )

if( BUILD_SHARED_LIBS )
    if( WIN32 )
        add_definitions( -DMINIDOM_DLL -DMINIDOM_EXPORT )
    endif( WIN32 )
endif( BUILD_SHARED_LIBS )

install(FILES ${HDRS} DESTINATION include)

install( TARGETS minidom 
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib )

