# CAGED Trainer

*Per una versione italiana delle istruzioni clicca [qui](https://github.com/marchfra/caged-trainer/blob/main/README_IT.md).*

Generate a chord and check if the user-provided list of modes are valid modes that the chord can harmonise.

## Table of Contents

- [Installation](#installation)
    - [macOS](#macos)
    - [Windows](#windows)
    - [Running from source (macOS / Linux / Windows)](#running-from-source-macos--linux--windows)
- [Usage](#usage)
    - [GUI version](#gui-version)
    - [CLI version](#cli-version)

## Installation

### macOS

1. Download the latest `CAGEDTrainer.dmg` installer from the [Releases](https://github.com/marchfra/caged-trainer/releases) page.
2. Open the `CAGEDTrainer.dmg` file and drag and drop the app to your `Applications` folder.
3. **Important**: since the app is not signed by an Apple-certified developer, macOS will block it on the first launch.
    To open it anyway:
    - Go to **System Settings** &rarr; **Privacy & Security**.
    - Scroll down to the message saying that the app was blocked.
    - Click **"Open Anyway"**, then confirm.

    After the first manual confirmation, macOS will allow the app to run normally.

### Windows

1. Download the latest `CAGED_Trainer_Setup.exe` from the [Releases](https://github.com/marchfra/caged-trainer/releases) page.
2. Double-click the `CAGED_Trainer_Setup.exe` file and follow the on-screen instructions to install the app.
3. Once installed, you'll find **CAGED Trainer** in your Start menu and possibly as a shortcut on your desktop, if you chose to create it during the installation process. You can uninstall the app normally from **Settings** &rarr; **Apps**.

#### If you see "Windows protected your PC"

Because the app is not digitally signed, Windows may show you a SmartScreen warning when trying to launch the installation:

1. Click **"More info"**
2. Click **"Run anyway"** to continue the installation.

This is a standard SmartScreen warning for new apps and doesn't indicate a real threat.

#### If Microsoft Defender blocks the app entirely

1. Open the **Start Menu** and search for **"Windows Security"**.
2. Go to **"Virus & Threat Protection"**.
3. Click on **"Protection History"**.
4. Find the alert related to the app (might say "Quarantined" or "Blocked").
5. Click on it and choose **"Allow on device"** or **"Restore"**.
6. Try launching the app again.

After the first confirmation, Windows will allow the app to run normally.

### Running from source (macOS / Linux / Windows)

If you're not using macOS or Windows, or prefer to run the app from source, follow these steps:

#### Prerequisites

- git
- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (optional but recommended)

#### Steps

1. Clone the repository:

    ```shell
    git clone https://github.com/marchfra/caged-trainer.git
    cd caged-trainer
    ```

2. Create and activate virtual environment (only if not using uv):

    ```shell
    python3 -m venv .venv
    source .venv/bin/activate  # on Windows: .venv\Scripts\activate
    pip install .
    ```

3. Run the app:

    ```shell
    uv run src/gui.py  # python3 src/gui.py
    ```

    or, to run the app in CLI mode,

    ```shell
    uv run src/main.py  # python3 src/main.py
    ```

## Usage

### GUI version

Once the app is running, you will be shown a chord along with a chord shape.

Below that, you'll find four sections, one for each scale. Inside each section there are checkboxes for each mode generated by that scale; click on the checkbox if you think that its mode can be harmonised by the displayed chord.

When you're done, press the "Check" button to get the correct answer and see how you did. To get a new question press the "New chord" button.

#### Keyboard shortcuts

| Shortcut                    | Action                   |
|-----------------------------|--------------------------|
| <kbd>Enter</kbd>            | Check your answers       |
| <kbd>N</kbd>                | New chord                |
| <kbd>1</kbd> - <kbd>4</kbd> | Focus scale 1-4          |
| <kbd>Tab</kbd>              | Move to next checkbox    |
| <kbd>Space</kbd>            | Toggle selected checkbox |

### CLI version

This is available only when running the source code directly.

Once the app is running, you will be shown a chord along with a chord shape.

You will then be shown a list of modes derived from the major scale. To select the modes that the chord can harmonise, enter their number(s) separated by a space. When you're done, press <kbd>Enter</kbd>. If you think there are no modes that the chord can harmonise, just press <kbd>Enter</kbd>.

Repeat the procedure for every set of modes that will appear until you see your results, then follow the instructions on screen to get a new exercise or quit the app.
