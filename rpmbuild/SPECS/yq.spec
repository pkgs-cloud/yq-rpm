%define golang 1.11.8

%undefine _missing_build_ids_terminate_build

Summary: yq is a portable command-line YAML processor
Name: yq
Version: 2.3.0
Release: 1%{?dist}
License: MIT
Group: Applications/File
URL: https://github.com/mikefarah/yq
Source0: https://github.com/mikefarah/yq/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://dl.google.com/go/go%{golang}.linux-amd64.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Lightweight and portable command-line YAML processor.
The aim of the project is to be the jq or sed of yaml files.

%prep
%setup -c -n %{name}-%{version} -T -D

mkdir -p src/yq
tar xzf %{SOURCE0} --strip 1 -C src/yq
tar xzf %{SOURCE1}

%build
export GOROOT=$(pwd)/go
export GOPATH=$(pwd)
export PATH=$GOROOT/bin:$GOPATH/bin:$PATH

cd src/yq
scripts/devtools.sh

govendor sync -v

CGO_ENABLED=0 go install ./...

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/yq %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%license src/yq/LICENSE
%defattr(-,root,root,-)
%{_bindir}/yq

%changelog
* Wed Apr 10 2019 pkgs.cloud - 2.3.0-1
- First RPM build
