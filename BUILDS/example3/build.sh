#!/bin/sh

echo ----------------------------------------------------
echo RPM package build script
echo ----------------------------------------------------
echo Jenkins environment:
echo '  'SVN_REVISION: $SVN_REVISION
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
mkdir -p /BINARIES/jdk8/
if [ -f "/BINARIES/jdk8/jdk-8u40-linux-x64.tar.gz" ]; then
  cp /BINARIES/jdk8/jdk-8u40-linux-x64.tar.gz .
else
  BASE_URL=http://download.oracle.com/otn-pub/java/jdk/8u40-b26/jdk-8u40
  wget --no-check-certificate --no-cookies - --header "Cookie: oraclelicense=accept-securebackup-cookie" "${BASE_URL}-linux-x64.tar.gz" -O /BINARIES/jdk8/jdk-8u40-linux-x64.tar.gz 
  cp /BINARIES/jdk8/jdk-8u40-linux-x64.tar.gz .
fi
popd

echo ----------------------------------------------------
echo Build the RPM
echo ----------------------------------------------------
rpmbuild --target=noarch --define="_topdir $PWD" --define="_tmppath $PWD/TEMP"  -bb SPECS/package.spec
echo ----------------------------------------------------
echo

#. ./sign-deploy.sh $*
