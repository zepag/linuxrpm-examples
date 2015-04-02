### Howto use this

Building the example found in BUILDS/example1 in centos6.

```sh
$ sh build-in.sh centos6 example1
```

Building the example found in BUILDS/example1 in centos7.

```sh
$ sh build-in.sh centos7 example1
```

Examples:

1: a basic package adding a file in a known place and creating a link
2: a package with a dependency
3: a very basic custom JDK package
4: a package building something native
5: a package building multiple packages at in a single spec
6: a package with triggers pre-post-build to illustrate lifecycle issues
