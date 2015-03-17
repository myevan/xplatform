#!/usr/bin/env python
import os
import urllib
import tarfile
import shutil

from urlparse import urlparse

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


def find_cmake_abs_path():
    if os.name == 'nt': 
        return "c:/Program Files (x86)/CMake/bin/cmake.exe"
    else:
        return "cmake"

def build_project(working_dir_abs_path, target_builder_name, remote_archive_uri, archive_file_name=None):
    if archive_file_name is None:
        archive_file_name = os.path.split(urlparse(remote_archive_uri).path)[1]

    if archive_file_name.endswith('.gz'):
        archive_name = os.path.splitext(os.path.splitext(archive_file_name)[0])[0]
    else:
        archive_name = os.path.splitext(archive_file_name)[0]

    local_archive_abs_path = os.path.join(SOURCES_DIR_ABS_PATH, archive_file_name)
    source_dir_abs_path = os.path.join(SOURCES_DIR_ABS_PATH, archive_name)
    prebuilt_dir_abs_path = os.path.join(PREBUILTS_DIR_ABS_PATH, archive_name)
    build_dir_abs_path = os.path.join(source_dir_abs_path, 'build')

    prepare_directory(SOURCES_DIR_ABS_PATH)
    download_file(remote_archive_uri, local_archive_abs_path)
    extract_file(local_archive_abs_path, SOURCES_DIR_ABS_PATH)
    copy_files(working_dir_abs_path, source_dir_abs_path)

    prepare_directory(prebuilt_dir_abs_path)
    prepare_directory(build_dir_abs_path)

    os.chdir(build_dir_abs_path)

    if target_builder_name == 'clean':
        shutil.rmtree(build_dir_abs_path)
    elif target_builder_name == 'make':
        os.system('''"{0}" {1} -DCMAKE_INSTALL_PREFIX={2}'''.format(CMAKE_EXE_ABS_PATH, source_dir_abs_path, prebuilt_dir_abs_path))
        os.system('''make''')
    elif target_builder_name == 'build_osx':
        os.system('''"{0}" -G Xcode {1} -DCMAKE_INSTALL_PREFIX={2}'''.format(CMAKE_EXE_ABS_PATH, source_dir_abs_path, prebuilt_dir_abs_path))
        os.system('''xcodebuild''')
    elif target_builder_name == 'build_ios':
        os.system('''"{0}" -G Xcode {1} -DCMAKE_TOOLCHAIN_FILE=../../../toolchains/ios.cmake  -DCMAKE_INSTALL_PREFIX={2}'''.format(CMAKE_EXE_ABS_PATH, source_dir_abs_path, prebuilt_dir_abs_path))

        os.system('''xcodebuild -configuration Debug''')
        os.system('''xcodebuild -configuration Debug -sdk iphoneos''')
        os.system('''xcodebuild -configuration Release''')
        os.system('''xcodebuild -configuration Release -sdk iphoneos''')

        if output_file_name.endswith('.a'):
            output_head, output_tail = os.path.split(output_file_name)
            debug_output_file_path = output_head + '_d' + output_tail
            debug_dev_output_file_path = os.path.join(build_dir_abs_path, 'Debug-iphoneos', debug_output_file_name)
            debug_sim_output_ile_path = os.path.join(build_dir_abs_path, 'Debug-iphonesimulator', debug_output_file_name)
            release_output_file_path = output_head + '_d' + output_tail
            release_dev_output_file_path = os.path.join(build_dir_abs_path, 'Debug-iphoneos', release_output_file_name)
            release_sim_output_file_path = os.path.join(build_dir_abs_path, 'Debug-iphonesimulator', release_output_file_name)
            os.system('''lipo -create -output {1} {1} {2}'''.format(
                archive_name, debug_output_file_name, debug_dev_output_file_path, debug_sim_output_ile_path))
            os.system('''lipo -create -output {1} {1} {2}'''.format(
                archive_name, release_output_file_name, release_dev_output_file_path, release_sim_output_ile_path))
    else:
        print('NOT_SUPPORTED_BUILDER:{0}'.format(target_builder_name))
   

SOURCES_DIR_REL_PATH = "../sources"
PREBUILTS_DIR_REL_PATH = "../prebuilts"
CMAKE_EXE_ABS_PATH = find_cmake_abs_path()
MODULE_DIR_ABS_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCES_DIR_ABS_PATH = os.path.normpath(os.path.join(MODULE_DIR_ABS_PATH, SOURCES_DIR_REL_PATH))
PREBUILTS_DIR_ABS_PATH = os.path.normpath(os.path.join(MODULE_DIR_ABS_PATH, PREBUILTS_DIR_REL_PATH))

if __name__ == '__main__':
    import sys
    import json

    def main():
        if len(sys.argv) <= 2:
            print("USAGE:")
            print("\t{0} [clean|make|xcode] [package_dir_path]".format(sys.argv[0]))
            return -1
          
        package_dir_abs_path = os.path.realpath(sys.argv[2])
        package_info_abs_path = os.path.join(package_dir_abs_path, 'info.json')
        package_info_dict = json.loads(open(package_info_abs_path).read())
        build_project(
                package_dir_abs_path, 
                sys.argv[1], 
                remote_archive_uri=package_info_dict['REMOTE_ARCHIVE_URI'], 
                local_archive_abs_path=package_info_dict.get('LOCAL_ARCHIVE_FILE_NAME', None),
                local_archive_abs_path=package_info_dict.get('OUTPUT_FILE_NAME', None))
        return 0

    sys.exit(main())

