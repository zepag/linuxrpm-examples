#!/bin/bash
rpmfiles=`find . -name *.rpm -type f -print`
echo ----------------------------------------------------
echo Signing the RPMs
echo ----------------------------------------------------
type expect >/dev/null 2>&1 || echo "'expect' needs to be available in the path. Impossible to sign your RPM without it";
chmod u+x autosign.exp
if test -z "$rpmfiles"; then
  echo "Error: no rpm file found";
  exit 1;
fi
for rpmfile in $rpmfiles
do
  echo Signing file $rpmfile
  ./autosign.exp 'Devoxx-Lab-RPM <devoxx-lab@example.com>' passphrase.gpg $rpmfile
done
