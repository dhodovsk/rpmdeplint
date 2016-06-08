rpmdeplint
----------

.. program:: rpmdeplint check-sat

Synopsis
~~~~~~~~

| :program:`rpmdeplint check-sat` [:option:`--repo` NAME,PATH] [RPMPATH]
| :program:`rpmdeplint list-deps` [:option:`--repo` NAME,PATH] [RPMPATH] 

Description
~~~~~~~~~~~

The :program:`rpmdeplint` will test dependency satisfiability of given RPM
packages against given repositories.

Options
~~~~~~~

.. option:: --repo NAME,PATH

   You can provide multiple repos of each type. The NAME may be anything you
   choose. The path must either be a filesystem path or a URL. In either case,
   the path is expected to point at `repodata/repomd.xml`.

Arguments
~~~~~~~~~

.. option:: RPMPATH

   Path to an RPM package. This can be a relative or absolute filesystem path.

Commands
~~~~~~~~

check-sat
  Checks for unmet dependencies with the given RPMs against given repositories.
  Each unmet dependency is listed.

list-deps
  All dependencies will be listed for each given RPM.

Exit status
~~~~~~~~~~~

Zero if all dependencies are satisfiable. Non-zero if dependency errors are
encountered.

Examples
~~~~~~~~

Test if an RPM package has unsatisfied dependencies against a remote repository::

  rpmdeplint check-sat --repo beaker,https://beaker-project.org/yum/client/Fedora23/ my-package.rpm

    Problems with dependency set:
    nothing provides python(abi) = 2.7 needed by some-package-1.2.3.fc23.noarch
    nothing provides TurboGears >= 1.1.3 needed by other-package-33.2-1.fc23.noarch

List all dependencies for `my-package.rpm`::

  rpmdeplint list-deps --repo beaker,https://beaker-project.org/yum/client/Fedora23/ my-package.rpm

    my-package has 72 dependencies:
            basesystem-11-1.fc23.noarch
            bash-4.3.42-1.fc23.x86_64
            beaker-common-22.1-1.fc22.noarch
            ....

Bugs
~~~~

Bug reports can be submitted to https://bugzilla.redhat.com/.