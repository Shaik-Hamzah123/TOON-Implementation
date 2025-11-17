# TOON Implementation

This repository contains a minimal implementation and experimentation
setup for **TOON (Token-Oriented Object Notation)** using the official
Python library:\
➡️ https://github.com/toon-format/toon-python/

TOON is a compact, human-readable serialization format optimized for
**LLM prompts**.\
It represents JSON data in a shorter, more token-efficient form while
keeping the structure explicit and easy for models to parse.

------------------------------------------------------------------------

## 📦 What is TOON?

**Token-Oriented Object Notation (TOON)** is a lightweight
representation of JSON designed specifically for Large Language Models.

-   Uses **indentation** (like YAML) for nested objects\
-   Uses **CSV-style tables** for uniform arrays\
-   Preserves structure exactly --- it's a **lossless** JSON
    representation\
-   Often reduces token usage significantly\
-   Helps LLMs parse, validate, and reason about structured data

Think of TOON as a **translation layer**:

> **Use JSON in your code → Encode as TOON → Send to the LLM.**

This brings CSV-like compactness with JSON-like structural clarity.

------------------------------------------------------------------------

## 📁 Project Structure

    TOON-IMPLEMENTATION/
    │
    ├── src/
    │   ├── dummy_api.py
    │   ├── main.py
    │   ├── toon_encoder.py
    │   ├── .env
    │   └── .env.example
    │
    ├── toon_try/
    │   └── toon.ipynb
    │
    ├── requirements.txt
    ├── .gitignore
    └── venv/

------------------------------------------------------------------------

## 🔧 Installation

Clone the repository and install dependencies:

``` bash
git clone <your-repo-url>
cd TOON-Implementation
pip install -r requirements.txt
```

Your `requirements.txt` must include:

    git+https://github.com/toon-format/toon-python.git

------------------------------------------------------------------------

## 🚀 Quick Start (Using toon-format)

``` python
from toon_format import encode

data = {
    "students": [
        {"name": "Alice", "age": 21},
        {"name": "Bob", "age": 22}
    ]
}

toon_text = encode(data)
print(toon_text)
```

Example output:

    students[2]:
        name, age
        Alice, 21
        Bob, 22

------------------------------------------------------------------------

## 🧪 Files in This Repository

### `src/main.py`

Entry script for testing TOON encoding.

### `src/toon_encoder.py`

Utility module for preparing and encoding data into TOON (e.g., for API
requests or LLM prompts).

### `src/dummy_api.py`

Example of loading data, encoding to TOON, and integrating into a simple
API workflow.

### `toon_try/toon.ipynb`

Exploratory Jupyter Notebook to experiment with TOON encoding.

------------------------------------------------------------------------

## 📚 More About TOON

Full documentation and examples:\
➡️ https://github.com/toon-format/toon-python/

------------------------------------------------------------------------
