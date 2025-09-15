"""
Setup script for Français-Thaï Moderne
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="francais-thai-moderne",
    version="1.2.0",
    author="Français-Thaï Moderne Team",
    author_email="michael@germini.info",
    description="Application web moderne pour apprendre le français-thaï avec génération automatique d'audios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/michaelgermini/Specialized-Training-Program",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8>=3.9",
            "black>=21.0",
            "mypy>=0.900",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "francais-thai=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": [
            "templates/*.html",
            "static/*",
            "*.csv",
            "*.md",
        ],
    },
    keywords="education thai french language learning audio gtts flask",
    project_urls={
        "Bug Reports": "https://github.com/michaelgermini/Specialized-Training-Program/issues",
        "Source": "https://github.com/michaelgermini/Specialized-Training-Program",
        "Documentation": "https://github.com/michaelgermini/Specialized-Training-Program#readme",
    },
)
