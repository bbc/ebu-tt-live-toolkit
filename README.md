[![Build Status](https://api.travis-ci.org/ebu/ebu-tt-live-toolkit.svg?branch=master)](https://travis-ci.org/ebu/ebu-tt-live-toolkit)
[![Coverage Status](https://coveralls.io/repos/github/ebu/ebu-tt-live-toolkit/badge.svg?branch=ebu_master)](https://coveralls.io/github/ebu/ebu-tt-live-toolkit?branch=ebu_master)

# ebu-tt-live-toolkit

This is the repository for the interoperability kit of [EBU-TT Live](https://tech.ebu.ch/publications/tech3370).

The kit is envisaged to contain a set of components for generating, testing and distributing subtitle documents in EBU-TT Part 3 format.

This is an open source project. Anyone is welcome to contribute to the development of the components. Please see the [wiki](https://github.com/ebu/ebu-tt-live-toolkit/wiki) for the list of required components, guidelines and release plan.

The project home page is at [http://ebu.github.io/ebu-tt-live-toolkit/](http://ebu.github.io/ebu-tt-live-toolkit/) and links to the pre-built documentation.

We have a Slack team called [ebu-tt-lit](https://ebu-tt-lit.slack.com) for day to day communications, questions etc. Please join up!

If you would like to contribute or join the Slack team, please contact <subtitling@ebu.ch> or <nigel.megitt@bbc.co.uk>

Preparing the build environment with poetry
==============================================

Make sure you have nodejs, Python 3.11 and poetry. 

To install the dependencies via poetry:
     
     poetry install

or
     make

To open a poetry shell (which you don't have to do, because you can prefix all commands with `poetry run`):

     poetry shell

Once you are in the correct virtual environment after running `poetry shell`, Your prompt should display something like below:

     (ebu-tt-live-py3.11) bash-3.2$

If your virtual environment doesn't have the correct python version then you can run the below command before running `poetry shell`:

     poetry env use python3.11

To Build the runtime system using make:

     make bindings ui

To Run tests:

     make bindings test

To Generate Documentation, follow the instructions to install graphviz, below, then run:

     make docs

To exit poetry shell:

     exit

After this you are supposed to be able to launch the command line tools this python package
provides i.e.:

    ebu-dummy-encoder

or if you are not in a poetry shell, 

    poetry run ebu-dummy-encoder

Windows users
=============

Windows is not the best friend of Makefiles. So there is a make.bat file for those who would like to develop using
Windows. Assuming Python 3+ and virtualenv is installed and are on the PATH. To build the project you will also need node.js. Please read the instructions for your system [here](https://nodejs.org/en/download/package-manager/). Then run :

    make

This will make sure a virtual environment is created and activated and installs all the tools into it.

After that the following command should work:

    ebu-dummy-encoder

The Schema definitions XSD
==========================

The schema definitions are to be found embedded in the Python library in the xsd1.1 subfolder.
The root schemadocument is called *ebutt_live.xsd*.

The Python library
==================

The library uses XSD schemas from the xsd1.1 subdirectory.
The bindings will keep the validation sane and PyXB makes sure that updates are working as
expected. Should the schema be modified a regeneration can be run and the bindings will respect
the changes.

Scripts
=======

There are several scripts that emulate different components (nodes) in the infrastructure. They can be executed individually or in combinations by running `ebu-run`. Assuming the Makefile worked, the package is installed in a virtual environment and the virtual environment is active, the components should be available by running the `ebu-run` script and passing a configuration file. There are several example configuration files in `examples/config`. For the complete list see of scripts see `docs/build/html/scripts_and_their_functions.html`.

Below is a list of some of the key components. .

The simple producer is the beginning of the data pipeline. It generates EBU-TT-Live documents in a timed manner. In the repository root there is a *test.html* file that can be used for manual testing of the producer in any websocket capable browser. To run it use `ebu-run`:

    `ebu-run --admin.conf ebu_tt_live/examples/config/simple_producer.json`

The simple consumer connects to the producer or later on in the pipeline, assuming there are more components inserted.

  `ebu-run --admin.conf ebu_tt_live/examples/config/simple_consumer.json`

The User Input producer is a web page with a user interface that allows you to send subtitle documents and view the output of a downstream node. For complete documentation see `docs/build/html/user_input_producer.html`.

To run a configuration of components, use a configuration file with multiple nodes defined. For example, this will create 3 nodes: a distributer that listens to the UIP and two consumers that subscribe to the distributer:

  `ebu-run --admin.conf ebu_tt_live/examples/config/user_input_producer_dist_consumers.json`   

Documentation
=============

**Go straight to the [pre-built documentation for the current master branch](http://ebu.github.io/ebu-tt-live-toolkit/html/index.html).**

The documentation framework uses the popular Sphinx documentation generating engine and autodoc plugins to give
developers the flexibility of writing Extra documentation interleaved with the autogenerated documentation created by
autodoc.

## Prerequisite: Graphviz

To display the images in the documentation, you need to have [Graphviz](http://www.graphviz.org/) installed and make sure the *dot* executable is on the PATH. For example, for users of [homebrew](http://brew.sh/):

    brew install graphviz

## Generating documentation

Documentation can be generated based on the sources in the docs/source directory. After having installed the packages in
requirements.txt (which is done automatically by the make command) documentation can be generated by one of the
following three ways:

 1 Calling setuptools

```Shell
poetry run python setup.py build_sphinx
```

or

```Shell
make docs
```

 2 Running make in the docs directory where separate makefiles and a make.bat file is giving a variety of options.

```Shell
cd docs
make html
```

 3 Calling the sphinx-build command line script that comes with sphinx. WARNING: Platform-dependent path-separators.

```Shell
sphinx-build -b html docs/source/ docs/build/html
```

## Previewing the documentation

After sphinx finished with a successful execution log the generated documentation should be accessible by opening the
docs/build/html/index.html in any web browser.

Tests
=====

The test framework is described in [CONTRIBUTING.md](CONTRIBUTING.md)

How to contribute
=================

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md)
