cmake_minimum_required(VERSION 2.8)
project (yaml-0.1.5)

macro(macro_add_definition_if FOUND_VAR)
    if (${FOUND_VAR})
        add_definitions(-D${FOUND_VAR}=1)
    endif(${FOUND_VAR})
endmacro(macro_add_definition_if)

include(CheckIncludeFiles)

check_include_files("dlfcn.h" HAVE_DLFCN_H)
check_include_files("inttypes.h" HAVE_INTTYPES_H)
check_include_files("memory.h" HAVE_MEMORY_H)
check_include_files("stdint.h" HAVE_STDINT_H)
check_include_files("stdlib.h" HAVE_STDLIB_H)
check_include_files("strings.h" HAVE_STRINGS_H)
check_include_files("string.h" HAVE_STRING_H)
check_include_files("sys/stat.h" HAVE_SYS_STAT_H)
check_include_files("sys/types.h" HAVE_SYS_TYPES_H)
check_include_files("unistd.h" HAVE_UNISTD_H)

macro_add_definition_if(HAVE_DLFCN_H)
macro_add_definition_if(HAVE_INTTYPES_H)
macro_add_definition_if(HAVE_MEMORY_H)
macro_add_definition_if(HAVE_STDINT_H)
macro_add_definition_if(HAVE_STDLIB_H)
macro_add_definition_if(HAVE_STRINGS_H)
macro_add_definition_if(HAVE_STRING_H)
macro_add_definition_if(HAVE_SYS_TYPES_H)
macro_add_definition_if(HAVE_SYS_STAT_H)
macro_add_definition_if(HAVE_UNISTD_H)

#add_definitions (-DHAVE_CONFIG_H -DYAML_DECLARE_STATIC)
add_definitions (-DYAML_DECLARE_STATIC)
add_definitions (-DYAML_VERSION_MAJOR=0)
add_definitions (-DYAML_VERSION_MINOR=1)
add_definitions (-DYAML_VERSION_PATCH=5)
add_definitions (-DYAML_VERSION_STRING="0.1.5")

include_directories (include)
file (GLOB SRC src/*.c)
add_library(yaml ${SRC})

install(FILES include/yaml.h DESTINATION include)

install(TARGETS yaml 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)

if (TEST)
    add_executable (test-reader tests/test-reader.c)
    target_link_libraries(test-reader yaml)

    install(TARGETS test-reader 
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION lib
            ARCHIVE DESTINATION lib/static)
endif ()

