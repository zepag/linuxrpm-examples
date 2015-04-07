#!/bin/sh

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
echo Build the RPM
echo ----------------------------------------------------
rpmbuild --target=noarch \
  --define="_topdir $PWD" \
  --define="_tmppath $PWD/TEMP" \
  -bb SPECS/package.spec
echo ----------------------------------------------------
echo

if [ -f /usr/bin/yum ]; then
  yum -q -y install expect
elif [ -f /usr/bin/zypper ]; then
  zypper -q --non-interactive install expect
else
  echo "Unable to determine package manager"
  exit 2
fi

. ./sign.sh 
