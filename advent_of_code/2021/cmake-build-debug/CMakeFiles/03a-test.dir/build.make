# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /mnt/local_2tb1/ide/CLion-2021.2.3/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /mnt/local_2tb1/ide/CLion-2021.2.3/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/cschalk/projects/advent_of_code/2021

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cschalk/projects/advent_of_code/2021/cmake-build-debug

# Utility rule file for 03a-test.

# Include any custom commands dependencies for this target.
include CMakeFiles/03a-test.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/03a-test.dir/progress.make

CMakeFiles/03a-test: 03a
	./03a <"/home/cschalk/projects/advent_of_code/2021/input/03.txt"

03a-test: CMakeFiles/03a-test
03a-test: CMakeFiles/03a-test.dir/build.make
.PHONY : 03a-test

# Rule to build all files generated by this target.
CMakeFiles/03a-test.dir/build: 03a-test
.PHONY : CMakeFiles/03a-test.dir/build

CMakeFiles/03a-test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/03a-test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/03a-test.dir/clean

CMakeFiles/03a-test.dir/depend:
	cd /home/cschalk/projects/advent_of_code/2021/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cschalk/projects/advent_of_code/2021 /home/cschalk/projects/advent_of_code/2021 /home/cschalk/projects/advent_of_code/2021/cmake-build-debug /home/cschalk/projects/advent_of_code/2021/cmake-build-debug /home/cschalk/projects/advent_of_code/2021/cmake-build-debug/CMakeFiles/03a-test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/03a-test.dir/depend

