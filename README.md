f1 f2 f3 f4 f5    f6 f7 f8 f9 f10
esc q w e r    2 3 i o to0
# Skeletyl ZMK Firmware Configuration

This repository contains the ZMK firmware configuration for the Skeletyl split keyboard. Below is an up-to-date summary of the keyboard's layers, combos, custom behaviors, and configuration.

---

## Keyboard Overview

- **Keyboard Name:** Skeletyl (Breadboard)
- **Type:** Split, wireless/USB, QMK/ZMK-inspired
- **Power:** Bluetooth +8dBm, 30min sleep, deep sleep enabled
- **Features:** Split BLE, USB on both halves, battery reporting, reliable split sync

---

## Layer Summary

### 0: Default Layer
Standard QWERTY typing layer.

### 1: Symbol Layer
Symbols, brackets, and shifted characters.

### 2: Navigation Layer
Text navigation, arrow keys, and editing controls.

### 3: Number Layer
Number row and numeric input.

### 4: Function Layer
F1–F12 and related keys.

### 5: Media Layer
Media controls (play, volume, next/prev, etc).

### 6: Gaming Layer
Optimized for Overwatch and similar games (WASD, quick melee, comms, etc).

---

## Keymap Visual Reference

See `config/key_positions_visual.md` for a full matrix and position reference.

---

## Combo & Layer Logic

### Sticky Layer Combos (One-Shot)
- **D+K (12+17):** Sticky SYMBOL (from Default)
- **E+I (2+7):** Sticky NUMBER (from Default)
- **C+COMMA (22+27):** Sticky FUNCTION (from Default)

### Shifted/Toggle Combos
- **W+O (1+8):** Toggle NUMBER layer
- **S+L (11+18):** Toggle SYMBOL layer
- **X+DOT (21+28):** Toggle FUNCTION layer

### Navigation/Default Layer Switching
- **M+K, K+L, M+K+L:** Switch to NAVIGATION from any layer except NAVIGATION; same combos on NAVIGATION return to DEFAULT

### Other Combos
- **Q+P:** Tilde (~)
- **Z+SLASH:** Lock session (Ctrl+Alt+L)
- **G+H:** Open terminal (Ctrl+Alt+T)
- **A+APOS:** Double Shift
- **B+N:** Toggle Bluetooth/Function layer
- **W+S+D:** Toggle Gaming layer
- **S+D+F:** Go to Gaming layer (Default only)
- **BT_CLR_ALL:** Clear all Bluetooth profiles (Function layer)
- **W+K:** Alt+F4 (Default only)

---

## Custom Behaviors

- **Mod-Tap (`mt`, `mth`, `mtb`):** Tap/hold with tap-preferred, hold-preferred, or balanced logic (200ms tapping term)
- **Sticky Layer (`sl`, `long_sk`):** One-shot or long sticky layer (2s or 15s timeout)
- **Layer-Tap (`lt`):** Tap for key, hold for layer (applied to key positions 2/7 = NUMBER, 12/17 = SYMBOL, 22/27 = FUNCTION, except where transparent)
- **Macros:** Quick actions (open terminal, lock session, double shift, paste git token, Overwatch comms, etc)
- **Layer-Mod Macro (`lm`):** Temporarily switch to a layer while holding a modifier

---

## Configuration Highlights

- Split BLE with central/peripheral roles
- USB enabled on both halves
- Battery reporting
- Aggressive split sync and connection reliability
- Custom Bluetooth name: "Skeletyl" or "Om"

---

## How to Use

1. Refer to the key position visual (`config/key_positions_visual.md`) for matrix mapping
2. Edit `skeletyl.keymap` for layer and key assignments
3. Edit `skeletyl.combos` for combo logic
4. Use the provided macros and behaviors for advanced functionality

---

## Maintainer Notes

- All layer and combo logic is up-to-date with the current firmware
- Outdated notations and legacy info have been removed
- For further customization, see comments in each config file
- Enhanced Bluetooth connectivity with higher power and improved reliability

- Split keyboard configuration with BLE
