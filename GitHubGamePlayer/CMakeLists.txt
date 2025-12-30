cmake_minimum_required(VERSION 3.10)
project(GitHubGamePlayer)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add executable
add_executable(GitHubGamePlayer src/main.cpp)

# Set output directory
set_target_properties(GitHubGamePlayer PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Platform-specific settings
if(WIN32)
    # Windows-specific settings
    target_compile_definitions(GitHubGamePlayer PRIVATE _WIN32)
endif()

# Installation
install(TARGETS GitHubGamePlayer
    RUNTIME DESTINATION bin
)