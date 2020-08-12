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
        'Django',

        # Prerelease versions to support django 3.1
        # https://github.com/niwinz/django-jinja/issues/260
        'django-debug-toolbar>=3.0a2',
        'django-jinja @ git+https://github.com/enricobarzetti/django-jinja@29319e8214d3496f8319cfe14db8dbe9f0f66435',

        'djangorestframework',
        'graphene',
        'graphene_django',
        'gunicorn',
        'jinja2',
        'markdown',
        'psycopg2cffi',
        'sentry-sdk',
        'Werkzeug',
        'whitenoise',
    ],
    entry_points={
        'console_scripts': [
            'blog = config.__main__:main',
        ]
    },
)
