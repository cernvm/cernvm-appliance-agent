#!/bin/bash
echo $(/sbin/ifconfig | grep "inet addr" |\
 grep -v "127.0.0.1" | awk '{print $2}' |\
  awk -F: '{print $2 }' | tail -n 1)
