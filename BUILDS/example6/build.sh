#!/bin/sh
echo ----------------------------------------------------
echo Build-Specific variables
echo ----------------------------------------------------
PRODUCT_VERSION="1.16.3"
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
echo Downloading wget sources
echo ----------------------------------------------------
mkdir -p SOURCES
pushd SOURCES
mkdir -p /BINARIES/wget/
if [ -f "/BINARIES/wget/wget-${PRODUCT_VERSION}.tar.gz" ]; then
  cp /BINARIES/wget/wget-${PRODUCT_VERSION}.tar.gz .
else
  wget "http://ftp.gnu.org/gnu/wget/wget-${PRODUCT_VERSION}.tar.gz" -O /BINARIES/wget/wget-${PRODUCT_VERSION}.tar.gz
  cp /BINARIES/wget/wget-${PRODUCT_VERSION}.tar.gz .
fi
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
