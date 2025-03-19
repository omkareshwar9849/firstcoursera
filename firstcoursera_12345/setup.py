from setuptools import setup, find_packages

setup(
    name="firstcoursera_12345",
    version="0.1.0",
    description="A simple Python project for Coursera",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add any project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'firstcoursera=src.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)