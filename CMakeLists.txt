cmake_minimum_required(VERSION 3.20.0)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

project(mlir-experiment)

set(CMAKE_CXX_STANDARD 17)

include(ExternalProject)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")


# #########
# LLVM & MLIR
# #########
find_package(LLVM)
if(NOT MLIR_DIR)
  set(MLIR_DIR ${LLVM_LIBRARY_DIRS}/cmake/mlir)
endif()
find_package(MLIR REQUIRED CONFIG PATHS ${MLIR_DIR})

list(APPEND CMAKE_MODULE_PATH "${MLIR_CMAKE_DIR}")
list(APPEND CMAKE_MODULE_PATH "${LLVM_CMAKE_DIR}")

include(TableGen) # required by AddMLIR
include(AddLLVM)
include(AddMLIR)

include_directories(${LLVM_INCLUDE_DIRS})
include_directories(${MLIR_INCLUDE_DIRS})

add_subdirectory(tests)


