# arca
A pattern language for music

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

To install dependencies and set up the virtual environment:

```bash
uv sync
```

## Usage

You can run Arca programs using the `arca` script:

```bash
uv run arca <program_file.txt> [output_file.musicxml]
```

Example:

```bash
uv run arca tutorial1a.txt output.musicxml
```

The programs are expected to be located in the `Arca Programs/` directory.
