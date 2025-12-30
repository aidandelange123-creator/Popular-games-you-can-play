#!/bin/bash

echo "Checking for .NET installation..."

# Check if dotnet is available
if ! command -v dotnet &> /dev/null; then
    echo ".NET is not installed on this system."
    echo "Installing .NET..."
    
    # Detect the Linux distribution
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$NAME
        VERSION=$VERSION_ID
    else
        echo "Cannot detect Linux distribution. Please install .NET manually."
        exit 1
    fi
    
    echo "Detected distribution: $DISTRO"
    
    # Install .NET based on the distribution
    case $DISTRO in
        *"Ubuntu"*|*"Debian"*)
            echo "Installing .NET for Ubuntu/Debian..."
            # Install required packages
            sudo apt update
            sudo apt install -y wget apt-transport-https
            
            # Add Microsoft's package repository
            wget -q https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb
            sudo dpkg -i packages-microsoft-prod.deb
            
            # Install .NET SDK
            sudo apt update
            sudo apt install -y dotnet-sdk-6.0
            ;;
        *"CentOS"*|*"Red Hat"*|*"Fedora"*)
            echo "Installing .NET for CentOS/RHEL/Fedora..."
            # Enable Microsoft's package repository
            sudo rpm -Uvh https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm
            
            # Install .NET SDK
            sudo dnf install -y dotnet-sdk-6.0
            ;;
        *"SUSE"*)
            echo "Installing .NET for SUSE..."
            # Enable Microsoft's package repository
            sudo zypper addrepo https://packages.microsoft.com/config/opensuse-leap/15.3/prod packages-microsoft-prod
            sudo zypper refresh
            
            # Install .NET SDK
            sudo zypper install -y dotnet-sdk-6.0
            ;;
        *"Arch"*)
            echo "Installing .NET for Arch Linux..."
            # Install .NET SDK from AUR (assuming yay is installed)
            if command -v yay &> /dev/null; then
                yay -S dotnet-sdk dotnet-runtime
            elif command -v paru &> /dev/null; then
                paru -S dotnet-sdk dotnet-runtime
            else
                echo "Please install yay or paru to install .NET on Arch Linux"
                exit 1
            fi
            ;;
        *)
            echo "Unsupported distribution: $DISTRO"
            echo "Please install .NET manually from: https://dotnet.microsoft.com/download"
            exit 1
            ;;
    esac
    
    if [ $? -ne 0 ]; then
        echo "Failed to install .NET SDK."
        exit 1
    else
        echo ".NET SDK installed successfully."
    fi
else
    echo ".NET is already installed."
fi

echo "Changing to .NET project directory..."
cd "$(dirname "$0")/dotnet"

echo "Building .NET application..."
dotnet build -c Release

if [ $? -ne 0 ]; then
    echo "Failed to build the application."
    exit 1
fi

echo "Running GitHub Game Player..."
dotnet run --configuration Release