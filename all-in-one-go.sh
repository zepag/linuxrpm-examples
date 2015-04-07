#!/bin/bash
for os in centos6 centos7 opensuse13.2 fedora21
do
    sh ./build-in.sh $os example1 example2 example3 example4 example5 example6 example7
done
