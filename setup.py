from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="sfpassman",
    version="0.0.0",
    description="Set random generated snowflake user passwords and store them in AWS Secrets Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "": ["py.typed"],
    },
    entry_points={"console_scripts": ["sfpassman = sfpassman.cli:main"]},
    install_requires=["snowflake-connector-python==2.7.0", "boto3==1.19.7"],
    extras_require={
        "dev": [
            "black==21.10b0",
            "isort==5.9.3",
            "flake8==4.0.1",
            "flake8-annotations==2.7.0",
            "flake8-colors==0.1.9",
            "pre-commit==2.15.0",
            "pytest==6.2.5",
        ]
    },
)
