Name:           jetty-distribution-remote-resources
Version:        1.1
Release:        8%{?dist}
Summary:        Jetty toolchain artifact for distribution remote resources

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  jetty-toolchain


%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/LICENSE*
%dir %{_javadir}/%{name}

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-8
- Mass rebuild 2013-12-27

* Fri Aug 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-7
- Migrate away from mvn-rpmbuild (#997438)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-2
- Install license files as well

* Wed Dec 14 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-1
- Initial version of the package
