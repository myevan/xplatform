#!/usr/bin/env python
import os
import glob
import shutil
import tarfile
import subprocess

from scripts import wget
from scripts import patch
from urlparse import urlparse


def prepare_directory(path):
    if os.access(path, os.R_OK):
        return

    os.makedirs(path)


def download_file(remote_file_uri, local_file_path):
    if os.access(local_file_path, os.R_OK):
        print('found_archive\n\tremote_uri:{0}\n\tlocal_file:{1}'.format(remote_file_uri, local_file_path))
        return

    print('download_archive\n\tremote_uri:{0}\n\tlocal_file:{1}'.format(remote_file_uri, local_file_path))
    wget.download(remote_file_uri, out=local_file_path)
    print('')


def extract_file(archive_file_path, target_dir_path):
    print('extract_archive\n\tarchive_file:{0}\n\ttarget_dir:{1}'.format(archive_file_path, target_dir_path))

    tar_file = tarfile.open(archive_file_path, 'r:gz')
    for member in tar_file.getmembers():
        # ignore first directory for differnt archive_name and target_directory_name
        member.name = '/'.join(member.name.split('/')[1:])
        tar_file.extract(member, target_dir_path)


def copy_files(source_dir_path, target_dir_path):
    for base_path, dir_names, file_names in os.walk(source_dir_path):
        for dir_name in list(dir_names):
            if dir_name == 'platform':
                dir_names.remove('platform')

        for file_name in file_names:
            if file_name.endswith('.patch'):
                continue

            source_file_path = os.path.join(base_path, file_name)
            target_file_path = os.path.normpath(os.path.join(
                target_dir_path, base_path[len(source_dir_path)+1:], file_name))

            target_branch = os.path.split(target_file_path)[0]
            if not os.access(target_branch, os.R_OK):
                os.makedirs(target_branch)

            shutil.copyfile(source_file_path, target_file_path)


def apply_patches(patch_dir_path, target_dir_path):
    patch_file_paths = glob.glob(os.path.join(patch_dir_path, '*.patch'))
    if patch_file_paths:
        print('apply_patch_dir:{0}'.format(patch_dir_path))
        for patch_file_path in patch_file_paths:
            print('\tpatch_file:{0}'.format(patch_file_path))
            patch_set = patch.fromfile(patch_file_path)
            patch_set.apply(strip=2, root=target_dir_path)


def find_cmake_abs_path():
    if os.name == 'nt': 
        return "c:/Program Files (x86)/CMake/bin/cmake.exe"
    else:
        return "cmake"


def find_visual_studio_devev():
    return "c:/Program Files (x86)/Microsoft Visual Studio 12.0/Common7/IDE/devenv.exe"


def prepare_platform_directory(platform_name, project_name):
    platform_dir_abs_path = os.path.join(PLATFORMS_DIR_ABS_PATH, platform_name, project_name)
    prepare_directory(platform_dir_abs_path)
    return platform_dir_abs_path


def make_universal_library(output_dir_path, pattern, install_dir_path):
    print("make_universal_library:{0} install:{1}".format(output_dir_path, install_dir_path))
    lib_file_paths = []
    for base_path, dir_names, file_names in os.walk(output_dir_path):
        for file_name in file_names:
            if file_name.endswith('.a'):
                if ".build" in base_path and pattern in base_path:
                    lib_file_path = os.path.join(base_path, file_name)
                    print("found_lib:{0}".format(lib_file_path[len(output_dir_path) + 1:]))
                    lib_file_paths.append(lib_file_path)

    lib_file_name = os.path.split(lib_file_paths[0])[1]
    install_file_path = os.path.join(install_dir_path, lib_file_name)

    prepare_directory(install_dir_path)
    make_universal_debug_lib_args = ['lipo', '-create', '-output', install_file_path]
    make_universal_debug_lib_args += lib_file_paths
    print(' '.join(make_universal_debug_lib_args))
    subprocess.call(make_universal_debug_lib_args)


