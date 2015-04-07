#!/bin/sh

download(){
FOLDER="$1"
URL="$2"
TARGET_NAME="$3"
HEADERS="$4"
mkdir -p /BINARIES/${FOLDER}/
if [ -f "/BINARIES/${FOLDER}/${TARGET_NAME}" ]; then
  cp /BINARIES/${FOLDER}/${TARGET_NAME} .
else
  wget --no-check-certificate --no-cookies --header="${HEADERS}"  "${URL}" -O /BINARIES/${FOLDER}/${TARGET_NAME}
  cp /BINARIES/${FOLDER}/${TARGET_NAME} .
fi
}

echo ----------------------------------------------------
echo Build-Specific variables
echo ----------------------------------------------------
PRODUCT_VERSION="5.2.7" 
echo '  'PRODUCT_VERSION: $PRODUCT_VERSION

echo ----------------------------------------------------
echo RPM package build script
echo ----------------------------------------------------
echo Jenkins environment:
echo '  'GIT_COMMIT: $GIT_COMMIT
echo '  'BUILD_NUMBER: $BUILD_NUMBER
echo '  'BUILD_ID: $BUILD_ID
echo '  'JOB_NAME: $JOB_NAME
echo '  'BUILD_TAG: $BUILD_TAG
echo '  'JAVA_HOME: $JAVA_HOME
echo '  'WORKSPACE: $WORKSPACE
echo '  'BUILD_URL: $BUILD_URL 
echo

echo ----------------------------------------------------
echo Clean up and create build directories
echo ----------------------------------------------------
for dir in BUILD BUILDROOT RPMS SRPMS TEMP
do
 [[ -d $dir ]] && rm -Rf $dir
  mkdir $dir
done
echo

echo ----------------------------------------------------
echo Downloading JDK Binary
echo ----------------------------------------------------
mkdir -p SOURCES
pushd SOURCES
download unrar \
  http://www.rarlab.com/rar/unrarsrc-${PRODUCT_VERSION}.tar.gz \
  unrarsrc-${PRODUCT_VERSION}.tar.gz
popd

echo ----------------------------------------------------
echo Build the RPM
echo ----------------------------------------------------
rpmbuild --target="x86_64" \
  --define="_topdir $PWD" \
  --define="_tmppath $PWD/TEMP" \
  --define="PRODUCT_VERSION $PRODUCT_VERSION" \
  -bb SPECS/package.spec
echo ----------------------------------------------------
echo
