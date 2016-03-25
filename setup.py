from setuptools import setup

setup(
    name='blog',
    packages=[
        'blog',
        'blog.core',
    ],
    install_requires=[
        'django',
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
