Name:		swing-layout
Summary:	Swing Layout Extensions
Version:	1.0.2
Release:	%mkrel 1
Group:		Development/Java
Source:		%{name}-%{version}-src.zip
URL:		https://swing-layout.dev.java.net/
License:	LGPL+
BuildArch:	noarch
BuildRequires:	java-devel >= 1.6.0, ant
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
%setup -q -c %{name}

%build
ant
cd dist
%{__mv} %{name}.jar %{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{name}.jar


%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir} %{buildroot}%{_javadocdir}
%{__cp} -a dist/%{name}.jar dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
%{__cp} -a dist/javadoc  %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%doc COPYING releaseNotes.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}

