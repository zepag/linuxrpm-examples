#!/bin/bash
usage(){
  echo "usage:"
  echo "  $0 <target_os> "
  echo " where target_os matches an existing zepag/rpmbuild-<target_os> docker container"
  exit 1
}
[ -z "$1" ] && usage
TARGET_OS="$1"
CONTAINER_HOST="$(echo ${TARGET_OS}|sed -e 's/\.//g').rpmbuild"
shift
mkdir -p "$PWD/OUTPUT/${TARGET_OS}"
docker run -t -i \
  --rm \
  -h ${CONTAINER_HOST} \
  -v $PWD/BUILDS/:/BUILDS-RO/:ro \
  -v "$PWD/OUTPUT/${TARGET_OS}"/:/OUTPUT/:rw \
  -v "$PWD/BINARIES/"/:/BINARIES/:rw \
  --entrypoint=/bin/bash \
  zepag/rpmbuild-${TARGET_OS} 
