"""
test_cli
----------------------------------
Tests for `cli` module.
"""
import pytest
from click.testing import CliRunner

from swingify2 import cli

# pylint doesn't like pytest-fixtures
# pylint: disable=redefined-outer-name


@pytest.fixture()
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.cli, ['--verbose'])
    assert result.exit_code == 0