def build_project(port_dir_abs_path, port_info_dict, command_name, command_options=[]):
    remote_archive_uri = port_info_dict['REMOTE_ARCHIVE_URI']
    archive_file_name = port_info_dict.get('LOCAL_ARCHIVE_FILE_NAME', os.path.split(urlparse(remote_archive_uri).path)[1])

    if archive_file_name.endswith('.gz'):
        archive_name = os.path.splitext(os.path.splitext(archive_file_name)[0])[0]
    else:
        archive_name = os.path.splitext(archive_file_name)[0]

    project_name = archive_name

    archive_file_abs_path = os.path.join(ARCHIVES_DIR_ABS_PATH, archive_file_name)
    source_dir_abs_path = os.path.join(SOURCES_DIR_ABS_PATH, archive_name)
    build_dir_abs_path = os.path.join(source_dir_abs_path, '__build')

    prepare_directory(build_dir_abs_path)
    os.chdir(build_dir_abs_path)

    if command_name == 'clean':
        shutil.rmtree(build_dir_abs_path)
        return

    prepare_directory(ARCHIVES_DIR_ABS_PATH)
    download_file(remote_archive_uri, archive_file_abs_path)
    if command_name == 'download':
        return

    prepare_directory(source_dir_abs_path)
    extract_file(archive_file_abs_path, source_dir_abs_path)
    copy_files(port_dir_abs_path, source_dir_abs_path)
    apply_patches(port_dir_abs_path, source_dir_abs_path)

    if command_name.startswith('build'):
        tokens = command_name.split('_')
        if len(tokens) == 2:
            platform_name = tokens[1]
        else:
            platform_name = 'posix'
    else:
        print('NOT_SUPPORTED_COMMAND:{0}'.format(command_name))

    platform_dir_abs_path = os.path.join(port_dir_abs_path, 'platform', platform_name)
    if os.access(platform_dir_abs_path, os.R_OK):
        copy_files(platform_dir_abs_path, source_dir_abs_path)
        apply_patches(platform_dir_abs_path, source_dir_abs_path)

    if platform_name == 'posix':
        platform_dir_abs_path = prepare_platform_directory('posix', project_name)

        os.system('''"{0}" {1} -DCMAKE_INSTALL_PREFIX={2} {3}'''.format(
            CMAKE_EXE_ABS_PATH, source_dir_abs_path, platform_dir_abs_path, ' '.join(command_options)))
        os.system('''make install''')
    elif platform_name == 'win':
        platform_dir_abs_path = prepare_platform_directory('win/VS2013', project_name)

        subprocess.call([
           CMAKE_EXE_ABS_PATH,
           '-G', 'Visual Studio 12 2013',
           source_dir_abs_path,
           '-DCMAKE_INSTALL_PREFIX={0}'.format(platform_dir_abs_path)] + command_options)

        vs_devenv_abs_path = find_visual_studio_devev()
        vs_solution_abs_path = os.path.join(build_dir_abs_path, project_name + ".sln")
        subprocess.call([vs_devenv_abs_path, vs_solution_abs_path, '/build', 'Debug', '/project', 'ALL_BUILD'])
        subprocess.call([vs_devenv_abs_path, vs_solution_abs_path, '/build', 'Release', '/project', 'ALL_BUILD'])
        subprocess.call([vs_devenv_abs_path, vs_solution_abs_path, '/build', 'Debug', '/project', 'INSTALL'])
        subprocess.call([vs_devenv_abs_path, vs_solution_abs_path, '/build', 'Release', '/project', 'INSTALL'])

    elif platform_name == 'osx':
        platform_dir_abs_path = prepare_platform_directory('osx', project_name)

        os.system('''"{0}" -G Xcode {1} -DCMAKE_INSTALL_PREFIX={2} {3}'''.format(
            CMAKE_EXE_ABS_PATH, source_dir_abs_path, platform_dir_abs_path, ' '.join(command_options)))
        os.system('''xcodebuild -configuration Debug -target install''')
        os.system('''xcodebuild -configuration Release -target install''')
    elif platform_name == 'ios':
        platform_dir_abs_path = prepare_platform_directory('ios', project_name)
        os.system('''"{0}" -G Xcode {1} -DCMAKE_TOOLCHAIN_FILE=../../../toolchains/ios.cmake  -DCMAKE_INSTALL_PREFIX={2} {3}'''.format(
            CMAKE_EXE_ABS_PATH, source_dir_abs_path, platform_dir_abs_path, ' '.join(command_options)))
        os.system('''xcodebuild -configuration Debug -sdk iphoneos -arch armv7 -arch armv7s -arch arm64''')
        os.system('''xcodebuild -configuration Release -sdk iphoneos -arch armv7 -arch armv7s -arch arm64''')
        os.system('''xcodebuild -configuration Debug -sdk iphonesimulator -arch i386 -arch x86_64''')
        os.system('''xcodebuild -configuration Release -sdk iphonesimulator -arch i386 -arch x86_64''')
        os.system('''xcodebuild -configuration Debug -target install''')
        os.system('''xcodebuild -configuration Release -target install''')

        platform_lib_dir_abs_path = os.path.join(platform_dir_abs_path, 'lib', 'static')
        output_dir_rel_path = port_info_dict.get('OUTPUT_DIR', '')
        output_dir_abs_path = os.path.join(build_dir_abs_path, 'CMakeBuild/libpython/Python27.build') if output_dir_rel_path else build_dir_abs_path

        make_universal_library(output_dir_abs_path, 'Debug', platform_lib_dir_abs_path)
        make_universal_library(output_dir_abs_path, 'Release', platform_lib_dir_abs_path)
    elif platform_name == 'and':
        platform_dir_abs_path = prepare_platform_directory('and', project_name)

        cmake_args = [
           CMAKE_EXE_ABS_PATH,
           source_dir_abs_path,
           '-DCMAKE_TOOLCHAIN_FILE=../../../toolchains/android.cmake', 
           '-DANDROID_NDK={0}'.format(os.environ['NDK_ROOT']), 
           '-DCMAKE_BUILD_TYPE=Release', 
           '-DANDROID_ABI=armeabi-v7a with NEON', 
           '-DCMAKE_INSTALL_PREFIX={0}'.format(platform_dir_abs_path)] 
        cmake_args += command_options
        print(' '.join(cmake_args))
        subprocess.call(cmake_args)
        subprocess.call(['make', 'VERBOSE=1'])
        subprocess.call(['make', 'install'])
    else:
        print('NOT_SUPPORTED_PLATFORM:{0}'.format(platform_name))


