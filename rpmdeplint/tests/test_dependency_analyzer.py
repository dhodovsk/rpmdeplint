from unittest import TestCase
from rpmdeplint import DependencyAnalyzer
from . import base
import os

class TestDependencyAnalyzer(TestCase):
    def test_repos(self):
        repo_path = os.path.join(os.path.dirname(__file__), 'repos')
        sack = base.TestSack(repo_dir=repo_path)
        sack.load_test_repo("base1", "base_1.repo")
        sack.load_test_repo("test", "test.repo")
        da = DependencyAnalyzer(sack)

        pkgs = da.list_latest_packages()
        self.assertEqual(6, len(pkgs))

        want_cinnamon = da.find_packages_that_require('cinnamon')
        self.assertEqual(1, len(want_cinnamon))
        apple_pie = want_cinnamon[0]
        self.assertEqual('apple-pie-1.9-1.x86_64', str(apple_pie))

        ok, result = da.try_to_install(apple_pie)
        self.assertEqual(True, ok)
        self.assertEqual(5, len(result['installs']))

        ok, result = da.try_to_install(*pkgs)
        self.assertEqual(False, ok)
        self.assertEqual(1, len(result['problems']))
        self.assertEqual('nothing provides egg-whites needed by lemmon-meringue-pie-1-0.x86_64', result['problems'][0])

        sack.load_test_repo("base2", "base_2.repo")
        ok, result = da.try_to_install(*pkgs)
        self.assertEqual(True, ok)
        self.assertEqual(8, len(result['installs']))
