# ZMK Skeletyl Keyboard Configuration

This repository contains the ZMK firmware configuration for a Skeletyl split keyboard. Below is a summary of the keyboard's configuration including layers, behaviors, macros, and combos.

## Keyboard Details

- **Keyboard Name**: "Yggdrasil" (Central) / "Skeletyl" (Breadboard)
- **Type**: Split keyboard
- **Power Settings**:
  - Bluetooth signal boost: +8dBm
  - Sleep timeout: 30 minutes (1,800,000ms)
  - Deep sleep enabled

## Layers

### 0: Default Layer
The main typing layer with mod-tap keys for common modifiers:
- Home row modifiers: Shift on A and ' (apostrophe)
- Bottom row modifiers: Ctrl on Z and / (slash)
- Layer access via hold: F and J access symbol layer (1)
- Layer access via hold: D and K access media layer (3)
- Layer access via hold: V and M access function layer (2)
- P key: Access to alt_tab layer (5) on tap-hold

### 1: Symbol Layer
Contains symbols and brackets:
- Upper row: ~, !, @, #, $, ], ;, :, -, =
- Middle row: *, %, ^, &, ;, [, (, ), _, +
- Bottom row: F4, F5, Del, Right, :, layer 0, {, }, \, |
- Navigation controls and modifiers preserved

### 2: Function Layer
Contains number keys and function keys:
- Upper row: Number keys 1-0
- Middle row: F1-F3, F11, F7-F9
- Bottom row: F4-F6, Left, Right, F10, F12
- Several "to 0" bindings to return to default layer

### 3: Media Layer
Contains media controls and navigation:
- Volume and playback controls
- Arrow keys for navigation
- Home, End, Page Up, Page Down
- Tab key and modifiers

### 4: Bluetooth Layer
For managing Bluetooth connections:
- BT_SEL 0-4: Select profiles
- BT_PRV/BT_NXT: Cycle profiles
- BT_CLR: Clear current profile
- OUT_TOG: Toggle output (USB/BLE)

### 5: Alt Tab Layer
Special layer for window switching:
- Alt+Tab and Alt+Shift+Tab for window navigation
- Tab navigation with and without shift
- Returns to default layer when done

### 6: Gaming Layer (Overwatch)
Optimized layout for playing Overwatch with shifted movement keys:
- QWED for movement (shifted one key to the right from traditional WASD)
- Q for ultimate ability (bottom right thumb key)
- Number keys for hero abilities and weapon switching
- Space bar for jump
- Left Shift for hero-specific abilities
- F for quick actions (lower right thumb key)
- Tab key available on both top and middle rows
- Quick access to communication (quick_hello macro)
- Quick melee attack available (via quick_melee macro)
- Easy return to default layer (top-right key)

## Behaviors

### Mod-Tap Variants
1. `mt`: Tap-preferred mod-tap with 200ms tapping term
   - Used for most modifier keys
   - Prioritizes the tap behavior when pressed quickly

2. `mth`: Hold-preferred mod-tap with 200ms tapping term
   - Used for specific keys (like RCTRL/SLASH)
   - Prioritizes the hold behavior

3. `mtb`: Balanced mod-tap with 200ms tapping term
   - Used for LSHIFT/APOS
   - Equal priority to tap and hold behaviors

### Layer-Mod Behavior
- `lm`: Custom macro for Layer-Mod combination
  - Temporarily switches to a layer while holding a modifier
  - Example: `&lm 5 LALT` - Access layer 5 while holding ALT

## Macros

1. `zed_em_kay`: Types "ZMK" with shift held down
2. `open_terminal`: Opens terminal with Ctrl+Alt+T
3. `double_lshift`: Taps left shift twice (commonly used for caps word in ZMK)
4. `paste_git_token`: Sends Ctrl+Alt+P to paste a stored git token
5. `alt_tab_macro`: Complex macro for window switching
   - Presses Alt+Tab
   - Releases Tab but keeps Alt pressed
   - Switches to the alt_tab layer
   - Releases Alt when leaving the layer
6. `lock_session`: Sends Ctrl+Alt+L to lock the screen
7. `quick_melee`: Sends V key for quick melee attack in Overwatch
8. `quick_hello`: Sends Ctrl+C for quick "Hello" communication in Overwatch
9. `toggle_gaming`: Toggles the gaming layer (6) for Overwatch

## Combos

| Keys         | Action                    | Description                                                      |
|--------------|---------------------------|------------------------------------------------------------------|
| S+L          | Open Terminal             | Opens terminal with Ctrl+Alt+T                                   |
| F+K          | GUI                       | Sends the GUI (Windows/Command) key                              |
| D+K          | Caps Lock                 | Toggles caps lock                                                |
| Q+P          | Tilde (~)                 | Types tilde character                                            |
| Z+/          | Lock Session              | Locks session with Ctrl+Alt+L                                    |
| A+'          | Double Shift              | Taps shift twice (caps word)                                     |
| B+N          | Toggle Bluetooth Layer    | Switches to BT layer (4)                                         |
| G+B          | Toggle Gaming Layer       | Toggles gaming layer (6) for Overwatch                           |
| S+D+F        | Go to Gaming Layer        | Directly goes to gaming layer (6), only active on default layer  |
| M+K          | Toggle Media Layer        | Toggles media layer (3)                                          |
| K+L          | Toggle Media Layer        | Toggles media layer (3)                                          |
| M+K+L        | Toggle Media Layer        | Toggles media layer (3)                                          |
| LEFT+UP      | Return to Default         | Goes to layer 0                                                  |
| LEFT+UP+RIGHT| Return to Default         | Goes to layer 0                                                  |
| RIGHT+UP     | Return to Default         | Goes to layer 0                                                  |
| X+.          | Paste Git Token           | Pastes git token                                                 |
| A+APOS       | Double Shift              | Taps shift twice (caps word)                                     |
| ESC          | Escape                    | Types escape key                                                 |
| W+O          | Alt+F4                    | Triggers Alt+F4 macro (close window), only on default layer      |
| Z+SLASH      | Lock Session              | Locks session with Ctrl+Alt+L                                    |
| BT_CLR_ALL   | Clear all BT profiles     | Clears all Bluetooth profiles, only on Bluetooth layer           |

## Configuration Details

- Enhanced Bluetooth connectivity with higher power and improved reliability
- Split keyboard configuration with BLE
- USB support on both halves
- Battery reporting enabled
- Improved split connection reliability with optimized parameters


a diferenciação deve ser feita pelo ID do parente seguindo a estrutura abaixo:

Assumindo:

