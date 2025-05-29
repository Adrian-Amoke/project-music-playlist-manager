# Music Playlist Manager 

## Project Overview

This project is a Command Line Interface (CLI) application for managing music playlists. It allows users to create, view, and manage playlists and songs through an interactive terminal interface. The project is built in Python and follows a modular structure to separate concerns such as user interface, data models, and helper functions.

## Installation

This project uses Pipenv for dependency management. To set up the environment, run the following commands:

```bash
pipenv install
pipenv shell
```

## Usage

To start the CLI application, run:

```bash
python main.py
```

Follow the on-screen prompts to interact with the application. You can create playlists, add songs, and perform other playlist management tasks.

## File Structure

- `lib/cli.py`: Main CLI script that handles user interaction and menu navigation.
- `lib/helpers.py`: Helper functions used by the CLI for various operations.
- `lib/debug.py`: Debugging utilities.
- `lib/models/`: Directory containing data model classes for playlists and songs.
- `main.py`: Entry point or additional script related to the project.

## Contribution

Feel free to fork the repository and contribute by adding new features, fixing bugs, or improving documentation.
