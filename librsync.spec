%define major 2
%define libname %mklibname rsync %{major}
%define develname %mklibname -d rsync

Summary:	Rsync libraries
Name:		librsync
Version:	2.3.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://librsync.sourceforge.net/
Source0:	https://github.com/librsync/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(popt)
BuildRequires:	cmake
BuildRequires:	doxygen

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files. librsync computes a delta relative
to a file's checksum, so the two files need not both be present to
generate a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient
than and incompatible with rsync 2.4.6.

%package -n	%{libname}
Summary:	Rsync libraries
Group:		System/Libraries

%description -n	%{libname}
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files. librsync computes a delta relative
to a file's checksum, so the two files need not both be present to
generate a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient
than and incompatible with rsync 2.4.6.

%package -n	%{develname}
Summary:	Headers for librsync
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	librsync-devel = %{version}-%{release}

%description -n	%{develname}
This package contains header files necessary for developing
programs based on librsync.

%package -n	rdiff
Summary:	Compute and apply signature-based file differences
Group:		System/Servers
Requires:	%{libname} = %{version}

%description -n	rdiff
Compute and apply signature-based file differences.

%prep
%setup -q
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%doc AUTHORS CONTRIBUTING.md NEWS.md README.md
%{_libdir}/librsync.so.%{major}{,.*}

%files -n %{develname}
%{_libdir}/%{name}.so
%{_includedir}/%{name}*
%{_mandir}/man3/*

%files -n rdiff
%{_bindir}/rdiff
%{_mandir}/man1/rdiff.1*
