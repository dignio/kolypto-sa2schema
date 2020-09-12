import nox.sessions


nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ['tests', 'tests_pydantic', 'tests_sqlalchemy']


@nox.session(python=['3.7', '3.8'])
def tests(session: nox.sessions.Session, sqlalchemy=None, pydantic=None):
    """ Run all tests """
    session.install('poetry')
    session.run('poetry', 'install')

    # Specific versions
    if sqlalchemy:
        session.install(f'sqlalchemy=={sqlalchemy}')
    if pydantic:
        session.install(f'pydantic[email]=={pydantic}')

    # Test
    session.run('pytest', 'tests/', '--cov=sa2schema')


@nox.session()
@nox.parametrize(
    'pydantic',
    [
        '1.5',
        '1.5.1',
        #'1.6', # has a bug
        '1.6.1',
    ]
)
def tests_pydantic(session, pydantic):
    tests(session, pydantic=pydantic)



@nox.session()
@nox.parametrize(
    'sqlalchemy',
    [
        *(f'1.3.{x}' for x in range(5, 1+18)),
    ]
)
def tests_sqlalchemy(session, sqlalchemy):
    tests(session, sqlalchemy=sqlalchemy)

