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
CMAKE_SOURCE_DIR = /home/cschalk/projects/codeeval/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cschalk/projects/codeeval/cpp/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/challenge_220.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/challenge_220.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/challenge_220.dir/flags.make

CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o: CMakeFiles/challenge_220.dir/flags.make
CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o: ../easy/challenge_220.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/cschalk/projects/codeeval/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o -c /home/cschalk/projects/codeeval/cpp/easy/challenge_220.cpp

CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/cschalk/projects/codeeval/cpp/easy/challenge_220.cpp > CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.i

CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/cschalk/projects/codeeval/cpp/easy/challenge_220.cpp -o CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.s

# Object files for target challenge_220
challenge_220_OBJECTS = \
"CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o"

# External object files for target challenge_220
challenge_220_EXTERNAL_OBJECTS =

challenge_220: CMakeFiles/challenge_220.dir/easy/challenge_220.cpp.o
challenge_220: CMakeFiles/challenge_220.dir/build.make
challenge_220: CMakeFiles/challenge_220.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/cschalk/projects/codeeval/cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable challenge_220"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/challenge_220.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/challenge_220.dir/build: challenge_220
.PHONY : CMakeFiles/challenge_220.dir/build

CMakeFiles/challenge_220.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/challenge_220.dir/cmake_clean.cmake
.PHONY : CMakeFiles/challenge_220.dir/clean

CMakeFiles/challenge_220.dir/depend:
	cd /home/cschalk/projects/codeeval/cpp/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cschalk/projects/codeeval/cpp /home/cschalk/projects/codeeval/cpp /home/cschalk/projects/codeeval/cpp/cmake-build-debug /home/cschalk/projects/codeeval/cpp/cmake-build-debug /home/cschalk/projects/codeeval/cpp/cmake-build-debug/CMakeFiles/challenge_220.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/challenge_220.dir/depend

