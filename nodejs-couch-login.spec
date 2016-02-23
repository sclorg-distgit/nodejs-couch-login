%{?scl:%scl_package nodejs-couch-login}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-couch-login
Version:        0.1.18
Release:        4%{?dist}
Summary:        A module for doing logged-in requests to a couchdb server

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/isaacs/couch-login
Source0:        http://registry.npmjs.org/couch-login/-/couch-login-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A module for doing logged-in requests to a couchdb server.

%prep
%setup -q -n package

%nodejs_fixdep request

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/couch-login
cp -pr package.json couch-login.js %{buildroot}%{nodejs_sitelib}/couch-login

%nodejs_symlink_deps
%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/couch-login
%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.18-4
- rebuilt

* Tue Mar 04 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.18-3
- Add missing nodejs_symlink_deps macro

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.18-2
- replace provides and requires with macro


* Fri Sep 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.18-1
- update to upstream release 0.1.18
- add ExclusiveArch logic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.15-5
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.15-4
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.15-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.15-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.15-1
- initial package generated by npm2rpm
