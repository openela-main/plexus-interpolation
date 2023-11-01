%bcond_with bootstrap

Name:           plexus-interpolation
Version:        1.26
Release:        12%{?dist}
Summary:        Plexus Interpolation API
# Most of the code is ASL 2.0, a few source files are ASL 1.1 and some tests are MIT
License:        ASL 2.0 and ASL 1.1 and MIT
URL:            https://github.com/codehaus-plexus/plexus-interpolation
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-interpolation/archive/plexus-interpolation-%{version}.tar.gz

Patch0:         0001-Use-PATH-env-variable-instead-of-JAVA_HOME.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap-openjdk8
%else
BuildRequires:  maven-local-openjdk8
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%{?javadoc_package}

%prep
%setup -q -n plexus-interpolation-plexus-interpolation-%{version}
%patch0 -p1
%pom_add_dep junit:junit:4.13.1:test
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-publish-plugin

%build
%mvn_file : plexus/interpolation
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 29 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.26-11
- Add missing test dependency on JUnit 4

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.26-10
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.26-7
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.26-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.26-3
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.26-2
- Mass rebuild for javapackages-tools 201902

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Marian Koncek <mkoncek@redhat.com> - 1.26-1
- Update to upstream version 1.26

* Wed Jul 03 2019 Filipe Rosset <rosset.filipe@gmail.com> - 1.26-1
- Update to version 1.26, fixes rhbz#1724390

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.25-1
- Update to version 1.25.

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-10
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-6
- Remove BR on maven-release-plugin

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-3
- Cleanup spec file

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-2
- Update upstream URL

* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.22-1
- Update to upstream version 1.22

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.21-1
- Update to upstream version 1.21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.15-8
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.15-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.15-4
- Build with xmvn

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.15-3
- Fix source URL to be stable

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 1.15-1
- Update to latest upstream.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.14-2
- Use add_maven_depmap macro
- Use more precise specification of files

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 1.14-2
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 1.14-1
- Update to upstream 1.14 version.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.13-2
- Fix review comments.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1.13-1
- Initial package.
