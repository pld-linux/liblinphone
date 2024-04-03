# TODO:
# - -DENABLE_TUNNEL (BR: TunnelConfig.cmake >= 0.7.0) - proprietary?
#
# Conditional build:
%bcond_with	ldap		# OpenLDAP contacts provider (too old LDAP in PLD?)
%bcond_without	lime		# LIMEv2/X3DH encryption support
%bcond_without	static_libs	# static libraries

Summary:	Linphone Internet Phone libraries
Summary(pl.UTF-8):	Biblioteki telefonu internetowego Linphone
Name:		liblinphone
Version:	5.3.39
Release:	1
License:	AGPL v3+ or proprietary
Group:		Applications/Communications
#Source0Download: https://gitlab.linphone.org/BC/public/liblinphone/-/tags
Source0:	https://gitlab.linphone.org/BC/public/liblinphone/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	aadff2af0262c6e7bae35eb1525996f8
Patch0:		%{name}-wrappers.patch
Patch1:		%{name}-jsoncpp.patch
Patch4:		%{name}-zxing.patch
URL:		https://www.linphone.org/technical-corner/liblinphone
# base and tester components
BuildRequires:	bctoolbox-devel >= 5.3.0
BuildRequires:	belcard-devel >= 5.3.0
BuildRequires:	belle-sip-devel >= 5.3.0
BuildRequires:	belr-devel >= 5.3.0
%{?with_lime:BuildRequires:	bzrtp-devel >= 5.3.0}
BuildRequires:	cmake >= 3.22
# required not only for docs, but also C++ wrappers
BuildRequires:	doxygen
BuildRequires:	jsoncpp-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libsoci-devel >= 4.0
BuildRequires:	libsoci-sqlite3-devel >= 4.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxml2-devel >= 2.0
%{?with_lime:BuildRequires:	lime-devel >= 5.3.0}
BuildRequires:	mediastreamer-devel >= 5.3.0
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	ortp-devel >= 5.3.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
# to generate C++ wrappers
BuildRequires:	python3-pystache
BuildRequires:	python3-six
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel >= 3.7.0
BuildRequires:	udev-devel
BuildRequires:	xerces-c-devel
BuildRequires:	zxing-cpp-nu-devel >= 1.4.0
BuildRequires:	zlib-devel >= 1.2.3
Requires(post,postun):	/sbin/ldconfig
Requires:	bctoolbox >= 5.3.0
Requires:	belcard >= 5.3.0
Requires:	belle-sip >= 5.3.0
Requires:	belr >= 5.3.0
%{?with_lime:Requires:	bzrtp >= 5.3.0}
%{?with_lime:Requires:	lime >= 5.3.0}
Requires:	mediastreamer >= 5.3.0
Requires:	ortp >= 5.3.0
Requires:	sqlite3 >= 3.7.0
Requires:	zlib >= 1.2.3
Obsoletes:	linphone-libs < 4
Conflicts:	linphone < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liblinphone is a high-level SIP library integrating all calling and
instant messaging features into an unified easy-to-use API.

It is the cross-platform VoIP library on which the Linphone
application is based on, and that anyone can use to add audio and
video calls or instant messaging capabilities to an application.

%description -l pl.UTF-8
Liblinphone to wysokopoziomowa biblioteka SIP integrująca całą
funkcjonalność związaną z dzwonieniem i komunikacją tekstową w
ujednolicone, łatwe w użyciu API.

Jest to wieloplatformowa biblioteka VoIP, na której oparta jest
aplikacja Linphone; może jej używać każdy, kto chce dodać do
swojej aplikacji obsługę połączeń dźwiękowych lub wideo albo
komunikacji tekstowej.

%package devel
Summary:	Header files for Linphone library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Linphone
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bctoolbox-devel >= 5.3.0
Requires:	belle-sip-devel >= 5.3.0
Requires:	belr-devel >= 5.3.0
%{?with_lime:Requires:	bzrtp-devel >= 5.3.0}
Requires:	jsoncpp-devel
Requires:	libstdc++-devel >= 6:7
Requires:	libxml2-devel >= 2.0
%{?with_lime:Requires:	lime-devel >= 5.3.0}
Requires:	mediastreamer-devel >= 5.3.0
Requires:	ortp-devel >= 5.3.0
Requires:	sqlite3-devel >= 3.7.0
Requires:	zlib-devel >= 1.2.3
Obsoletes:	linphone-devel < 4

%description devel
Development files for the Linphone library.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki Linphone.

%package static
Summary:	Linphone static library
Summary(pl.UTF-8):	Statyczna biblioteka Linphone
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	linphone-static < 4

%description static
Static version of Linphone library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki Linphone.

%package apidocs
Summary:	API documentation for Linphone library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Linphone
Group:		Documentation
Obsoletes:	linphone-apidocs < 4
BuildArch:	noarch

%description apidocs
API documentation for Linphone library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Linphone.

%package c++
Summary:	C++ wrapper for Linphone library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki Linphone
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	linphone-c++ < 4

