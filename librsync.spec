%define	major 1
%define libname	%mklibname rsync %{major}
%define develname %mklibname -d rsync

Summary:	Rsync libraries
Name:		librsync
Version:	0.9.7
Release:	9
License:	LGPL
Group:		System/Libraries
URL:		http://librsync.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		librsync-0.9.7-fix-str-fmt.patch
Patch1:		librsync-0.9.7-lfs_overflow.patch
Patch2:		librsync-0.9.7-getopt.patch
Patch3:		librsync-0.9.7-man_pages.patch
BuildRequires:	bzip2-devel
BuildRequires:	autoconf automake libtool
BuildRequires:	popt-devel

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
Group:         	System/Libraries

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
Obsoletes:	%{_lib}rsync1-devel < 0.9.7-6

%description -n		%{develname}
This package contains header files necessary for developing
programs based on librsync.

%package -n	rdiff
Summary:	Compute and apply signature-based file differences
Group:          System/Servers
Requires:	%{libname} = %{version}

%description -n	rdiff
Compute and apply signature-based file differences.

%prep

%setup -q
%patch0 -p0
%patch1 -p1 -b .lfs_overflow
%patch2 -p1 -b .getopt
%patch3 -p1 -b .man_pages


%build
libtoolize --copy --force
autoreconf -fi

%configure2_5x \
    --enable-shared \
    --disable-static

%make

%install

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS NEWS README THANKS
%attr(0755,root,root) %{_libdir}/librsync.so.%{major}*

%files -n %{develname}
%doc TODO
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*

%files -n rdiff
%attr(0755,root,root) %{_bindir}/rdiff
%{_mandir}/man1/rdiff.1*
