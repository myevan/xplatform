import os
import urllib
import tarfile
import shutil


def prepare_directory(path):
    if os.access(path, os.R_OK):
        return

    os.makedirs(path)


def download_file(remote_file_uri, local_file_path):
    if os.access(local_file_path, os.R_OK):
        return

    data = urllib.urlopen(remote_file_uri).read()
    open(local_file_path, "wb").write(data)


def extract_file(archive_file_path, target_dir_path):
    tar_file = tarfile.open(archive_file_path, 'r:gz')
    tar_file.extractall(target_dir_path)


def copy_files(source_dir_path, target_dir_path):
    for base_path, dir_names, file_names in os.walk(source_dir_path):
        for file_name in file_names:
            source_file_path = os.path.join(base_path, file_name)
            target_file_path = os.path.normpath(os.path.join(
                target_dir_path, base_path[len(source_dir_path)+1:], file_name))

            shutil.copyfile(source_file_path, target_file_path)


def prepare_project(cmake_exe_path, project_dir_path, system_dir_path):
    os.system('''"{0}" {1} -DCMAKE_INSTALL_PREFIX={2}'''.format(cmake_exe_path, project_dir_path, system_dir_path))


remote_archive_uri = "http://www.lua.org/ftp/lua-5.1.5.tar.gz"

CMAKE_EXE_ABS_PATH = "c:/Program Files (x86)/CMake/bin/cmake.exe"
SOURCES_DIR_REL_PATH = "../../sources"
PREBUILTS_DIR_REL_PATH = "../../prebuilts"
MAIN_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCES_DIR_ABS_PATH = os.path.normpath(os.path.join(MAIN_DIR_PATH, SOURCES_DIR_REL_PATH))
PREBUILTS_DIR_ABS_PATH = os.path.normpath(os.path.join(MAIN_DIR_PATH, PREBUILTS_DIR_REL_PATH))
local_archive_abs_path = os.path.join(SOURCES_DIR_ABS_PATH, 'lua-5.1.5.tar.gz')
source_dir_abs_path = os.path.join(SOURCES_DIR_ABS_PATH, 'lua-5.1.5')
prebuilt_dir_abs_path = os.path.join(PREBUILTS_DIR_ABS_PATH, 'lua-5.1.5')
build_dir_abs_path = os.path.join(source_dir_abs_path, 'build')

prepare_directory(SOURCES_DIR_ABS_PATH)
download_file(remote_archive_uri, local_archive_abs_path)
extract_file(local_archive_abs_path, SOURCES_DIR_ABS_PATH)
copy_files(MAIN_DIR_PATH, source_dir_abs_path)
prepare_directory(prebuilt_dir_abs_path)
prepare_directory(build_dir_abs_path)
os.chdir(build_dir_abs_path)
prepare_project(CMAKE_EXE_ABS_PATH, source_dir_abs_path, prebuilt_dir_abs_path)