%description c++
C++ wrapper for Linphone library.

%description c++ -l pl.UTF-8
Interfejs C++ do biblioteki Linphone.

%package c++-devel
Summary:	Headers for liblinphone++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblinphone++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	linphone-c++-devel < 4

%description c++-devel
Headers for liblinphone++ library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblinphone++.

%package c++-static
Summary:	Static liblinphone++ library
Summary(pl.UTF-8):	Statyczna biblioteka liblinphone++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}
Obsoletes:	linphone-c++-static < 4

%description c++-static
Static liblinphone++ library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka liblinphone++.

%package c++-apidocs
Summary:	API documentation for Linphone C++ library
Summary(pl.UTF-8):	Dokumentacja API biblioteki C++ Linphone
Group:		Documentation
Obsoletes:	linphone-c++-apidocs < 4
BuildArch:	noarch

%description c++-apidocs
API documentation for Linphone C++ library.

%description c++-apidocs -l pl.UTF-8
Dokumentacja API biblioteki C++ Linphone.

%package -n linphonec
Summary:	Linphone Internet Phone console interface
Summary(pl.UTF-8):	Linphone - telefon internetowy, interfejs konsolowy
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n linphonec
Linphonec is the console version of originally GNOME Internet phone
Linphone.

%description -n linphonec -l pl.UTF-8
Linphonec to konsolowa wersja telefonu internetowego Linphone
pochodzącego z GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch4 -p1

%build
%if %{with static_libs}
%cmake -B builddir-static \
	-DBUILD_SHARED_LIBS=OFF \
	%{?with_ldap:-DENABLE_LDAP=ON} \
	%{!?with_lime:-DENABLE_LIME_X3DH=OFF} \
	-DENABLE_TOOLS=OFF \
	-DENABLE_UNIT_TESTS=OFF

%{__make} -C builddir-static
%endif

%cmake -B builddir \
	-DENABLE_CONSOLE_UI=ON \
	-DENABLE_DOC=ON \
	%{?with_ldap:-DENABLE_LDAP=ON} \
	%{!?with_lime:-DENABLE_LIME_X3DH=OFF} \
	-DENABLE_STRICT=OFF \
	-DENABLE_UNIT_TESTS=OFF

%{__make} -C builddir

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C builddir-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

# some tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/liblinphone-{lpc2xml-test,test-ecc,xml2lpc-test}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/linphone-daemon-pipetest

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/liblinphone-5.3.0

# omitted by cmake install
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,cs/man1}
cp -p share/C/{linphonec,linphonecsh}.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p share/cs/linphonec.1 $RPM_BUILD_ROOT%{_mandir}/cs/man1

# missing in 4+
[ ! -d $RPM_BUILD_ROOT%{_pkgconfigdir} ] || exit 1
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
cat >$RPM_BUILD_ROOT%{_pkgconfigdir}/linphone.pc <<'EOF'
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: liblinphone
Requires: mediastreamer ortp bctoolbox
Description: All in one linphone libs.
Version: %{version}
Libs: -L${libdir} -llinphone
Cflags: -I${includedir}
EOF

cat >$RPM_BUILD_ROOT%{_pkgconfigdir}/linphone++.pc <<'EOF'
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: liblinphone++
Requires.private: linphone bctoolbox belle-sip
Description: C++ wrapper for linphone libraries.
Version: %{version}
Libs: -L${libdir} -llinphone++
Cflags: -I${includedir}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md NEWS README.md
%attr(755,root,root) %{_bindir}/liblinphone-auto-answer
%attr(755,root,root) %{_bindir}/liblinphone-sendmsg
%attr(755,root,root) %{_bindir}/linphone-daemon
%attr(755,root,root) %{_libdir}/liblinphone.so.10
%{_datadir}/belr/grammars/cpim_grammar
%{_datadir}/belr/grammars/ics_grammar
%{_datadir}/belr/grammars/identity_grammar
%{_datadir}/linphone
%{_datadir}/sounds/linphone

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblinphone.so
%{_includedir}/linphone
%{_pkgconfigdir}/linphone.pc
%dir %{_datadir}/LibLinphone
%{_datadir}/LibLinphone/cmake

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblinphone.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc builddir/coreapi/help/doc/doxygen/c/{*.css,*.html,*.js,*.png}

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblinphone++.so.10

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblinphone++.so
%{_includedir}/linphone++
%{_pkgconfigdir}/linphone++.pc
%dir %{_datadir}/LinphoneCxx
%{_datadir}/LinphoneCxx/cmake

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/liblinphone++.a
%endif

%files c++-apidocs
%defattr(644,root,root,755)
%doc builddir/wrappers/cpp/cpp/{*.css,*.html,*.js,*.png}

%files -n linphonec
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/linphonec
%attr(755,root,root) %{_bindir}/linphonecsh
%{_mandir}/man1/linphonec.1*
%{_mandir}/man1/linphonecsh.1*
%lang(cs) %{_mandir}/cs/man1/linphonec.1*
