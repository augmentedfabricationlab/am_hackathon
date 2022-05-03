# Additive Manufacturing Hackathon

[![Github - License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/augmentedfabricationlab/computational_design_and_fabrication)
[![PyPI - Latest Release](https://travis-ci.org/augmentedfabricationlab/computational_design_and_fabrication.svg?branch=master)](https://github.com/augmentedfabricationlab/computational_design_and_fabrication)


### 1. Aims of the AM_Hackathon

* Developing understanding for additive manufacturing processes
* Hands-on experience with a design-to-production interface
* First delve into computational design

**am_hackathon** runs on Python 3

--------------
### 2. Requirements

* Rhino 6 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

#### Dependencies

* [COMPAS](https://compas-dev.github.io/)
* [COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)
* [AM Information Model](https://github.com/augmentedfabricationlab/am_information_model)
* [UR Fabrication Control](https://github.com/augmentedfabricationlab/ur_fabrication_control)
* [Extruder Control](https://github.com/augmentedfabricationlab/extruder_control)
* [Fabrication Control](https://github.com/augmentedfabricationlab/fabrication_control)

--------------
### 3. Installation

#### 3.1 Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge

#### Windows
    (base) conda create -n amh compas_fab=0.22.0 --yes
    (base) conda activate amh

#### Mac
    (base) conda create -n amh compas_fab=0.22.0 python.app --yes
    (base) conda activate amh
    

#### Verify Installation

    (amh) pip show compas_fab
####
    Name: compas-fab
    Version: 0.22.0
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

#### Install on Rhino

    (amh) python -m compas_rhino.install

NOTE: This installs default to Rhino 7.0, if you are using a different Rhino version add `-v 5.0` or `-v 6.0` after the above statement.

#### 3.2 Installing remaining dependencies

#### AM Information Model
    
    (amh) python -m pip install git+https://github.com/augmentedfabricationlab/am_information_model@master#egg=am_information_model
    (amh) python -m compas_rhino.install -p am_information_model

#### UR Fabrication Control
    
    (amh) python -m pip install git+https://github.com/augmentedfabricationlab/ur_fabrication_control@master#egg=ur_fabrication_control
    (amh) python -m compas_rhino.install -p ur_fabrication_control

#### Extruder Control
    
    (amh) python -m pip install git+https://github.com/augmentedfabricationlab/extruder_control@master#egg=extruder_control
    (amh) python -m compas_rhino.install -p extruder_control

#### Fabrication Control
    
    (amh) python -m pip install git+https://github.com/augmentedfabricationlab/fabrication_control@master#egg=fabrication_control
    (amh) python -m compas_rhino.install -p fabrication_control

#### AM Hackathon
    This installs your local copy of the am_hackathon in editable mode, applying updates to the local repository directly into the rhino environment!
    (amh) python -m pip install -e <your_path>/<your_repository_name>
    (amh) python -m compas_rhino.install -p computational_design_and_fabrication -v7.0

--------------
#### 4. Credits
This package was created by Gido Dielemans `@gidodielemans <https://github.com/gidodielemans>`_ at `@augmentedfabricationlab <https://github.com/augmentedfabricationlab>`_
