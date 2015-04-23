# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

# Force MT for MSVC
if(MSVC)
    if (NOT BUILD_SHARED_LIBS)
        message("make msvc project runtime library: MT")
        set(CompilerFlags
            CMAKE_CXX_FLAGS
            CMAKE_CXX_FLAGS_DEBUG
            CMAKE_CXX_FLAGS_RELEASE
            CMAKE_C_FLAGS
            CMAKE_C_FLAGS_DEBUG
            CMAKE_C_FLAGS_RELEASE)

        foreach(CompilerFlag ${CompilerFlags})
            string(REPLACE "/MD" "/MT" ${CompilerFlag} "${${CompilerFlag}}")
        endforeach()
    endif()
endif()
