# 🔒 Caesar Cipher Tool (GUI-Based)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Track](https://img.shields.io/badge/Track-Cybersecurity-red.svg)](#)

A modern, interactive Graphical User Interface (GUI) application built in Python using the **Tkinter** library to perform text encryption and decryption using the classic **Caesar Cipher** algorithm. 

This project is completed as part of the **Prodigy InfoTech Cybersecurity Internship (Task 01)**.

---

## 📖 Table of Contents
* [Features](#features)
* [How the Caesar Cipher Works](#how-the-caesar-cipher-works)
* [Application Preview](#application-preview)
* [Installation & Setup](#installation--setup)
* [How to Run](#how-to-run)
* [Code Structure](#code-structure)
* [Developer](#developer)

---

## Features

* **Modern Dark-Themed GUI**: A beautiful, user-friendly interface using a sleek charcoal dark mode.
* **Bi-directional Cipher**: Easily toggle between **Encryption** (shifting forward) and **Decryption** (shifting backward).
* **Smart Text Handling**:
  * Preserves original letter case (uppercase stays uppercase, lowercase stays lowercase).
  * Ignores and preserves non-alphabetic characters (spaces, numbers, and symbols remain unaffected).
* **Smooth Alphabet Wrap-around**: Seamlessly wraps around the alphabet (for example, shifting 'Z' forward by 1 wraps it directly back to 'A').
* **User-friendly Utility Buttons**:
  * 📋 **Copy Result**: Instantly copies the output to your system clipboard.
  * 🧹 **Clear**: Resets all fields with a single click.
* **Automatic Window Focus**: The app automatically launches on top of other active windows for seamless workflow interaction.

---

## How the Caesar Cipher Works

The Caesar Cipher is a type of substitution cipher where each character in the message is replaced by another character some fixed number of positions down the alphabet.

* **Encryption**: Each letter is shifted forward down the alphabet by your chosen shift key. 
  * *Example with a shift of 3:* `A` becomes `D`, `B` becomes `E`, and `Z` wraps around to become `C`.
* **Decryption**: The exact opposite happens. Each letter is shifted backward down the alphabet by the same shift key value to recover the original message.

---

## Installation & Setup

Since this application uses Python's built-in libraries (`tkinter`), you **do not** need to install any external dependencies!

### Prerequisites
Make sure you have Python 3 installed on your system. You can verify this by running:
```bash
python --version

PRODIGY_CS_01/
│
├── caesar_gui.py       # Main application containing GUI layout and logic
├── README.md           # Project documentation and guide
└── .gitignore          # File specifying ignored files for git
