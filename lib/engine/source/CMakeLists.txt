cmake_minimum_required(VERSION 2.6)
project(CHECKERS)

find_package(PkgConfig)

set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_FLAGS "-g -Wall -std=c++0x")

add_library(checkers SHARED AI.cpp NewAI.cpp BitBoard.cpp Game.cpp Save.cpp)