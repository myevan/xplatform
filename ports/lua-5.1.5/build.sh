mkdir -p ../../prebuilts/lua-5.1.5/
mkdir -p ../../sources/
pushd ../../sources/
wget http://www.lua.org/ftp/lua-5.1.5.tar.gz
tar -zxvf lua-5.1.5.tar.gz
cd lua-5.1.5
cp -r ../../ports/lua-5.1.5/* .
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../../../prebuilts/lua-5.1.5/
make install
popd
