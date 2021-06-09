from setuptools import find_packages, setup

requirements = [
    "Django",
    "dj_database_url",
    "gunicorn",
    "python-dotenv",
    "whitenoise"
]

setup(
    name="https://github.com/michellesenar/french-verbs",
    version="0.2",
    description="Practice French Verbs conjugation",
    url="https://github.com/michellesenar/french-verbs",
    author="Michelle Senar Dressler",
    license="MIT",
    install_requires=requirements,
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "manage = manage:main"
        ],
    },
)
