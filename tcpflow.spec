# Note that this is NOT a relocatable package
%define ver      1.4.5
%define rel      1
%define prefix   /usr

Summary: Network traffic recorder
Name: tcpflow
Version: %ver
Release: %rel
Copyright: GPLv3
Group: Console/Networking
Source: http://afflib.org/downloads/tcpflow-1.4.5.tar.gz
BuildRoot: /var/tmp/tcpflow-root
Prefix: %prefix
URL: http://afflib.org/tcpflow/

%description
tcpflow is a program that captures data transmitted as part of TCP connections (flows), and stores the data in a way that is convenient for protocol analysis or debugging. A program like 'tcpdump' shows a summary of packets seen on the wire, but usually doesn't store the data that's actually being transmitted. In contrast, tcpflow reconstructs the actual data streams and stores each flow in a separate file for later analysis.

%changelog

* 2012-02-26 Simson Garfinkel <simsong@acm.org> - Rewrite for version 1.2
* 1999-04-22 Ross Golder <rossigee@bigfoot.com> -  Wrote for version 0.12

%prep
%setup

%build
# Needed for snapshot releases.
%ifarch alpha
  MYARCH_FLAGS="--host=alpha-redhat-linux"
%endif
MYCFLAGS="$RPM_OPT_FLAGS"

#if [ ! -f configure ]; then
#  CFLAGS="$MYCFLAGS" ./autogen.sh $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --with-pcap=/usr/include/pcap
#else
#  CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib --with-pcap=/usr/include/pcap
#fi

CFLAGS="$MYCFLAGS" ./configure $MYARCH_FLAGS --prefix=%prefix --localstatedir=/var/lib 

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/man/man*/*

