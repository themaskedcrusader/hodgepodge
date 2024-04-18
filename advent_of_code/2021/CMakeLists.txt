# Created by TheMaskedCrusader on 2021/12/13.
cmake_minimum_required(VERSION 3.16)
project(advent_of_code_2021)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(input_dir "${CMAKE_CURRENT_SOURCE_DIR}/input")


function (advent name data)
    set(options "")
    set(one_value_args VALIDATE)
    set(multi_value_args LIBRARIES SOURCES)
    cmake_parse_arguments(CREATE_PUZZLE "${options}" "${one_value_args}" "${multi_value_args}" ${ARGN})
    add_executable(${name}
            advent/${name}.cpp
            ${CREATE_PUZZLE_SOURCES}
            )
    if(CREATE_PUZZLE_LIBRARIES)
        target_link_libraries(${name}
                PRIVATE ${CREATE_PUZZLE_LIBRARIES}
                )
    endif()
    target_compile_features(${name} PRIVATE
            cxx_std_17
            )
    set_target_properties(${name} PROPERTIES
            CXX_EXTENSIONS OFF
            )
    add_custom_target(${name}-test
            DEPENDS ${name}
            COMMAND $<TARGET_FILE:${name}> <"${input_dir}/${data}.txt"
            )
    if(CREATE_PUZZLE_VALIDATE)
        set(validate_test "${name}-validate")
        add_test(${validate_test}
                ${name} "${input_dir}/${name}"
                )
        set_tests_properties(${name}-validate PROPERTIES
                PASS_REGULAR_EXPRESSION "${CREATE_PUZZLE_VALIDATE}"
                )
    endif()
endfunction(advent)

advent(00 00)