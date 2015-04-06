#!/bin/bash
for dir in BUILD BUILDROOT RPMS SRPMS TEMP
do
 [[ -d $dir ]] && rm -Rf $dir && echo "Removed dir $dir"
done
