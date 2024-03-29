#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
Name     : compat-readline-soname5
Version  : 5.2
Release  : 10
URL      : https://ftp.gnu.org/gnu/readline/readline-5.2.tar.gz
Source0  : https://ftp.gnu.org/gnu/readline/readline-5.2.tar.gz
Source1  : https://ftp.gnu.org/gnu/readline/readline-5.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: compat-readline-soname5-lib = %{version}-%{release}
Requires: compat-readline-soname5-license = %{version}-%{release}
BuildRequires : ncurses-dev
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
Introduction
============
This is the Gnu Readline library, version 5.2.
The Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in.  Both
Emacs and vi editing modes are available.  The Readline library includes
additional functions to maintain a list of previously-entered command
lines, to recall and perhaps reedit those lines, and perform csh-like
history expansion on previous commands.

%package dev
Summary: dev components for the compat-readline-soname5 package.
Group: Development
Requires: compat-readline-soname5-lib = %{version}-%{release}
Provides: compat-readline-soname5-devel = %{version}-%{release}
Requires: compat-readline-soname5 = %{version}-%{release}

%description dev
dev components for the compat-readline-soname5 package.


%package lib
Summary: lib components for the compat-readline-soname5 package.
Group: Libraries
Requires: compat-readline-soname5-license = %{version}-%{release}

%description lib
lib components for the compat-readline-soname5 package.


%package license
Summary: license components for the compat-readline-soname5 package.
Group: Default

%description license
license components for the compat-readline-soname5 package.


%prep
%setup -q -n readline-5.2
cd %{_builddir}/readline-5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632275375
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --includedir=/usr/include/readline5/
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1632275375
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-readline-soname5
cp %{_builddir}/readline-5.2/COPYING %{buildroot}/usr/share/package-licenses/compat-readline-soname5/a2c02b708b37f47c7b9ebb49c18a3e26d3cb3e8b
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/man/man3/history.3
rm -f %{buildroot}/usr/share/man/man3/readline.3
rm -f %{buildroot}/usr/share/info/history.info
rm -f %{buildroot}/usr/share/info/readline.info
rm -f %{buildroot}/usr/share/info/rluserman.info
## install_append content
mv %{buildroot}/usr/lib64/libhistory.so %{buildroot}/usr/lib64/libhistory5.so
mv %{buildroot}/usr/lib64/libreadline.so %{buildroot}/usr/lib64/libreadline5.so
# Default perms are 555, but this causes `brp-strip` to fail: it requires write
# access to the files. With rpm < 4.17 on Clear Linux, the files were not
# processed; `brp-strip-shared` was responsible for processing these files, but
# that script was disabled.  With rpm 4.17, `brp-strip` handles processing of
# most ELF content (except debuginfo and kernel modules).
chmod 755 %{buildroot}/usr/lib64/libhistory.so.5.*
chmod 755 %{buildroot}/usr/lib64/libreadline.so.5.*
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/readline5/readline/chardefs.h
/usr/include/readline5/readline/history.h
/usr/include/readline5/readline/keymaps.h
/usr/include/readline5/readline/readline.h
/usr/include/readline5/readline/rlconf.h
/usr/include/readline5/readline/rlstdc.h
/usr/include/readline5/readline/rltypedefs.h
/usr/include/readline5/readline/tilde.h
/usr/lib64/libhistory5.so
/usr/lib64/libreadline5.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhistory.so.5
/usr/lib64/libhistory.so.5.2
/usr/lib64/libreadline.so.5
/usr/lib64/libreadline.so.5.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-readline-soname5/a2c02b708b37f47c7b9ebb49c18a3e26d3cb3e8b
