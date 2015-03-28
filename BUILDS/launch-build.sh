#!/bin/bash

usage(){
  echo "usage:"
  echo "  sh $0 <exampleid>"
  exit 1
}

error() {
  echo "$1"
  exit 2
}
SCRIPT="$(readlink -f $0)"
BUILD_PATH="$(dirname $SCRIPT)/$1/"

[ -z "$1" ] && usage
[ -d "$BUILD_PATH" ] || error "No folder '$BUILD_PATH'"
cd $BUILD_PATH
sh ${BUILD_PATH}/build.sh
