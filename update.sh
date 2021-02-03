#!/bin/bash

RED="\033[1;31m"
GREEN="\033[1;32m"
NOCOLOR="\033[0m"

echo

echo -e "${GREEN}Step 1: Pre-configuring packages...${NOCOLOR}"
sudo dpkg --configure -a

echo

echo -e "${GREEN}Step 2: Fixing and attempting to correct any system with broken dependencies...${NOCOLOR}"
sudo apt-get install -f

echo

echo -e "${GREEN}Step 3: Updating apt cache...${NOCOLOR}"
sudo apt-get update -y

echo

echo -e "${GREEN}Step 4: Upgrading Packages...${NOCOLOR}"
sudo apt-get upgrade -y

echo

echo -e "${GREEN}Step 5: Distro Upgrade...${NOCOLOR}"
sudo apt-get dist-upgrade

echo

echo -e "${GREEN}Step 6: Removing Unused Packages...${NOCOLOR}"
sudo apt-get --purge autoremove

echo

echo -e "${GREEN}Step 7: Cleaning up...${NOCOLOR}"
sudo apt-get autoclean

echo
