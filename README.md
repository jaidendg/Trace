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

- **Dynamic module loading** -  Add new modules without changing core code
- **Sync + Async** module support
- **Clean CLI** with command history and helpful output

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
from core.base import BaseModule

class ExampleModule(BaseModule):
    name = "example"
    description = "Example description"

    def run(self, target: str):
        return {"result": target}
```

### Module Requirements

| Field          | Required | Description |
|----------------|----------|-----------|
| `name`         | Yes      | Command name (lowercase) |
| `description`  | Yes      | Brief description of module |
| `run()`        | Yes      | Main function that receives the arguments |

## Roadmap

- More OSINT modules
- Output formatting
- Export results

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.