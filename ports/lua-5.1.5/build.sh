mkdir -p ../../tmp
pushd ../../tmp
#wget http://www.lua.org/ftp/lua-5.1.5.tar.gz
#tar -zxvf lua-5.1.5.tar.gz
cd lua-5.1.5
cp -r ../../ports/lua-5.1.5/* .
mkdir -p build
cd build
cmake ..
make
popd
