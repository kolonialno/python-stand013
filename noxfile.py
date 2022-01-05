"""Nox sessions."""

import nox

locations = ["src", "tests", "noxfile.py"]


@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def tests(session):
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def flake8(session):
    """Lint using flake8."""
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("flake8", *args)


@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def mypy(session):
    """Type-check using mypy."""
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("mypy", *args)
