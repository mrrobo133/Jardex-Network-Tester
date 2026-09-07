# 🛡️ JARDEX - STRESS TESTING & ETHICAL HACKING LAB

*An advanced, multi-threaded local infrastructure stress-testing suite designed specifically for ethical hacking laboratories and educational simulations inside Termux.*

---

## ⚡ Overview
**Jardex** is a lightweight, command-line-driven security and load-testing tool designed to simulate concurrent network traffic against isolated local servers to analyze bandwidth behavior and stability.

---

## ⚠️ CRITICAL LEGAL DISCLAIMER
> **ATTENTION:** This software is strictly intended for **educational purposes and authorized testing within private localhost lab environments**. Executing stress-testing modules against public networks without explicit prior written authorization is **illegal**. The developer assumes **ZERO liability**.

---

## 🚀 Key Features
- **Multi-Threaded Engine:** High-speed concurrent packet dispatching using Python's `threading` and `socket` modules.
- **Batching & Rate Limiting:** Optimized request routing to prevent terminal crashes.
- **Secure Authentication Gate:** Built-in lightweight registration and login verification layer.
- **Termux Optimized:** Runs smoothly on Android via Termux.

---

## 🛠️ Installation & Usage Guide

Copy and execute the commands directly in your Termux or Linux terminal:


# 1. Clone the Repository (
```bash
git clone https://github.com/mrrobo133/Jardex-Network-Tester.git
```
# 2. Navigate into the project directory
```bash
cd jardex
```
# 3. Run the automated installation script
```bash
chmod +x install.sh
```
install tool
```bash
./install.sh
```
# 4. Launch the too
```bash
python jardex.py
```
