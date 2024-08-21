%{!?registry: %global registry container-registry.oracle.com/olcne}
%global app_name               cert-manager-webhook-oci
%global app_version            0.1.0
%global oracle_release_version 1
%global _buildhost             build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}-container-image
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        ACME webhook for Oracle Cloud Infrastructure
License:        Apache-2.0
Group:          System/Management
Source:         %{name}-%{version}.tar.bz2

%description
ACME webhook for Oracle Cloud Infrastructure, can be used when you want to use cert-manager with Oracle Cloud
Infrastructure as a DNS provider.

%prep
%setup -q -n %{name}-%{version}

%build
%global rpm_name %{app_name}-%{version}-%{release}.%{_build_arch}
%global docker_tag %{registry}/%{app_name}:v%{version}

yum clean all
yumdownloader --destdir=${PWD}/rpms %{rpm_name}

docker build --pull \
    --build-arg https_proxy=${https_proxy} \
    -t %{docker_tag} -f ./olm/builds/Dockerfile .
docker save -o %{app_name}.tar %{docker_tag}

%install
ls -ltr %{app_name}.tar
%__install -D -m 644 %{app_name}.tar %{buildroot}/usr/local/share/olcne/%{app_name}.tar

%files
%license LICENSE.txt THIRD_PARTY_LICENSES.txt SECURITY.md
/usr/local/share/olcne/%{app_name}.tar

%changelog
* Wed Aug 14 2024 Padmanabha Bhat <padmanabha.bhat@oracle.com> 0.1.0-1
- Changes to build the component in OLCNE pipeline
