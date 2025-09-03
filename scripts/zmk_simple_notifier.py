#!/usr/bin/env python3
"""
ZMK Layer Status Notifier (Simple Version)

This script listens for keyboard events and shows notifications 
when certain key combinations are detected.

Dependencies:
- python3-evdev
- python3-notify2
"""

import evdev
from evdev import InputDevice, categorize, ecodes
import notify2
import time
import os
import signal
import sys
import subprocess
from threading import Thread, Lock

# Layer definitions and their friendly names
LAYERS = {
    0: {"name": "DEFAULT", "color": "#3584e4", "icon": "input-keyboard"},
    1: {"name": "SYMBOL", "color": "#f5c211", "icon": "accessories-character-map"},
    2: {"name": "NAVIGATION", "color": "#33d17a", "icon": "input-mouse"},
    3: {"name": "NUMBER", "color": "#e66100", "icon": "accessories-calculator"},
    4: {"name": "FUNCTION", "color": "#613583", "icon": "utilities-terminal"},
    5: {"name": "MEDIA", "color": "#1c71d8", "icon": "multimedia-volume-control"},
    6: {"name": "GAMING", "color": "#a51d2d", "icon": "input-gaming"},
    7: {"name": "BLUETOOTH", "color": "#1a5fb4", "icon": "bluetooth"},
    8: {"name": "TAB", "color": "#26a269", "icon": "view-paged"}
}

# Key combinations for each layer (Ctrl+Shift+F20-F24, etc)
LAYER_KEY_COMBINATIONS = {
    # These are the key combinations we defined in the ZMK config
    # In a real implementation, you would need to detect these combinations
    # This is a simplified example
    (29, 42, 88): 0,  # Ctrl+Shift+F20 = DEFAULT layer
    (29, 42, 89): 1,  # Ctrl+Shift+F21 = SYMBOL layer
    (29, 42, 90): 2,  # Ctrl+Shift+F22 = NAVIGATION layer
    (29, 42, 91): 3,  # Ctrl+Shift+F23 = NUMBER layer
    (29, 42, 56, 88): 4,  # Ctrl+Shift+Alt+F20 = FUNCTION layer
    (29, 42, 56, 89): 5,  # Ctrl+Shift+Alt+F21 = MEDIA layer
    (29, 42, 56, 90): 6,  # Ctrl+Shift+Alt+F22 = GAMING layer
    (29, 42, 56, 91): 7,  # Ctrl+Shift+Alt+F23 = BT layer
    (29, 42, 56, 92): 8,  # Ctrl+Alt+Shift+F24 = TAB layer
    (56, 29, 42, 92): -1  # Alt+Ctrl+Shift+F24 = STICKY layer
}

