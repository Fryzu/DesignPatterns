cmake_minimum_required(VERSION 2.8)
project(Factory)
set(CMAKE_CXX_FLAGS "-std=c++11 -pthread")

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_library(factory factory.cpp)

add_executable(testy tests.cpp)

target_link_libraries(testy ${GTEST_BOTH_LIBRARIES})
target_link_libraries(testy factory)

