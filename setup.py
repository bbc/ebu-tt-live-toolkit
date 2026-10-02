
from setuptools import setup

extra = {
    "include_package_data": True,
    # setup_requires=['pytest-runner']
}

packages =[
    "ebu_tt_live",
    "ebu_tt_live.bindings",
    "ebu_tt_live.clocks",
    "ebu_tt_live.scripts",
    "ebu_tt_live.twisted",
    "ebu_tt_live.node",
    "ebu_tt_live.documents",
    "ebu_tt_live.examples"
]

setup(
    name="ebu-tt-live",
    version="3.1.0",
    description="EBU-TT Part 3 library implementing Specification EBU-3370",
    install_requires=[
        "pyxb-x=1.2.6.3",
        "ipdb>=0.10.1,<0.10.3",  # This will eventually be removed from here
        "configobj=5.0.9",
        "pyyaml~=6.0.3",
        # "service_identity",
        "twisted~=26.4.0",
        "autobahn~=26.7.1",
        "nltk~=3.10.3",
        # "sortedcontainers",
        "configmanners @ git+https://github.com/twobraids/configmanners.git@bff28a98cb45dde1b75f52ba3a3ac572a96885eb",
    ],
    license="BSD3",
    packages=packages,
    package_data={
        'ebu_tt_live.examples': ['*.txt', '*.json']
    },
    entry_points={
        'console_scripts': [
            'ebu-dummy-encoder = ebu_tt_live.scripts.ebu_dummy_encoder:main',
            'ebu-interactive-shell = ebu_tt_live.scripts.ebu_interactive_shell:main',
            'ebu-simple-consumer = ebu_tt_live.scripts.ebu_simple_consumer:main',
            'ebu-simple-producer = ebu_tt_live.scripts.ebu_simple_producer:main',
            'ebu-user-input-consumer = ebu_tt_live.scripts.ebu_user_input_consumer:main',
            'ebu-user-input-forwarder = ebu_tt_live.scripts.ebu_user_input_forwarder:main',
            'ebu-ebuttd-encoder = ebu_tt_live.scripts.ebu_ebuttd_encoder:main',
            'ebu-run = ebu_tt_live.scripts.ebu_run:main'
        ]
    },
    **extra
)
