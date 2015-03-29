#!/bin/bash
TARGET_OS="$1"
shift
docker run -t -i -v $PWD/BUILDS/:/BUILDS-RO/:ro -v $PWD/OUTPUT/:/OUTPUT/:rw zepag/rpmbuild-${TARGET_OS} /BUILDS-RW/run-builds.sh "$@"
