# openfoam-data-extractor
Python script to extract datas from OpenFOAM generated files

## Description
This script extracts searched datas from the OpenFOAM project
generated files e.g. gravity, centreOfMass etc. The datas will be
stored as a CSV file located at the directory of the script, named
like the command line search pattern. This file can be easily
imported to OpenOffice calc, Matlab or whatever. The script must be
placed in a OpenFOAM case folder.

## OpenFOAM
From Wikipedia:
"OpenFOAM (Open source Field Operation And Manipulation) is a C++ toolbox for the development of customized numerical solvers, and pre-/post-processing utilities for the solution of continuum mechanics problems, including computational fluid dynamics (CFD). The code is released as free and open source software under the GNU General Public License. It is maintained by The OpenFOAM Foundation, which is sponsored by the ESI Group, the owner of the trademark to the name OpenFOAM."

## Usage
python extract.py -s <searchpattern> (e.g. centreOfMass) -f <filename> (e.g. sixDoFRigidBodyMotionState) -v (verbose screen output)

## Copyright
Copyright (C) 2015 by Christian Handorf under GPLv3+

