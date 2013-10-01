#!/bin/bash

#This file contains only functions that are
#useful during testing. Nothing important should be put here.

rpm2tar() {
    RPM_DATABASE=$1
    ifs_b=$IFS
    IFS=$'\n'
    TEMP_DIR=$(mktemp -d)
    PROVIDES_DIR="$TEMP_DIR/provides"
    CONFLICTS_DIR="$TEMP_DIR/conflicts"
    POSTIN_DIR="$TEMP_DIR/scripts.postinstall"
    mkdir "$PROVIDES_DIR"
    mkdir "$CONFLICTS_DIR"
    mkdir "$POSTIN_DIR"
    
    for package in `rpm --dbpath $RPM_DATABASE -qa`; do
        rpm  --dbpath "$RPM_DATABASE" -q --provides "$package" | cat >"$PROVIDES_DIR/$package"
        rpm  --dbpath "$RPM_DATABASE" -q --conflicts "$package" | cat >"$CONFLICTS_DIR/$package"
                
        rpm --dbpath "$RPM_DATABASE" -q --qf "\#\!%{POSTINPROG}\n%{POSTIN}\n" "$package" | cat >"$POSTIN_DIR/$package"
        
    done
    echo "TARBALL FOR CONFLICTS" | cat >README
    tar -cf "update.tar" README
    curr_dir=`echo $(pwd)/update.tar`
    cd $TEMP_DIR
    for file in `ls`; do
        tar -rf "$curr_dir" $file
        tar -rf "$curr_dir" $file
        tar -rf "$curr_dir" $file
    done
    echo $curr_dir
}

replace_hash() {
    FILE_PATH=$1
    HASH_INDEX=$2
    line=`cat cernvm_hashes.data | head -n $HASH_INDEX | tail -n 1`
    cvm_hash=`echo $line | cut -d '|' -f 2 | tr -d ' '`
    echo "$cvm_hash is the hash"
    echo $cvm_hash | cat >$FILE_PATH
    echo "HEAD" | cat >>$FILE_PATH
}

backup_database() {
    
    DIRECTORY=$1
    DATABASE=$2
    curr_path=$(pwd)
    cd $DIRECTORY
    tar -cvf "$curr_path/backup$DATABASE.tar" $DATABASE
    cd $curr_path
}

diff_databases() {
    database1=$(mktemp)
    database2=$(mktemp)
    rpm --dbpath $1 -qa | sort -d | cat >$database1
    rpm --dbpath $2 -qa | sort -d | cat >$database2
    diff --normal $database1 $database2 | grep '>' | tr -d '>' | tr -d ' ' |
cat >user_packages
}

RO_RPM_DATABASE="/mnt/.ro/cvm3/var/lib/rpm"
RW_RPM_DATABASE="/var/lib/rpm/"
#TAR_FILE=`rpm2tar $RO_RPM_DATABASE`
#mv "$TAR_FILE" .
#backup_database "/mnt/.rw/persistent/var/lib/" "rpm"
diff_databases $RO_RPM_DATABASE $RW_RPM_DATABASE
#replace_hash /mnt/.rw/aux/cvmfs_snapshot 1
