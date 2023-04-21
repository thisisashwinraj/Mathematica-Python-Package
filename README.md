![](https://github.com/thisisashwinraj/Mathematica-Python-Package/blob/main/assets/images/Mathematica_Banner_Dark.png#gh-dark-mode-only)
![](https://github.com/thisisashwinraj/Mathematica-Python-Package/blob/main/assets/images/Mathematica_Banner_Light.png#gh-light-mode-only)

Mathematica is a python package for performing advanced mathematical operations, distributions, and visualizations & is licensed under the [GNU General Public License v3.0](https://github.com/thisisashwinraj/Mathematica-Python-Package/blob/main/LICENSE). It includes modules for calculating mean, standard deviation and the probability distribution function of several statistical distributions. The latest stable release can be found [here](https://pypi.org/project/mathematica/).

The project was started in April 2021 by [Ashwin Raj](https://www.github.com/thisisashwinraj) as an academic project. The resources for this package, & the pull requests are maintained, and reviewed by a team of volunteers from [Workspace](https://github.com/workspacedevelopers). Learn more about mathematica [here](https://codeinplace.stanford.edu/2021/showcase/436)


# SubDirectories and Dependencies

### Dependencies
• Python (>= 3.9.0) - Learn more about the python programming from [here](https://www.python.org/), & download the latest version from [here](https://www.python.org/downloads/)
<br>
• NumPy (>=1.20.3) - Learn about the NumPy package [here](https://numpy.org/), & install the package following the guidelines from [here](https://numpy.org/install/)

Mathematica runs on all operating systems, is quick to install and is available for free use. No version of mathematica supports Python 2. Mathematica's plotting capabiliies requires [matplotlib](https://matplotlib.org/) (>= 2.1.1) and [seaborn](https://seaborn.pydata.org/) (>= 0.9.0) packages

### Files and Folders
The files & directories, that are used are of critical importance to the mathematica python package are as mentioned:
<br>
• [dist](https://github.com/thisisashwinraj/Mathematica-Python-Package/tree/main/dist): This directory contains the entire source distribution .tar file for the package that needs to be uploaded to PyPi
<br>
• [mathematica.egg-info](https://github.com/thisisashwinraj/Mathematica-Python-Package/tree/main/mathematica.egg-info): This sub-directory contains the entire package's metadata including a PKG-INGFO & sources
<br>
• [mathematica](https://github.com/thisisashwinraj/Mathematica-Python-Package/tree/main/mathematica): The directory contains the entire code for performing operations & visualizing statistical distributions

# Python Package Build Commands
To build mathematica python package, run the following command to create a tar.gz file (python distribution format):
```
python setup.py sdist
```
To upload the python package to the pypi repository run the following command in your command prompt/terminal:
```
python setup.py sdist bdist_wheel
```
Running this file creates the following sub-directories: dist, and elxsi.egg-info. Executable installer can also be created for installing the package in the Microsoft Windows environment. 
To create an executable installer, run the command:
```
python setup.py bdist_wininst
```
# User Installation and Source Code
Latest stable release of mathematica can be downloaded from the repo or simply installed from [PyPi](https://pypi.org/project/mathematica), using the code:
```
pip install mathematica
```
Once this package has succesfully installed, a large array of different statistical distributions can be imported from the package by specifying the name of the distribution (seprated by a ','), with first letter of each word typed in uppercase
<br>
Mathematica's development takes place on [GitHub](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package). Please submit bugs you may encounter to the issue tracker with a reproducible example demonstrating the problem, in accordance with the issue templates present in [~/.github](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/.github) folder.
    
    ├── LICENSE                   // Licensed under the 'GNU General Public License v3.0'
    ├── pyproject.toml
    ├── README.md                 // Contains the base level documentation of the gh-repo
    ├── requirements.txt
    ├── assets                    // Contains all visual graphics (images, videos & gifs)
    │   └── images/Video/gif 
    ├── example                   // Contains the user guide for working with mathematica
    │   └── notebook
    ├── setup.py                  // Packaged, & distributed using the disutils py module
    ├── mathematica/
    │   ├── distributions         // Code for various different statistical distributions
    │   └── __init__.py
    └── tests/                    // Files for performing several unit test (to be added)
    

# Contribution Guidelines
To start contributing to the project, clone the repository into your local system subdirectory using the below git code:
```
git clone https://github.com/thisisashwinraj/Mathematica-Python-Package.git
```
Before cloning the repository, make sure to navigate to the working subdirectory of your command line interface and ensure that no folder with same name exists. Other ways to clone the repository includes using a password protected SSH key, or by using Git CLI. The changes may additionally be performed by opening this repo, using [GitHub Desktop](https://desktop.github.com/)
```
gh repo clone thisisashwinraj/Mathematica-Python-Package
```
Before opening a Pull Request it is recommended to have a look at the full contributing page to make sure your code complies with all the pull request guidelines. Please ensure that you satisfy the [~/checklist](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/tree/main/Template%20Files/PULL_REQUEST_TEMPLATE) before submitting your PR.

Navigate to this sub-directory & check status of all files that were altered (red) by running the below code in GitBash:
```
git status
```
Stage all your files that are to be pushed into your pull request. This can be done in two ways - stage all or some files:
```
git add .            // adds every single file that shows up red when running git status
```
```
git add <filename>   // type in the particular file that you would like to add to the PR
```

Commit all the changes that you've made and describe in brief the changes that you have made, using the command:
```
git commit -m "<commit_message>"
```
Push all of your updated work into this GitHub repo in the form of a Pull Request by running the following command:
```
git push origin main
```
All Pull Requests are reviewed on a monthly rolling basis. Your understanding is appreciate during this review process.

# License and Project Status
The package, and other resources are distributed under the [GNU General Public License 3](https://github.com/thisisashwinraj/Elxsi-Mathematical-Python-Package/blob/main/LICENSE). This package is compatible with all operating systems. The latest stable version release of mathematica v1.0.1 & is available to be installed on any local system for general use through pip installer from [PyPi](https://pypi.org/project/elxsi/) (& other indexes) using requirement specifiers. Check out pip documentation v21.1.1 [here](https://pip.pypa.io/en/stable/) for any information regarding the installer. The changes are logged in the [changelog](https://github.com/thisisashwinraj/Mathematica-Python-Package/blob/main/CHANGELOG.md)
