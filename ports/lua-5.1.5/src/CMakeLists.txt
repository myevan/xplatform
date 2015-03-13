set(SRC_CORE lapi.c lcode.c ldebug.c ldo.c ldump.c lfunc.c lgc.c llex.c lmem.c lobject.c lopcodes.c lparser.c lstate.c lstring.c ltable.c ltm.c  lundump.c lvm.c lzio.c)
set(SRC_LIB lauxlib.c lbaselib.c ldblib.c liolib.c lmathlib.c loslib.c ltablib.c lstrlib.c loadlib.c linit.c)
set(SRC_LUA lua.c)
set(SRC_LUAC luac.c print.c)
add_library(lua ${SRC_CORE} ${SRC_LIB})

add_executable (luai ${SRC_LUA})
target_link_libraries(luai lua)

add_executable (luac ${SRC_LUAC})
target_link_libraries(luac lua)

install(FILES lua.h DESTINATION include)
install(FILES lualib.h DESTINATION include)
install(FILES lauxlib.h DESTINATION include)
install(FILES luaconf.h DESTINATION include)

install(TARGETS lua luai luac 
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
