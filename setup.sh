#!/bin/bash
#Version 0.2
#Description setup tool for the cernvm-appliance-agent
#Author: Vasilis Nicolaou
#Copyright (c) CERN 2013
#All rights reserved
VERSION=0.2
APPLICATION_PATH="usr/libexec/cernvm-appliance-agent"
SERVICE_PATH="etc/init.d/cernvm-appliance-agent"
ETC_PATH="etc/cernvm-appliance-agent"
LOGS=/var/log/cernvm-appliance-agent
this_install(){
    echo -n "Installing CernVM appliance agent "
    [[ ! -d "/$APPLICATION_PATH" && ! -f "/$SERVICE_PATH" && ! -d "/$ETC_PATH" && ! -d "/$LOGS" ]] || {
        print_error "ABORTED"
        echo "The application is already installed. Run \`setup reinstall' if the installation is broken "
        exit 1
    }

    print_ok
    echo -n "Adding user account for appliance... "
    useradd -r cernvm-appliance-agent
    print_ok "DONE"
    sleep 0.5
    /bin/cp -rv "$APPLICATION_PATH" "/$APPLICATION_PATH"
    /bin/cp -v "$SERVICE_PATH" "/$SERVICE_PATH"
    chmod +x "/$SERVICE_PATH"
    /bin/cp -rv "$ETC_PATH" "/$ETC_PATH"
    chown -R cernvm-appliance-agent "/$APPLICATION_PATH/etc"
    echo -n "Starting the CernVM appliance agent apache instance daemon "
    [ $? -eq 0 ] || {
        print_error "FAILED"
        echo 
        exit 1
    }
    print_ok
    
    echo "Please add cernvm-appliance-agent to the sudoers file in order to use all the functionalities of the appliance"
    echo "e.g. put this line: cernvm-appliance-agent ALL=(ALL) NOPASSWD:ALL"
    echo "to the sudoers file"
}


this_uninstall() {
    echo "Removing CernVM appliance agent"
    this_safe_remove "/$APPLICATION_PATH"

    this_safe_remove "/$ETC_PATH"
    echo -n "Stopping CernVM appliance agent apache instance daemon "
    "/$SERVICE_PATH" stop
    this_safe_remove "/$SERVICE_PATH"
    print_ok
    echo "Deleting user account of appliance..."
    userdel -f cernvm-appliance-agent
    print_ok "DONE"
}

this_safe_remove() {
    echo "attempting to remove $1"
    [[ -f "$1" || -d "$1" ]] && {
        echo -n "Removing $1"
        /bin/rm -r "$1"
        [ $? -eq 0 ] || {
            print_error "FAILED"

        }
        print_ok
    }
}

this_reinstall() {
    echo "Reinstalling CernVM appliance agent"
    this_uninstall
    this_install
}

print_ok() {
msg="OK"
[ -n "$1" ] && {
   msg=$1
} 
echo -e "[ \e[1;32m $msg \e[0m ]"

}

print_error() {
    echo -e "[ \e[1;31m $1 \e[0m ]"
}

print_warning() {
   echo -e "[ \e[1;33m $1 \e[0m ]"    
}



case $1 in
    install)
        [ $(id -u) -eq 0 ] || {
            echo "You need to be root to run the setup"
            exit 1
        }
        this_install
        exit $?
    ;;
    uninstall)
        [ $(id -u) -eq 0 ] || {
            echo "You need to be root to run the setup"
            exit 1
        }
        this_uninstall
        
        exit $?
    ;;
    reinstall)
        [ $(id -u) -eq 0 ] || {
            echo "You need to be root to run the setup"
            exit 1
        }
        this_reinstall
        
        exit $?
    ;;
    version)
        echo "Version: $VERSION:"
        exit 0
    ;;
    *|?)
        echo "Usage $0 <install|uninstall|reinstall>"
        exit 1
    ;;
esac    
