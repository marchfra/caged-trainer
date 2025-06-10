# CAGED Trainer

*Per una versione italiana delle istruzioni clicca [qui](https://github.com/marchfra/caged-trainer/blob/main/README_IT.md).*

Generate a chord and check if the user-provided list of modes are valid modes that the chord can harmonize.

## Table of Contents

- [Installation](#installation)
    - [Binary](#binary)
    - [Source code](#source-code)
- [Running the app](#running-the-app)
    - [Binary](#binary-1)
    - [Source code](#source-code-1)
- [Usage](#usage)

## Installation

### Binary

The compiled binary is only available for MacOS.

To download it, go to the [Releases page](https://github.com/marchfra/caged-trainer/releases) and click on **caged-trainer** (the one with a little cube on its left).

To be able to open the application, open Terminal (you can find Terminal in Applications > Utilities, or by writing "Terminal" in Spotlight) and type the following lines, pressing Enter after each one:

```shell
xattr -d com.apple.quarantine '/path/to/caged-trainer'
```

This command removes the "quarantine" attribute that macOS adds to files downloaded from the internet. Removing this attribute allows the application to run without macOS security warnings. **Use this command only for files you trust.**

```shell
chmod +x '/path/to/caged-trainer'
```

This command gives the file permission to be run as a program (makes it "executable"). Without this permission, trying to run the file will either do nothing or open it in a text editor, showing its raw contents instead of executing it. Use this command if you want to be able to run the file.

By default the ```/path/to/caged-trainer``` should be ```~/Downloads/caged-trainer```, but if you are unsure of the path to the application you can drag-and-drop the app file in the Terminal window instead of writing its path. This will automatically insert the correct path.

You might be asked to enter your password.

You can now move the application file wherever you want it, and even make multiple copies.

### Source code

You can obtain the compressed source code from the [Releases page](https://github.com/marchfra/caged-trainer/releases).

You will need a Python installation in order to run the application from the source code. If you don't have Python installed, you can download it from [python.org](https://python.org).

## Running the app

### Binary

To launch the app, just double click on it. A Terminal window will open; this is normal, as the application runs inside the Terminal.

### Source code

**Using `uv` (recommended)**: if you have `uv` installed, run the application with

```shell
uv run main.py
```

If you are not familiar with `uv`, you can learn more about it [here](https://github.com/astral-sh/uv), or simply use the `python3` command as shown below.

**Using python**: run the application with

```shell
python3 main.py
```

## Usage

Once the app is running, you will be shown a chord along with a chord shape.

You will then be shown a list of modes derived from the major scale. To select the modes that the chord can harmonize, enter their number(s) separated by a space. When you're done, press Enter. If you think there are no modes that the chord can harmonize, just press Enter.

Repeat the procedure for every set of modes that will appear until you see your results, then follow the instructions on screen to get a new exercise or quit the app.
