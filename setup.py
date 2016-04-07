
try:
    from setuptools import setup
    extra = dict(test_suite="tests.test.suite", include_package_data=True, test_requires=[])
except ImportError:
    from distutils.core import setup
    extra = {}


packages=[
    "ebu_tt_live"
]


setup(
    name="ebu-tt-live",
    version="0.0.1",
    description="EBU-TT Part 3 library implementing Specification EBU-3370",
    install_requires=[
        "PyXB"
    ],
    license="MIT",
    packages=packages,
    entry_points={
        'console_scripts': [
            'ebu-dummy-encoder = ebu_tt_live.scripts.ebu_dummy_encoder:main',
            'ebu-interactive-shell = ebu_tt_live.scripts.ebu_interactive_shell:main'
        ]
    }
)