PROJECT(ILUT)

FILE(GLOB ILUT_SRCS src/*.c)
FILE(GLOB ILUT_INC include/*.h ../include/IL/config.h ../include/IL/devil_internal_exports.h ../include/IL/ilut.h)
FILE(GLOB ILUT_RSRC)

INCLUDE_DIRECTORIES(

        ${ILUT_SOURCE_DIR}/include
)

#SET(ILUT_SRCS ${ILUT_SRCS} ${ILUT_INCS} )


SET(LIBRARY_OUTPUT_PATH         ${DEVIL_LIB_DEST_DIR}   )

#
# for windows add the .def and .rc files to the source list
#
IF(WIN32)
        ADD_DEFINITIONS(-DALLEGRO_MSVC)
        ADD_DEFINITIONS(-DIL_USE_PRAGMA_LIBS)
        IF(BUILD_SHARED_LIBS)
                ADD_DEFINITIONS(-DILUT_DLL)
                SET(ILUT_SRCS ${ILUT_SRCS} msvc/ilut.def)
                SET(ILUT_RSRC ${ILUT_RSRC} "msvc/resources/IL Logo.ico" msvc/ILUT.rc)
                SET(CMAKE_C_FLAGS_RELEASE "/MT /O2")
        ELSE(BUILD_SHARED_LIBS)
                ADD_DEFINITIONS(-DIL_STATIC_LIB)
        ENDIF(BUILD_SHARED_LIBS)
ENDIF(WIN32)

SOURCE_GROUP("Source Files" FILES src/*.c)
SOURCE_GROUP("Header Files" FILES ${ILUT_INC} )
SOURCE_GROUP("Resource Files" FILES ${ILUT_RSRC} )

# Remove SHARED to create a static library
ADD_LIBRARY(ILUT SHARED ${ILUT_SRCS} ${ILUT_INC} ${ILUT_RSRC})


## add link sub library info

TARGET_LINK_LIBRARIES(ILUT

        DevIL
        ILU
)

INCLUDE_DIRECTORIES(

        ${DevIL_SOURCE_DIR}/../include
        ${DevIL_SOURCE_DIR}/include
        ${DevILU_SOURCE_DIR}/include
)