ARCHIVES_DIR_REL_PATH = "./archives"
SOURCES_DIR_REL_PATH = "./sources"
PLATFORMS_DIR_REL_PATH = "./platforms"
CMAKE_EXE_ABS_PATH = find_cmake_abs_path()
MODULE_DIR_ABS_PATH = os.path.dirname(os.path.realpath(__file__))
ARCHIVES_DIR_ABS_PATH = os.path.normpath(os.path.join(MODULE_DIR_ABS_PATH, ARCHIVES_DIR_REL_PATH))
SOURCES_DIR_ABS_PATH = os.path.normpath(os.path.join(MODULE_DIR_ABS_PATH, SOURCES_DIR_REL_PATH))
PLATFORMS_DIR_ABS_PATH = os.path.normpath(os.path.join(MODULE_DIR_ABS_PATH, PLATFORMS_DIR_REL_PATH))

if __name__ == '__main__':
    import sys
    import json

    def main():
        if len(sys.argv) <= 2:
            print("USAGE:")
            print("\t{0} [clean|build|build_win|build_osx|build_ios] [port_dir_path]".format(sys.argv[0]))
            return -1

        options = sys.argv[3:]
        port_dir_abs_path = os.path.realpath(sys.argv[2])
        port_info_abs_path = os.path.join(port_dir_abs_path, 'info.json')
        port_info_dict = json.loads(open(port_info_abs_path).read())

        build_project(
            port_dir_abs_path,
            port_info_dict,
            sys.argv[1],
            options)

        return 0

    sys.exit(main())

