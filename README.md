# 🔍 Boolean Information Retrieval System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

_A lightweight Boolean search engine implementation in pure Python_

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples)

</div>

---

## 📋 Overview

This project implements a **Boolean Information Retrieval Model** — one of the foundational models in search engine technology. It supports Boolean queries using `AND`, `OR`, and `NOT` operators to search through a collection of text documents.

## ✨ Features

| Feature                   | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| 📄 **Document Loading**   | Load documents from a simple text file (one document per line) |
| 🧹 **Stop Words Removal** | Automatically filters out common English stop words            |
| 📊 **Inverted Index**     | Builds an efficient inverted index for fast lookups            |
| 🔗 **Boolean Operators**  | Full support for `AND`, `OR`, `NOT` query operators            |
| 💬 **Interactive Mode**   | Built-in REPL for continuous searching                         |
| 🚀 **Zero Dependencies**  | Pure Python implementation — no external libraries required    |

## 📁 Project Structure

```
boolean-information-retrieval/
│
├── 📄 main.py            # Main application code
├── 📝 documents.txt      # Text documents collection
└── 📖 README.md          # Documentation
```

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/boolean-information-retrieval.git

# Navigate to the project directory
cd boolean-information-retrieval
```

> **Note:** No additional dependencies required! Just Python 3.6+

## 💻 Usage

### Step 1: Prepare Your Documents

Add your documents to `documents.txt`, with **one document per line**:

```text
Information retrieval is the activity of obtaining information.
Boolean model uses AND, OR, NOT operators for searching.
Python is a programming language good for text processing.
```

### Step 2: Run the Application

```bash
python main.py
```

### Step 3: Start Searching

Use the following query formats:

| Query Type | Syntax            | Description                                |
| ---------- | ----------------- | ------------------------------------------ |
| **Simple** | `term`            | Find documents containing the term         |
| **AND**    | `term1 AND term2` | Find documents containing **both** terms   |
| **OR**     | `term1 OR term2`  | Find documents containing **either** term  |
| **NOT**    | `NOT term`        | Find documents **not** containing the term |

## 📖 Examples

### Sample Queries & Results

```
🔍 Query: 'information AND retrieval'

✓ Found 3 documents:
--------------------------------------------------
  [Doc 1]: Information retrieval is the activity of obtaining information system resources.
  [Doc 4]: Information retrieval can be implemented using various models.
  [Doc 6]: Search engines use indexing to speed up information retrieval.
```

```
🔍 Query: 'python OR boolean'

✓ Found 3 documents:
--------------------------------------------------
  [Doc 2]: Boolean model uses AND, OR, NOT operators to combine search terms.
  [Doc 3]: Python is a programming language good for text processing.
  [Doc 5]: Boolean logic is essential in search engines.
```

```
🔍 Query: 'NOT search'

✓ Found 5 documents:
--------------------------------------------------
  [Doc 1]: Information retrieval is the activity of obtaining information system resources.
  [Doc 3]: Python is a programming language good for text processing.
  ...
```

## 🛑 Stop Words

The system automatically removes common English stop words during preprocessing:

| Category         | Examples                                |
| ---------------- | --------------------------------------- |
| **Articles**     | a, an, the                              |
| **Prepositions** | in, on, at, by, for, with, to, from     |
| **Pronouns**     | i, you, he, she, it, we, they           |
| **Auxiliaries**  | is, are, was, were, be, been, have, has |
| **Conjunctions** | and, or, but, if, then, because         |

## 🔧 How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Documents  │ ──► │ Preprocessor │ ──► │ Inverted Index  │
│   (.txt)    │     │ (tokenize +  │     │  term → {docs}  │
└─────────────┘     │ stop words)  │     └────────┬────────┘
                    └──────────────┘              │
                                                  ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Results   │ ◄── │   Boolean    │ ◄── │   User Query    │
│             │     │   Matching   │     │                 │
└─────────────┘     └──────────────┘     └─────────────────┘
```

## 📊 Inverted Index Example

For the sample documents, the inverted index looks like:

| Term          | Document IDs     |
| ------------- | ---------------- |
| `information` | {1, 4, 6}        |
| `retrieval`   | {1, 4, 6}        |
| `boolean`     | {2, 5}           |
| `python`      | {3}              |
| `search`      | {2, 5, 6, 8, 10} |

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for Information Retrieval enthusiasts**

⭐ Star this repo if you find it helpful!

</div>
