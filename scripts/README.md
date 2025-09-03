# ZMK Layer Notifier

A system tray applet and notification system for ZMK keyboard layers.

## Features

- System tray icon showing current active layer
- Desktop notifications when changing layers
- Distinguishes between normal and sticky layers
- Different colors and icons for each layer
- Customizable preferences

## Installation

1. First, make sure your ZMK firmware is properly updated with the layer notification macros.
   The `layer_notify.dtsi` file needs to be included in your keymap.

2. Run the installation script:
   ```bash
   cd /path/to/zmk-breadboard/scripts
   chmod +x install_notifier.sh
   ./install_notifier.sh
   ```

3. The script will:
   - Install required dependencies
   - Set up an autostart entry to run at login
   - Optionally start the notifier immediately

## Usage

The notifier will show:
- A system tray icon showing your current layer
- Notifications when you change layers
- Different icons for each layer type
- Special indication for sticky layers

Right-click the system tray icon to:
- View the current active layer
- Toggle notifications on/off
- Access preferences
- Exit the application

## Customization

You can modify the appearance and behavior through the preferences dialog:
- Set notification timeout
- Use system theme or custom colors
- Show/hide layer icons

## Troubleshooting

If the notifier doesn't show layer changes:
1. Make sure your ZMK firmware includes the layer_notify.dtsi file
2. Check that the notifier is running (should be in your system tray)
3. Try manually running the notifier from the terminal:
   ```bash
   python3 /path/to/zmk-breadboard/scripts/zmk_layer_notifier.py
   ```

## Uninstallation

```bash
rm ~/.config/autostart/zmk-layer-notifier.desktop
```

Then kill any running instances:
```bash
pkill -f zmk_layer_notifier.py
```
