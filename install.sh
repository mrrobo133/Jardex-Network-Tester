#!/bin/bash

echo "[+] Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "[+] Installing Git, Python, and dependencies..."
pkg install git python -y

echo "[+] Installing required Python packages (Pip & Flask)..."
pip install --upgrade pip
pip install flask

echo "[+] Setting up execution permissions..."
if [ -f "jardex.py" ]; then
    chmod +x jardex.py
    echo "[+] Main file 'jardex.py' found and configured."
else
    echo "[!] Warning: 'jardex.py' not found in current directory."
fi

echo ""
echo "[+] Installation Completed Successfully!"
echo "[+] Run your tool using: python jardex.py"
