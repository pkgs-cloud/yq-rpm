### YQ RPM package build on CentOS 7 using Docker

[yq](https://github.com/mikefarah/yq) is a portable command-line YAML processor

1. Install Docker on your system. And clone repository.

2. Build docker image and run RPM build within a container

	```
	docker build -t yq-rpmbuild .
	
	docker run --rm -a stdout \
	  -v $(pwd)/rpmbuild/SPECS:/root/rpmbuild/SPECS \
	  -v $(pwd)/rpmbuild/RPMS:/root/rpmbuild/RPMS \
	  -v $(pwd)/rpmbuild/SOURCES:/root/rpmbuild/SOURCES \
	  -t -i yq-rpmbuild /build.sh
	```
	
3. Find RPM package under `rpmbuild/RPMS`

