# ebu-tt-live-toolkit

This is the repository for the interoperability kit of [EBU-TT Live](https://tech.ebu.ch/publications/tech3370). 

The kit is envisaged to contain a set of components for generating, testing and distributing subtitle documents in EBU-TT Part 3 format.

This is an open source project. Anyone is welcome to contribute to the development of the components. Please see the [wiki](https://github.com/ebu/ebu-tt-live-toolkit/wiki) for the list of required components, guidelines and release plan. 

If you would like to contribute, please contact <subtitling@ebu.ch> or <nigel.megitt@bbc.co.uk>

Preparing the build environment
===============================

Make sure you have python 2.7+. Make sure you have python virtual environment capability.

If not you can install virtualenv systemwide from your operating system's package repository
or by pip:

    sudo pip install virtualenv

After that creating a virtual environment should be as simple as:

    virtualenv env

Let's activate it (source makes sure the current shell executes the script
and assumes the environment variables that the activation script sets):

    source ./env/bin/activate

After having created the python virtual environment and having activated it the package
can be built by typing make if you have GNU build tooling on your system.

    make


Alternatively:

    pip install -r requirements.txt
    pip install -r requirements-test.txt
    python setup.py develop

    pyxbgen -r --binding-root=./ebu_tt_live/bindings -m __init__ --schema-root=./ebu_tt_live/xsd1.1/ -u ebutt_live.xsd

After this you are supposed to be able to launch the command line tools this python package
provides i.e.:

    ebu-dummy-encoder
    
Windows users
=============

Windows is not the best friend of Makefiles. So there is a make.bat file for those who would like to develop using 
Windows. Assuming python 2.7 and virtualenv is installed and are on the PATH.

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

There are several scripts that emulate different components in the infrastructure. Assuming the Makefile worked,
the package is installed in a virtual environment and the virtual environment is active the following scripts should
be available directly from the command line.

The simple producer is the beginning of the data pipeline. It generates
EBU-TT-Live documents in a timed manner. In the repository root there is a *test.html* file that can be used for manual testing of the producer in any websocket capable browser.

    ebu-simple-producer

The simple consumer connects to the producer or later on in the pipeline, assumint there are more components inserted.

    ebu-simple-consumer

How to contribute
=================

Please refer to CONTRIBUTING.md
