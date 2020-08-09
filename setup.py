from setuptools import find_packages, setup

setup(
    name='blog',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"blog": [
        "static/*/*",
        "templates/*",
    ]},
    install_requires=[
        'arrow',
        'dj-database-url',
        'dj-static',

        # https://github.com/niwinz/django-jinja/issues/260
        'Django<3.1',

        'django-debug-toolbar',
        'django-jinja',
        'djangorestframework',
        'graphene',
        'graphene_django',
        'gunicorn',
        'jinja2',
        'markdown',
        'psycopg2cffi',
        'sentry-sdk',
        'Werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'blog = config.__main__:main',
        ]
    },
)
