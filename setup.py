from setuptools import setup, find_packages

setup(
    name='task-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task-cli=task_cli.cli:main',
        ],
    },
    author="jupelaz",
    description="A simple task manager CLI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/task-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
