cmake_minimum_required(VERSION 2.8)
project(Factory)
set(CMAKE_CXX_FLAGS "-std=c++11 -pthread")

find_package(GTest REQUIRED)
find_package(Boost REQUIRED COMPONENTS system filesystem thread)

include_directories(${GTEST_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
include_directories(.)

add_library(singleton singleton.cpp)

add_executable(testy tests.cpp)

target_link_libraries(testy ${GTEST_BOTH_LIBRARIES})
target_link_libraries(testy ${Boost_LIBRARIES})
target_link_libraries(testy singleton)

