from setuptools import find_packages, setup

setup(
    name='blog',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'arrow',
        'Django',
        'django-debug-toolbar',
        'django-jinja',
        'djangorestframework',
        'dj-database-url',
        'dj-static',
        'gunicorn',
        'jinja2',
        'markdown',
    ],
    entry_points={
        'console_scripts': [
            'blog = blog.__main__:main',
        ]
    },
)
