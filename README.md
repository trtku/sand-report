# sand-report
> my master thesis in 2022

## Requirements

Install the following tools:

- [Anaconda](https://www.anaconda.com/products/individual)
- [Visual Studio Code](https://code.visualstudio.com/)
    and extensions:
    - [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
    - [editorconfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [Github Desktop](https://desktop.github.com/)
- [Rhinoceros version 7](https://www.rhino3d.com/download)
    and its plugins:
    - [KUKA|PRC](https://www.robotsinarchitecture.org/kuka-prc)


## Getting Started

We use `conda` to make sure we have clean, isolated environment for dependencies.

1. Open `Anaconda prompt`...

1. If you use conda for the first time, run below in anaconda.
    ```
    conda config --add channels conda-forge
    ```

1. go to working directory
    ```
    cd PATH_TO_WORKING_DIRECTORY
    ```

1. clone this repository
    ```
    git clone https://github.com/trtku/sand-report.git
    ```

1. go to folder of this repository
    ```
    cd sand-report
    ```

1. create envinronment
    ```
    conda create -f environment.yml
    ```

1. activate the environment
    ```
    conda activate sand-report
    ```

1. install python to Rhinoceros
    ```
    python -m compas_rhino.uninstall -v 7.0
    python -m compas_rhino.install -v 7.0
    ```

1. Open Visual Studio Code (, Rhinoceros and Grasshopper if necessary)
    ```
    code .
    ```

1. In case of updating environment
    ```
    conda env update -f environment.yml
    ```

## Credit

This project is developed by Ko Tsuruta(<trtku0809@gmail.com>); as a part of his Master Thesis at Tokyo University of the Arts (TUA) supervised by Prof.Mitshiro Kanada and Takahiro Kai.

Special Thanks to the members of Structural Engineering Laboratory at TUA for fruitful discussion.