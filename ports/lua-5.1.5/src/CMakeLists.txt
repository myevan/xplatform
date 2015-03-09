set(SRC_CORE lapi.c lcode.c ldebug.c ldo.c ldump.c lfunc.c lgc.c llex.c lmem.c lobject.c lopcodes.c lparser.c lstate.c lstring.c ltable.c ltm.c  lundump.c lvm.c lzio.c)
set(SRC_LIB lauxlib.c lbaselib.c ldblib.c liolib.c lmathlib.c loslib.c ltablib.c lstrlib.c loadlib.c linit.c)
set(SRC_LUA lua.c)
set(SRC_LUAC luac.c print.c)
add_library(liblua ${SRC_CORE} ${SRC_LIB})

add_executable (lua ${SRC_LUA})
target_link_libraries(lua liblua)

add_executable (luac ${SRC_LUAC})
target_link_libraries(luac liblua)
