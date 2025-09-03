#!/bin/bash
# ZMK Layer Notifier Installation Script

echo "ZMK Layer Notifier Installer"
echo "============================"
echo

# Check if running as root
if [ "$EUID" -eq 0 ]; then
  echo "Please do not run this script as root. It will use sudo when needed."
  exit 1
fi

# Install dependencies
echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3-evdev python3-notify2 python3-gi gir1.2-appindicator3-0.1 python3-pip
pip3 install --user pynput

# Make the scripts executable
chmod +x "$(dirname "$0")/zmk_layer_notifier.py"
chmod +x "$(dirname "$0")/zmk_simple_notifier.py"

# Create autostart entries
echo "Creating autostart entry..."
mkdir -p "$HOME/.config/autostart"

# Choose which notifier to use
echo
echo "Which notifier would you like to use?"
echo "1) Full applet with system tray icon (requires more dependencies)"
echo "2) Simple notifier with notifications only"
read -p "Enter your choice (1 or 2, default: 2): " choice

# Default to simple notifier
choice=${choice:-2}

if [ "$choice" -eq 1 ]; then
  SCRIPT_PATH="$(realpath "$(dirname "$0")/zmk_layer_notifier.py")"
  DESKTOP_NAME="ZMK Layer Notifier (Applet)"
else
  SCRIPT_PATH="$(realpath "$(dirname "$0")/zmk_simple_notifier.py")"
  DESKTOP_NAME="ZMK Layer Notifier"
fi

# Create desktop file
cat > "$HOME/.config/autostart/zmk-layer-notifier.desktop" << EOF
[Desktop Entry]
Type=Application
Name=$DESKTOP_NAME
Comment=Displays notifications when ZMK layers change
Exec=python3 $SCRIPT_PATH
Terminal=false
Hidden=false
X-GNOME-Autostart-enabled=true
EOF

echo
echo "Installation complete!"
echo "The notifier will start automatically when you log in."
echo "You can start it now by running: python3 $SCRIPT_PATH"
echo
read -p "Would you like to start the notifier now? (y/n, default: y): " start_now

# Default to yes
start_now=${start_now:-y}

if [[ $start_now == "y" || $start_now == "Y" ]]; then
  echo "Starting notifier..."
  python3 "$SCRIPT_PATH" &
  echo "Notifier is running in the background."
fi

echo
echo "To uninstall, simply delete the autostart entry:"
echo "rm $HOME/.config/autostart/zmk-layer-notifier.desktop"
echo
