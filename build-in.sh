#!/bin/bash
usage(){
  echo "usage:"
  echo "  $0 <target_os> <rpm_source...>"
  echo " where target_os matches an existing zepag/rpmbuild-<target_os> docker container"
  echo " where rpm_source is a list of source folders found in $PWD/BUILDS, separated by spaces"
  exit 1
}
[ -z "$1" ] && usage
[ -z "$2" ] && usage
TARGET_OS="$1"
CONTAINER_HOST="$(echo ${TARGET_OS}|sed -e 's/\.//g').rpmbuild"
TARGET_CONTAINER="zepag/rpmbuild-${TARGET_OS}"
shift
mkdir -p "$PWD/OUTPUT/${TARGET_OS}"
for rpm_source in "$@"
do
  if [ -f "$PWD/CUSTOM_CONTAINERS/${TARGET_OS}/${rpm_source}/Dockerfile" ]; then
    pushd $PWD/CUSTOM_CONTAINERS/${TARGET_OS}/${rpm_source}/ 2>&1 > /dev/null
    docker build -t "zepag/rpmbuild-${TARGET_OS}-${rpm_source}" . && TARGET_CONTAINER="zepag/rpmbuild-${TARGET_OS}-${rpm_sourceex}"
    popd 2>&1 > /dev/null
  fi
done
echo " |> Running container: ${TARGET_CONTAINER}"
docker run -t -i \
  --rm \
  -h ${CONTAINER_HOST} \
  -v $PWD/BUILDS/:/BUILDS-RO/:ro \
  -v "$PWD/OUTPUT/${TARGET_OS}"/:/OUTPUT/:rw \
  -v "$PWD/BINARIES/"/:/BINARIES/:rw \
  ${TARGET_CONTAINER} "$@"
