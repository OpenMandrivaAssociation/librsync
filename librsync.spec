%define	major	1
%define libname	%mklibname rsync %{major}

Summary:	Rsync libraries
Name:		librsync
Version:	0.9.7
Release:	%mkrel 6
License:	LGPL
Group:		System/Libraries
URL:		http://librsync.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		librsync-0.9.7-4Gig.patch
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}-devel
Summary:	Headers for librsync
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	librsync-devel

%description -n		%{libname}-devel
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
%patch0 -p1

%build

%configure2_5x \
    --enable-shared \
    --enable-static

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(0755,root,root) %{_libdir}/librsync.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%doc TODO
%{_libdir}/librsync.a
%{_libdir}/librsync.la
%{_libdir}/librsync.so
%{_includedir}/*
%{_mandir}/man3/*

%files -n rdiff
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/rdiff
%{_mandir}/man1/rdiff.1*

