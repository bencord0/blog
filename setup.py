from setuptools import setup

setup(
    name='blog',
    packages=['blog'],
    install_requires=[
        'django',
        'dj-database-url',
        'dj-static',
        'gunicorn',
    ],
    entry_points={
        'console_scripts': [
            'blog = blog.__main__:main',
        ]
    },
)
