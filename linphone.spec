# TODO: 
#  - split main package to few smaller (there is linphonec for console,
#    auto-answering machine and linphone applet for gnome)
#  - check why --enable-alsa doesn't require alsa-lib-devel
#  - check if all this configure option I've set are really needed

Summary:	Linphone Internet Phone
Summary(pl):	Linphone - telefon internetowy
Name:		linphone
Version:	0.11.0
Release:	2.2
License:	LGPL/GPL
Group:		Applications/Communications
Source0:	http://simon.morlat.free.fr/download/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	d44393ea9cfbd276c0cf0415849c9cc6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
Patch2:		%{name}-system-libs.patch
URL:		http://www.linphone.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.5
BuildRequires:	gnome-panel-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libgsm-devel >= 1.0.10
BuildRequires:	libosip-devel >= 0.9.7
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	lpc10-devel >= 1.5
BuildRequires:	scrollkeeper
BuildRequires:	speex-devel >= 1.0.0
BuildRequires:	xft-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
Linphone is a web phone: it let you phone to your friends anywhere in
the whole world, freely, simply by using the internet. The cost of the
phone call is the cost that you spend connected to the internet.

Here are the main features of linphone:
    - Works with the Gnome Desktop under linux.
    - Works as simply as a cellular phone. Two buttons, no more.
    - Understands the SIP protocol.
    - You just require a soundcard to use linphone.
    - Linphone is free software, released under the General Public
      Licence.
    - Linphone is documented: there is a complete user manual readable
      from the application that explains you all you need to know.

%description -l pl
Linphone to telefon internetowy - pozwala dzwoni� do znajomych na
ca�ym �wiecie bez dodatkowych op�at, u�ywaj�c tylko Internetu.

G��wne cechy linphone:
 - dzia�anie ze �rodowiskiem GNOME
 - na�ladowanie prostego telefonu kom�rkowego - tylko dwa przyciski
 - obs�uga protoko�u SIP
 - wymaga karty d�wi�kowej
 - jest wolnodost�pnym oprogramowaniem (na licencji GPL)
 - ma dokumentacj�: pe�ny podr�cznik dost�pny z aplikacji.

%package devel
Summary:	Linphone Internet Phone - header files
Summary(pl):	Telefon internetowy Linphone - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtk-doc-common

%description devel
Development files for the Linphone Internet Phone.

%description devel -l pl
Pliki dla programist�w u�ywaj�cych telefonu internetowego Linphone.

%package static
Summary:	Linphone static libraries
Summary(pl):	Statyczne biblioteki Linphone
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of Linphone libraries.

%description static -l pl
Statyczne wersje bibliotek Linphone.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
# gettext 0.11.5 used
#%%{__gettextize}
%{__libtoolize}
%{__aclocal} -I /usr/share/aclocal/gnome2-macros
%{__autoconf}
%{__automake}
cd oRTP
	%{__libtoolize} 
	%{__aclocal}
	%{__autoconf}
	# don't use -f here
	automake -a -c --foreign
cd ..
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-platform-gnome-2 \
	--enable-alsa \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications \
	$RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

install share/linphone.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install share/linphone.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers
install pixmaps/*.png pixmaps/*.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
/sbin/ldconfig

%postun
/usr/bin/scrollkeeper-update
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%config(noreplace) %{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Network/Communications/*
%{_pixmapsdir}/*
%{_datadir}/sounds/*
%{_datadir}/linphonec
%{_mandir}/man*/*
%{_libdir}/bonobo/servers/GNOME_LinphoneApplet.server
%attr(755,root,root) %{_libdir}/linphone_applet
%{_datadir}/gnome-2.0/ui/GNOME_LinphoneApplet.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/ortp
%{_includedir}/osipua
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