class SimpleLayerNotifier:
    def __init__(self):
        # Initialize notification system
        notify2.init("ZMK Layer Status")
        self.notification = notify2.Notification("ZMK Layer", "Starting...", "input-keyboard")
        self.notification.set_timeout(3000)  # 3 seconds
        
        self.current_layer = 0  # DEFAULT layer
        self.is_sticky = False
        
        # Track pressed keys
        self.pressed_keys = set()
        self.key_lock = Lock()
        
        # Signal handling
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)
        
        self.running = True
    
    def handle_signal(self, sig, frame):
        """Handle termination signals"""
        self.running = False
        sys.exit(0)
    
    def show_notification(self, layer_id, sticky=False):
        """Show a notification with the current layer"""
        if layer_id not in LAYERS and layer_id != -1:
            return
            
        if layer_id == -1:  # Special case for sticky indicator
            self.is_sticky = True
            return
        
        layer_info = LAYERS[layer_id]
        self.current_layer = layer_id
        
        # Format notification
        sticky_text = " (STICKY)" if self.is_sticky else ""
        title = f"ZMK Layer: {layer_info['name']}{sticky_text}"
        
        color = layer_info["color"]
        body = f'<span background="{color}" foreground="white"> {layer_info["name"]} </span>'
        
        # Show notification
        self.notification.update(title, body, layer_info["icon"])
        self.notification.show()
    
    def find_keyboards(self):
        """Find all keyboard devices"""
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        keyboards = []
        
        for device in devices:
            caps = device.capabilities()
            if evdev.ecodes.EV_KEY in caps:
                # Check if this device has typical keyboard keys
                key_caps = caps[evdev.ecodes.EV_KEY]
                key_codes = [code for code in key_caps]
                
                # If it has letter keys, consider it a keyboard
                letter_keys = [evdev.ecodes.KEY_A, evdev.ecodes.KEY_Z, evdev.ecodes.KEY_E]
                if any(key in key_codes for key in letter_keys):
                    keyboards.append(device)
        
        return keyboards
    
    def monitor_keyboard(self, device):
        """Monitor a keyboard for key events"""
        try:
            device.grab()  # Take exclusive control of the device
            
            for event in device.read_loop():
                if not self.running:
                    break
                    
                if event.type == evdev.ecodes.EV_KEY:
                    key_event = categorize(event)
                    
                    with self.key_lock:
                        # Track key press/release
                        if key_event.keystate == key_event.key_down:
                            self.pressed_keys.add(key_event.scancode)
                        elif key_event.keystate == key_event.key_up:
                            if key_event.scancode in self.pressed_keys:
                                self.pressed_keys.remove(key_event.scancode)
                        
                        # Check for layer change combinations
                        for combo, layer in LAYER_KEY_COMBINATIONS.items():
                            if all(key in self.pressed_keys for key in combo):
                                if layer == -1:  # Sticky indicator
                                    self.is_sticky = True
                                else:
                                    self.show_notification(layer, self.is_sticky)
                                    if not self.is_sticky:
                                        self.is_sticky = False  # Reset sticky flag for normal layer changes
        except Exception as e:
            print(f"Error monitoring keyboard {device.name}: {e}")
        finally:
            try:
                device.ungrab()
            except:
                pass
    
    def run(self):
        """Run the notifier"""
        while self.running:
            try:
                keyboards = self.find_keyboards()
                if not keyboards:
                    print("No keyboard devices found. Retrying in 5 seconds...")
                    time.sleep(5)
                    continue
                
                # Start a thread for each keyboard
                threads = []
                for keyboard in keyboards:
                    thread = Thread(target=self.monitor_keyboard, args=(keyboard,))
                    thread.daemon = True
                    threads.append(thread)
                    thread.start()
                
                # Keep the main thread alive
                for thread in threads:
                    while thread.is_alive() and self.running:
                        thread.join(1)
                        
            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(5)

def create_desktop_entry():
    """Create a desktop entry to start the notifier at login"""
    desktop_dir = os.path.expanduser("~/.config/autostart")
    desktop_file = os.path.join(desktop_dir, "zmk-layer-notifier.desktop")
    
    if not os.path.exists(desktop_dir):
        os.makedirs(desktop_dir)
    
    script_path = os.path.abspath(__file__)
    
    with open(desktop_file, "w") as f:
        f.write(f"""[Desktop Entry]
Type=Application
Name=ZMK Layer Notifier
Comment=Displays notifications when ZMK layers change
Exec=python3 {script_path}
Terminal=false
Hidden=false
X-GNOME-Autostart-enabled=true
""")
    
    os.chmod(desktop_file, 0o755)
    print(f"Created autostart entry: {desktop_file}")

if __name__ == "__main__":
    # Process command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        create_desktop_entry()
        print("To install dependencies, run: sudo apt install python3-evdev python3-notify2")
        sys.exit(0)
    
    notifier = SimpleLayerNotifier()
    
    # For testing: simulate layer changes
    def test_layer_changes():
        layer_ids = list(LAYERS.keys())
        i = 0
        sticky = False
        
        while notifier.running:
            layer = layer_ids[i % len(layer_ids)]
            notifier.show_notification(layer, sticky)
            sticky = not sticky if i % 3 == 0 else sticky
            i += 1
            time.sleep(5)
    
    # Uncomment for testing
    # test_thread = Thread(target=test_layer_changes)
    # test_thread.daemon = True
    # test_thread.start()
    
    try:
        notifier.run()
    except KeyboardInterrupt:
        print("Shutting down...")
        notifier.running = False
