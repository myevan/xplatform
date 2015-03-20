# Minimal CMake project for building a static library under Windows.

cmake_minimum_required (VERSION 2.8)

project (yaml C)


set (YAML_VERSION_MAJOR 0)
set (YAML_VERSION_MINOR 1)
set (YAML_VERSION_PATCH 5)
set (YAML_VERSION_STRING "${YAML_VERSION_MAJOR}.${YAML_VERSION_MINOR}.${YAML_VERSION_PATCH}")


# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")


include(cmake/configure.cmake)
configure_file(config.h.cmake ${CMAKE_CURRENT_SOURCE_DIR}/config.h)

file (GLOB SRC src/*.c)

include_directories (include win32)
add_definitions (-DHAVE_CONFIG_H -DYAML_DECLARE_STATIC)
add_library (yaml STATIC ${SRC})

install(FILES include/yaml.h DESTINATION include)

install(TARGETS yaml 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
