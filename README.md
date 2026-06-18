<div align="center">

# 🕵️‍♂️ Trace

**A lightweight Python OSINT framework for intelligence gathering.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/jaidendg/trace)](https://github.com/jaidendg/trace/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/jaidendg/trace)](https://github.com/jaidendg/trace/issues)

---

Trace helps you collect publicly available information through an intuitive command-line interface.

</div>

## Features

- **Dynamic module & command loading**
- **Sync + Async** module support
- **Clean CLI**

> ⚠️ **Early Development** -  This project is still in active development. Things may change.

## Preview

![Trace Preview](assets/example.png)

## Installation

```bash
git clone https://github.com/jaidendg/trace.git
cd trace
```

**Create virtual environment:**

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

Start the framework:

```bash
python trace.py
```

## Creating Modules

Creating new modules in Trace is **very simple**.

### 1. Create a new file

Go to `modules/` and create a new Python file (e.g. `example.py`).

### 2. Example Module

```python
from core.base import Module

class ExampleModule(Module):
    name = "example"
    description = "Example description"

    def run(self, arg: str):
        if ...:
            return {"result": ...}
        else:
            return {"error": ...}
```

### Module Requirements

| Field          | Required | Description |
|----------------|----------|-----------|
| `name`         | Yes      | Module name (lowercase) |
| `description`  | Yes      | Brief description of module |
| `run()`        | Yes      | Main function |

## Creating Commands

### 1. Create a new file

Go to `commands/` and create a new Python file (e.g. `example.py`).

### 2. Example Command

```python
from core.base import Command

class ExampleCommand(Command):
    name = "example"
    description = "Example description"
    aliases = []

    @Command.execute
    def run(self, arg: str):
        return
```

### Command requirements

| Field          | Required | Description |
|----------------|----------|-----------|
| `name`         | Yes      | Command name (lowercase) |
| `description`  | Yes      | Brief description of command |
| `aliases`      | No       | Aliases of the command
| `run()`        | Yes      | Main function |

## Roadmap

- More OSINT modules
- Output formatting
- Export results
- Command to reload the registry
- Guided input

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.