#!/usr/bin/env python3
"""
ZMK Layer Notification Applet

This script listens for special key combinations from a ZMK keyboard
and displays a notification showing the current active layer.
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, AppIndicator3, Notify, GLib
import subprocess
import os
import sys
import signal
from threading import Thread
from evdev import InputDevice, ecodes, list_devices, categorize
import time
import configparser

# Layer definitions
LAYERS = {
    "Ctrl+Shift+F20": {"name": "DEFAULT", "color": "#3584e4", "icon": "input-keyboard"},
    "Ctrl+Shift+F21": {"name": "SYMBOL", "color": "#f5c211", "icon": "accessories-character-map"},
    "Ctrl+Shift+F22": {"name": "NAVIGATION", "color": "#33d17a", "icon": "input-mouse"},
    "Ctrl+Shift+F23": {"name": "NUMBER", "color": "#e66100", "icon": "accessories-calculator"},
    "Ctrl+Shift+Alt+F20": {"name": "FUNCTION", "color": "#613583", "icon": "utilities-terminal"},
    "Ctrl+Shift+Alt+F21": {"name": "MEDIA", "color": "#1c71d8", "icon": "multimedia-volume-control"},
    "Ctrl+Shift+Alt+F22": {"name": "GAMING", "color": "#a51d2d", "icon": "input-gaming"},
    "Ctrl+Shift+Alt+F23": {"name": "BLUETOOTH", "color": "#1a5fb4", "icon": "bluetooth"},
    "Ctrl+Alt+Shift+F24": {"name": "TAB", "color": "#26a269", "icon": "view-paged"},
    "Alt+Ctrl+Shift+F24": {"name": "STICKY", "color": "#ffbe6f", "icon": "view-pin"}
}

# Default configuration
DEFAULT_CONFIG = {
    'General': {
        'NotificationTimeout': '3',
        'ShowTrayIcon': 'true',
        'ShowLayerNotifications': 'true'
    },
    'Appearance': {
        'UseSystemTheme': 'true',
        'ShowLayerIcons': 'true'
    }
}

class ZMKLayerNotifier:
    def __init__(self):
        self.current_layer = "DEFAULT"
        self.is_sticky = False
        self.config_file = os.path.expanduser('~/.config/zmk-layer-notifier/config.ini')
        self.load_config()
        
        # Initialize notification system
        Notify.init("ZMK Layer Notifier")
        self.notification = Notify.Notification.new("ZMK Layer", "Starting...", "input-keyboard")
        
        # Create app indicator
        if self.config.getboolean('General', 'ShowTrayIcon'):
            self.indicator = AppIndicator3.Indicator.new(
                "zmk-layer-notifier",
                "input-keyboard",
                AppIndicator3.IndicatorCategory.HARDWARE
            )
            self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
            self.indicator.set_menu(self.create_menu())
            self.update_indicator()
        
        # Start keyboard listener in a separate thread
        self.running = True
        self.listener_thread = Thread(target=self.keyboard_listener)
        self.listener_thread.daemon = True
        self.listener_thread.start()
    
    def load_config(self):
        """Load configuration from file or create default"""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        self.config = configparser.ConfigParser()
        self.config.read_dict(DEFAULT_CONFIG)
        
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            # Create default config
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
    
    def save_config(self):
        """Save current configuration to file"""
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
    
    def create_menu(self):
        """Create the right-click menu for the indicator"""
        menu = Gtk.Menu()
        
        # Layer indicator (not clickable)
        layer_item = Gtk.MenuItem()
        layer_item.set_label(f"Current Layer: {self.current_layer}")
        layer_item.set_sensitive(False)
        menu.append(layer_item)
        
        menu.append(Gtk.SeparatorMenuItem())
        
        # Toggle notifications
        notify_item = Gtk.CheckMenuItem()
        notify_item.set_label("Show Layer Notifications")
        notify_item.set_active(self.config.getboolean('General', 'ShowLayerNotifications'))
        notify_item.connect("toggled", self.toggle_notifications)
        menu.append(notify_item)
        
        # Preferences
        pref_item = Gtk.MenuItem()
        pref_item.set_label("Preferences...")
        pref_item.connect("activate", self.show_preferences)
        menu.append(pref_item)
        
        menu.append(Gtk.SeparatorMenuItem())
        
        # Exit
        exit_item = Gtk.MenuItem()
        exit_item.set_label("Exit")
        exit_item.connect("activate", self.quit)
        menu.append(exit_item)
        
        menu.show_all()
        return menu
    
    def toggle_notifications(self, widget):
        """Toggle showing notifications"""
        self.config.set('General', 'ShowLayerNotifications', str(widget.get_active()))
        self.save_config()
    
    def show_preferences(self, widget):
        """Show preferences dialog"""
        dialog = Gtk.Dialog(
            title="ZMK Layer Notifier Preferences",
            parent=None,
            flags=0
        )
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK)
        dialog.set_default_size(350, 250)
        
        box = dialog.get_content_area()
        box.set_spacing(10)
        box.set_margin_top(10)
        box.set_margin_bottom(10)
        box.set_margin_start(10)
        box.set_margin_end(10)
        
        # Notification timeout
        timeout_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        timeout_label = Gtk.Label(label="Notification Timeout (seconds):")
        timeout_box.pack_start(timeout_label, False, False, 0)
        
        timeout_spinner = Gtk.SpinButton()
        timeout_spinner.set_numeric(True)
        adjustment = Gtk.Adjustment(
            value=float(self.config.get('General', 'NotificationTimeout')),
            lower=1,
            upper=10,
            step_increment=1
        )
        timeout_spinner.set_adjustment(adjustment)
        timeout_box.pack_start(timeout_spinner, False, False, 0)
        box.add(timeout_box)
        
        # Use system theme
        theme_check = Gtk.CheckButton(label="Use System Theme")
        theme_check.set_active(self.config.getboolean('Appearance', 'UseSystemTheme'))
        box.add(theme_check)
        
        # Show layer icons
        icon_check = Gtk.CheckButton(label="Show Layer Icons")
        icon_check.set_active(self.config.getboolean('Appearance', 'ShowLayerIcons'))
        box.add(icon_check)
        
        box.show_all()
        response = dialog.run()
        
        if response == Gtk.ResponseType.OK:
            # Save settings
            self.config.set('General', 'NotificationTimeout', str(int(timeout_spinner.get_value())))
            self.config.set('Appearance', 'UseSystemTheme', str(theme_check.get_active()))
            self.config.set('Appearance', 'ShowLayerIcons', str(icon_check.get_active()))
            self.save_config()
        
        dialog.destroy()
    
    def update_indicator(self):
        """Update the indicator icon and label"""
        if hasattr(self, 'indicator'):
            layer_info = next((layer for key, layer in LAYERS.items() if layer["name"] == self.current_layer), 
                         {"name": "DEFAULT", "icon": "input-keyboard"})
            
            # Update icon
            icon = layer_info["icon"]
            if self.is_sticky:
                icon = "view-pin"
            self.indicator.set_icon_full(icon, f"ZMK Layer: {self.current_layer}")
            
            # Update menu
            menu = self.indicator.get_menu()
            layer_item = menu.get_children()[0]
            sticky_text = " (STICKY)" if self.is_sticky else ""
            layer_item.set_label(f"Current Layer: {self.current_layer}{sticky_text}")
    
    def show_notification(self, layer_name, is_sticky=False):
        """Show a notification with the current layer"""
        if not self.config.getboolean('General', 'ShowLayerNotifications'):
            return
            
        timeout = self.config.getint('General', 'NotificationTimeout') * 1000
        
        layer_info = next((layer for key, layer in LAYERS.items() if layer["name"] == layer_name), None)
        if not layer_info:
            return
            
        # Format notification
        sticky_text = " (STICKY)" if is_sticky else ""
        title = f"ZMK Layer: {layer_name}{sticky_text}"
        
        icon = layer_info["icon"]
        if is_sticky:
            icon = "view-pin"
        
        # Use appropriate color if not using system theme
        if not self.config.getboolean('Appearance', 'UseSystemTheme'):
            color = layer_info["color"]
            body = f'<span background="{color}" foreground="white"> {layer_name} </span>'
        else:
            body = layer_name
        
        # Show notification
        self.notification.update(title, body, icon)
        self.notification.set_timeout(timeout)
        self.notification.show()
    
    def find_keyboard_devices(self):
        """Find all keyboard input devices"""
        devices = [InputDevice(path) for path in list_devices()]
        keyboards = []
        
        for device in devices:
            if ecodes.EV_KEY in device.capabilities():
                # Check if this device has typical keyboard keys
                caps = device.capabilities()[ecodes.EV_KEY]
                key_codes = [code for code, _ in caps]
                
                # If it has letter keys or function keys, consider it a keyboard
                letter_keys = {ecodes.KEY_A, ecodes.KEY_Z, ecodes.KEY_E}
                function_keys = {ecodes.KEY_F1, ecodes.KEY_F4, ecodes.KEY_F20}
                
                if any(key in key_codes for key in letter_keys) or any(key in key_codes for key in function_keys):
                    keyboards.append(device)
        
        return keyboards
    
    def keyboard_listener(self):
        """Listen for ZMK layer change key sequences"""
        while self.running:
            try:
                # Find all keyboard devices
                keyboards = self.find_keyboard_devices()
                if not keyboards:
                    print("No keyboard devices found. Retrying in 5 seconds...")
                    time.sleep(5)
                    continue
                
                # Monitor all keyboards for events
                for keyboard in keyboards:
                    try:
                        for event in keyboard.read():
                            if event.type == ecodes.EV_KEY:
                                key_event = categorize(event)
                                # Process key events to detect our custom sequences
                                # This would need more complex logic to detect the combinations
                                # For demonstration purposes, we'll simulate layer changes here
                                
                                # In a real implementation, you would detect the specific key combinations
                                # that match our ZMK macros defined in layer_notify.dtsi
                    except Exception as e:
                        print(f"Error reading keyboard events: {e}")
                        time.sleep(1)
                
                time.sleep(0.1)
            except Exception as e:
                print(f"Error in keyboard listener: {e}")
                time.sleep(5)
    
    def simulate_layer_change(self, layer_name, sticky=False):
        """Simulate a layer change (for testing)"""
        self.current_layer = layer_name
        self.is_sticky = sticky
        self.update_indicator()
        self.show_notification(layer_name, sticky)
    
    def quit(self, widget=None):
        """Exit the application"""
        self.running = False
        if self.listener_thread.is_alive():
            self.listener_thread.join(1)
        Notify.uninit()
        Gtk.main_quit()

def main():
    # Handle signals
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    
    app = ZMKLayerNotifier()
    
    # For testing: simulate layer changes every 5 seconds
    def test_layer_changes():
        layers = ["DEFAULT", "SYMBOL", "NAVIGATION", "NUMBER", "FUNCTION", "MEDIA", "GAMING", "BLUETOOTH", "TAB"]
        i = 0
        sticky = False
        
        while True:
            layer = layers[i % len(layers)]
            app.simulate_layer_change(layer, sticky)
            sticky = not sticky if i % 3 == 0 else sticky
            i += 1
            time.sleep(5)
    
    # Uncomment for testing
    # test_thread = Thread(target=test_layer_changes)
    # test_thread.daemon = True
    # test_thread.start()
    
    try:
        Gtk.main()
    except KeyboardInterrupt:
        app.quit()

if __name__ == "__main__":
    main()
