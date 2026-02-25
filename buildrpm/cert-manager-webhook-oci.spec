%global debug_package %{nil}
%global app_name            cert-manager-webhook-oci
%global _buildhost          build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           cert-manager-webhook-oci
Version:        1.1.0
Release:        3%{?dist}
Summary:        ACME webhook for Oracle Cloud Infrastructure

Group:          System/Management
License:        Apache-2.0
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang >= 1.20.12

%description
ACME webhook for Oracle Cloud Infrastructure, can be used when you want to use cert-manager with Oracle Cloud
Infrastructure as a DNS provider.

%prep
%setup -q

%build
make go-build-webhook

%install
install -m 755 -d %{buildroot}/%{app_name}
cp -ap out/acme_webhook/* %{buildroot}/%{app_name}

%files
%license LICENSE.txt THIRD_PARTY_LICENSES.txt SECURITY.md
/%{app_name}/

%changelog
* Wed Feb 11 2026 Murali Annamneni <murali.annamneni@oracle.com> - 1.1.0-3
- Update golang version to 1.25.7

* Wed Aug 28 2024 Padmanabha Bhat <padmanabha.bhat@oracle.com> 1.1.0-2
- Update release version

* Wed Aug 28 2024 Padmanabha Bhat <padmanabha.bhat@oracle.com> 1.1.0-1
- Initial change
