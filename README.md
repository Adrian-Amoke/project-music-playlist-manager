# Music Playlist Manager 

## Project Overview

This project is a Command Line Interface (CLI) application for managing music playlists. It allows users to create, view, and manage playlists, songs, and reviews through an interactive terminal interface. The project is built in Python and follows a modular structure to separate concerns such as user interface, data models, and helper functions.

## Features

- Create, view, update, and delete multiple playlists.
- Add, view, update, and delete songs within playlists.
- Create, view, update, and delete reviews for playlists and songs.
- Use playlist names instead of IDs when associating songs or reviews.
- View data in neatly formatted tables with headers and aligned columns.
- Detailed view to list all songs in a selected playlist.
- Interactive terminal interface for easy navigation.
- Modular codebase for easy maintenance and extension.
- Debugging utilities to assist in development.

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

Follow the on-screen prompts to interact with the application. You can create playlists, add songs, write reviews, and perform other playlist management tasks. The menus provide options to view data in tables and detailed views.

## File Structure

- `lib/cli.py`: Main CLI script that handles user interaction and menu navigation.
- `lib/helpers.py`: Helper functions used by the CLI for various operations.
- `lib/debug.py`: Debugging utilities.
- `lib/models/`: Directory containing data model classes for playlists, songs, and reviews.
- `main.py`: Entry point script that launches the CLI.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes with clear commit messages.
4. Submit a pull request describing your changes.
