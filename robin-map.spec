%define devname %mklibname robin-map -d

Name: robin-map
Version: 1.3.0
Release: 1
Source0: https://github.com/Tessil/robin-map/archive/refs/tags/v%{version}.tar.gz
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing
URL: https://github.com/Tessil/robin-map
License: GPL
Group: System/Libraries
BuildSystem: cmake
BuildArch: noarch

%description
C++ implementation of a fast hash map and hash set using robin hood hashing

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_datadir}/cmake/*
