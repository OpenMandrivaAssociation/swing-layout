Name:		swing-layout
Summary:	Swing Layout Extensions
Version:	1.0.3
Release:	0.0.8
Group:		Development/Java
Source:		%{name}-%{version}-src.zip
URL:		https://swing-layout.dev.java.net/
License:	LGPL+
BuildArch:	noarch
BuildRequires:	jpackage-utils >= 1.6
BuildRequires:	java-devel >= 1.6.0
BuildRequires:	ant
%description
Swing Layout Extensions goal is to make it easy to create professional
cross platform layouts with Swing. This project will consist of extensions
to Swing and possibly a new LayoutManager. The long term goal is to roll
these changes back into Swing proper.

%package javadoc
Summary:	Javadoc for %name
Group:		Development/Java
%description javadoc
Javadoc for %name

%prep
%setup -q

%build
%{ant}
cd dist
%{__mv} %{name}.jar %{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{name}.jar


%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir} %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a dist/%{name}.jar dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
cp -pr dist/javadoc/*  %{buildroot}%{_javadocdir}/%{name}-%{version}/

%files
%doc COPYING releaseNotes.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-0.0.2mdv2010.0
+ Revision: 434236
- rebuild

* Tue Mar 11 2008 Alexander Kurtakov <akurtakov@mandriva.org> 1.0.3-0.0.1mdv2008.1
+ Revision: 186206
- new version

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-1mdv2008.1
+ Revision: 168284
- fix no-buildroot-tag

* Fri Sep 14 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 85664
- Import swing-layout

