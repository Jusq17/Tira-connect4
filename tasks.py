from invoke import task

@task
def start(ctx):
    ctx.run("python src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests/logictests.py src/tests/performance-tests.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests/logictests.py src/tests/performance-tests.py", pty=True)

@task(coverage)
def coveragereport(ctx):
    ctx.run("coverage html", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
