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
JAVA_VERSION="1.8.0"
JAVA_TM_VERSION="8"
JAVA_RELEASE="40"
JAVA_BUILD="26"
echo '  'JAVA_VERSION: $JAVA_VERSION
echo '  'JAVA_TM_VERSION: $JAVA_TM_VERSION
echo '  'JAVA_RELEASE: $JAVA_RELEASE
echo '  'JAVA_BUILD: $JAVA_BUILD 

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
download jdk \
  http://download.oracle.com/otn-pub/java/jdk/${JAVA_TM_VERSION}u${JAVA_RELEASE}-b${JAVA_BUILD}/jdk-${JAVA_TM_VERSION}u${JAVA_RELEASE}-linux-x64.tar.gz \
  jdk-${JAVA_TM_VERSION}u${JAVA_RELEASE}-linux-x64.tar.gz \
  "Cookie: oraclelicense=accept-securebackup-cookie"
popd

echo ----------------------------------------------------
echo Build the RPM
echo ----------------------------------------------------
rpmbuild --target=x86_64 \
  --define="_topdir $PWD" \
  --define="_tmppath $PWD/TEMP" \
  --define="JAVA_VERSION $JAVA_VERSION" \
  --define="JAVA_RELEASE $JAVA_RELEASE" \
  --define="JAVA_TM_VERSION $JAVA_TM_VERSION" \
  --define="JAVA_BUILD $JAVA_BUILD" \
  -bb SPECS/package.spec
echo ----------------------------------------------------
echo
