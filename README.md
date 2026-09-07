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
cd Jardex-Network-Tester
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
# 🛡️ JARDEX - LOCAL STRESS TESTING SUITE

A lightweight, Python-based stress-testing and simulation tool designed for educational lab environments in Termux.

---

## 🔐 Authentication & Audit Guide

Before accessing the main stress-testing features, Jardex requires a secure local login and audit identification to maintain accountability logs.

* **Registration:** When you first launch the tool, select option `2` to register. Provide a unique username and password to create your local lab profile.
* **Login:** Select option `1` and enter your registered credentials to enter the main menu.
* **Audit Gmail / ID:** Upon launching the stress test module, the tool will prompt you for an **Audit Gmail/ID** (e.g., `yourname@gmail.com` or a custom identifier like `jjx`). This acts as an audit trail signature to track who initiated the test session.

---

## 💻 How to Use the Tool

1. **Launch:** Run the application script in your terminal.
2. **Authenticate:** Log in using your registered username and password.
3. **Select Module:** Choose the DDoS/Stress Test option from the main menu.
4. **Enter Audit ID:** Provide your tracking Gmail or identity when asked.e.g., `audit.lab.user@gmail.com` — *No password needed*).
5. **Target Setup:** Input your local lab URL or IP (e.g., `http://127.0.0.1:8080`).
6. **Set Limit:** Specify the total number of packets (up to 10,000) and monitor the multi-threaded delivery in real-time.
