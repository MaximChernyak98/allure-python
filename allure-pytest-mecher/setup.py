import os,sys
from setuptools import setup
from pkg_resources import require, DistributionNotFound, VersionConflict

try:
    require('pytest-allure-adaptor')
    print("""
    You have pytest-allure-adaptor installed.
    You need to remove pytest-allure-adaptor from your site-packages
    before installing allure-pytest, or conflicts may result.
    """)
    sys.exit()
except (DistributionNotFound, VersionConflict):
    pass

PACKAGE = "allure-pytest-mecher"

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Pytest',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
]

setup_requires = [
    "setuptools_scm"
]


install_requires = [
    "pytest>=4.5.0"
]


def prepare_version():
    from setuptools_scm import get_version
    configuration = {"root": "..",  "relative_to": __file__}
    version = get_version(**configuration)
    install_requires.append(f"allure-python-commons=={version}")
    return configuration


def get_readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    setup(
        name=PACKAGE,
        use_scm_version=prepare_version,
        description="Allure pytest integration",
        url="https://github.com/allure-framework/allure-python",
        author="QAMetaSoftware, Stanislav Seliverstov",
        author_email="sseliverstov@qameta.io",
        license="MIT",
        classifiers=classifiers,
        keywords="allure reporting pytest",
        long_description=get_readme('README.rst'),
        packages=["allure_pytest"],
        package_dir={"allure_pytest": "src"},
        entry_points={"pytest11": ["allure_pytest = allure_pytest.plugin"]},
        setup_requires=setup_requires,
        install_requires=install_requires
    )

if __name__ == '__main__':
    main()

