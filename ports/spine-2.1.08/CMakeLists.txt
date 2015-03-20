cmake_minimum_required(VERSION 2.8)

project (spine C)

option(BUILTIN_ATLAS "enable builtin atlas" ON)

set(VERSION "2.1.08")

# to distinguish between debug and release lib
set(CMAKE_DEBUG_POSTFIX "_d")

include(cmake/msvc.cmake)

set(CORE_SOURCES
    spine-c/src/spine/Animation.c
    spine-c/src/spine/AnimationState.c
    spine-c/src/spine/AnimationStateData.c
    spine-c/src/spine/AtlasAttachmentLoader.c
    spine-c/src/spine/Attachment.c
    spine-c/src/spine/AttachmentLoader.c
    spine-c/src/spine/Bone.c
    spine-c/src/spine/BoneData.c
    spine-c/src/spine/BoundingBoxAttachment.c
    spine-c/src/spine/Event.c
    spine-c/src/spine/EventData.c
    spine-c/src/spine/IkConstraint.c
    spine-c/src/spine/IkConstraintData.c
    spine-c/src/spine/Json.c
    spine-c/src/spine/MeshAttachment.c
    spine-c/src/spine/RegionAttachment.c
    spine-c/src/spine/Skeleton.c
    spine-c/src/spine/SkeletonBounds.c
    spine-c/src/spine/SkeletonData.c
    spine-c/src/spine/SkeletonJson.c
    spine-c/src/spine/Skin.c
    spine-c/src/spine/SkinnedMeshAttachment.c
    spine-c/src/spine/Slot.c
    spine-c/src/spine/SlotData.c
    spine-c/src/spine/extension.c)

if(BUILTIN_ATLAS)
    set(ATLAS_SOURCES
        spine-c/src/spine/Atlas.c)
endif()

set(PUBLIC_HEADERS
    spine-c/include/spine/Animation.h
    spine-c/include/spine/AnimationState.h
    spine-c/include/spine/AnimationStateData.h
    spine-c/include/spine/Atlas.h
    spine-c/include/spine/AtlasAttachmentLoader.h
    spine-c/include/spine/Attachment.h
    spine-c/include/spine/AttachmentLoader.h
    spine-c/include/spine/Bone.h
    spine-c/include/spine/BoneData.h
    spine-c/include/spine/BoundingBoxAttachment.h
    spine-c/include/spine/Event.h
    spine-c/include/spine/EventData.h
    spine-c/include/spine/IkConstraint.h
    spine-c/include/spine/IkConstraintData.h
    spine-c/include/spine/MeshAttachment.h
    spine-c/include/spine/RegionAttachment.h
    spine-c/include/spine/Skeleton.h
    spine-c/include/spine/SkeletonBounds.h
    spine-c/include/spine/SkeletonData.h
    spine-c/include/spine/SkeletonJson.h
    spine-c/include/spine/Skin.h
    spine-c/include/spine/SkinnedMeshAttachment.h
    spine-c/include/spine/Slot.h
    spine-c/include/spine/SlotData.h
    spine-c/include/spine/extension.h
    spine-c/include/spine/spine.h)

include_directories(spine-c/include)

add_library(spine STATIC ${CORE_SOURCES} ${ATLAS_SOURCES})

install(FILES ${PUBLIC_HEADERS} DESTINATION include/spine)

install(TARGETS spine
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib/static)
