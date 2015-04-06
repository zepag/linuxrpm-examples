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
2: a package with a dependency to the first one, and nothing else ;)
3: a very basic custom JDK package
4: a package building something native: unrar
5: a package building multiple packages in a single spec
6: another package building something native and adding man pages and a configuration page: wget
