include(CheckIncludeFiles)

check_include_files("dlfcn.h"           HAVE_DLFCN_H)
check_include_files("glut/glut.h"       HAVE_GLUT_GLUT_H)
check_include_files("gl/glut.h"         HAVE_GL_GLUT_H)
check_include_files("gl/glu.h"          HAVE_GL_GLU_H)
check_include_files("gl/gl.h"           HAVE_GL_GL_H)
check_include_files("inttypes.h"        HAVE_INTTYPES_H)
check_include_files("memory.h"          HAVE_MEMORY_H)
check_include_files("opengl/glu.h"      HAVE_OPENGL_GLU_H)
check_include_files("opengl/gl.h"       HAVE_OPENGL_GL_H)
check_include_files("stdint.h"          HAVE_STDINT_H)
check_include_files("stdlib.h"          HAVE_STDLIB_H)
check_include_files("strings.h"         HAVE_STRINGS_H)
check_include_files("string.h"          HAVE_STRING_H)
check_include_files("sys/stat.h"        HAVE_SYS_STAT_H)
check_include_files("sys/types.h"       HAVE_SYS_TYPES_H)
check_include_files("unistd.h"          HAVE_UNISTD_H)
check_include_files("windows.h"         HAVE_WINDOWS_H)
check_include_files("d3d8.h"            ILUT_USE_DIRECTX8)
check_include_files("d3d9.h"            ILUT_USE_DIRECTX9)

include(CheckLibraryExists)
check_library_exists(m pow  "" HAVE_LIBM)
check_library_exists(m exp  "" HAVE_LIBM)
check_library_exists(m sqrt "" HAVE_LIBM)

include (CheckFunctionExists)
check_function_exists(valloc VALLOC)
check_function_exists(mm_malloc MM_MALLOC)
check_function_exists(posix_memalign POSIX_MEMALIGN)

include(CheckCCompilerFlag)
check_c_compiler_flag("-msse" SSE)
check_c_compiler_flag("-msse2" SSE2)
check_c_compiler_flag("-msse3" SSE3)
check_c_compiler_flag("-faltivec -maltivec" ALTIVEC_GCC)

include ( TestBigEndian )
test_big_endian(WORDS_BIGENDIAN)

find_package(OpenGL)
find_package(SDL)
if (OPENGL_FOUND)
  set (ILUT_USE_OPENGL 1)
endif ()
if (SDL_FOUND)
  set (ILUT_USE_SDL 1)
endif ()

find_package (Threads)
if(Threads_FOUND)
    if(CMAKE_USE_PTHREADS_INIT)
        set(HAVE_PTHREAD 1)
    else()
        set(HAVE_PTHREAD 0)
    endif()
endif()

if(CMAKE_SYSTEM_PROCESSOR STREQUAL "ppc")
    set(GCC_PCC_ASM 1)
    set(IL_INLINE_ASM 1)
endif()
if(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set(GCC_X86_64_ASM 1)
    set(IL_INLINE_ASM 1)
endif()
if(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86")
    set(GCC_X86_ASM 1)
    set(IL_INLINE_ASM 1)
endif()

if (APPLE)
    set (MAX_OS_X 1)
endif()

set(HAVE_LIBZ 1)
set(VECTORMEM 1)
set(STDC_HEADERS 1)
set(RESTRICT_KEYWORD 1)
set(X_DISPLAY_MISSING 1)
set(IL_NO_JP2 1)
set(IL_NO_MNG 1)
set(IL_NO_LCMS 1)
set(IL_NO_TIF 1)