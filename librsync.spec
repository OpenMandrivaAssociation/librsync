%define	major 1
%define libname	%mklibname rsync %{major}
%define develname %mklibname -d rsync

Summary:	Rsync libraries
Name:		librsync
Version:	0.9.7
Release:	10
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


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-9
+ Revision: 797026
- various fixes

* Tue Jun 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-8
+ Revision: 683052
- sync with librsync-0.9.7-16.fc15.src.rpm

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-7mdv2011.0
+ Revision: 620222
- the mass rebuild of 2010.0 packages

* Mon Jun 08 2009 Funda Wang <fwang@mandriva.org> 0.9.7-6mdv2010.0
+ Revision: 383836
- fix str fmt
- fix 4Gig problem:
  http://sourceforge.net/tracker/index.php?func=detail&aid=1439412&group_id=56125&atid=479441

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-5mdv2009.0
+ Revision: 250432
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.9.7-3mdv2008.1
+ Revision: 129040
- kill re-definition of %%buildroot on Pixel's request
- import librsync


* Thu Sep 01 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-3mdk
- fix #15498

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-2mdk
- rebuild

* Fri Dec 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.7-1mdk
- 0.9.7

* Sun Nov 02 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.9.6-1mdk
- initial cooker contrib, PLD import
