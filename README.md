# Skeletyl ZMK Firmware Configuration

This repository contains the ZMK firmware configuration for the Skeletyl split keyboard. Below is an up-to-date summary of the keyboard's layers, combos, custom behaviors, and configuration.

---

## Keyboard Overview

- **Keyboard Name:** Skeletyl (Breadboard)
- **Type:** Split, wireless/USB
- **Power:** Bluetooth +8dBm, 30min sleep timeout
- **Features:** Custom combos and multiple layers for enhanced productivity

---

## Layer Summary

### 0: Default Layer
Standard QWERTY typing layer with home row mods and layer-tap keys.

### 1: Symbol Layer
Symbols, brackets, and special characters.

### 2: Navigation Layer
Text navigation, arrow keys, and editing controls.

### 3: Number Layer
Number row and numeric input.

### 4: Function Layer
F1–F12 keys and system functions.

### 5: Media Layer
Media controls (volume, playback, etc).

### 6: Gaming Layer
Optimized for gaming (WASD, quick melee, comms).

### 7: Bluetooth Layer
BT profile selection and management.

### 8: Tab Layer
Tab navigation and special functions.

---

## Keymap Visual Reference

See `config/key_positions_visual.md` for a full matrix and position reference:

```
╭────────┬────────┬────────┬────────┬────────╮   ╭────────┬────────┬────────┬────────┬────────╮
│   0    │   1    │   2    │   3    │   4    │   │   5    │   6    │   7    │   8    │   9    │ 
│   Q    │   W    │   E    │   R    │   T    │   │   Y    │   U    │   I    │   O    │   P    │
├────────┼────────┼────────┼────────┼────────┤   ├────────┼────────┼────────┼────────┼────────┤
│   10   │   11   │   12   │   13   │   14   │   │   15   │   16   │   17   │   18   │   19   │
│   A    │   S    │   D    │   F    │   G    │   │   H    │   J    │   K    │   L    │  APOS  │
├────────┼────────┼────────┼────────┼────────┤   ├────────┼────────┼────────┼────────┼────────┤
│   20   │   21   │   22   │   23   │   24   │   │   25   │   26   │   27   │   28   │   29   │
│   Z    │   X    │   C    │   V    │   B    │   │   N    │   M    │ COMMA  │  DOT   │ SLASH  │
╰────────┴────────┴────────┴────────┴────────╯   ╰────────┴────────┴────────┴────────┴────────╯

                  ╭────────┬────────┬────────╮   ╭────────┬────────┬────────╮
                  │   30   │   31   │   32   │   │   33   │   34   │   35   │
                  │        │        │ SPACE  │   │ ENTER  │        │        │
                  ╰────────┴────────┴────────╯   ╰────────┴────────┴────────╯
```

---

## Current Layer Implementation

The default layer features:
- QWERTY layout with strategic layer-tap keys
- Mod-taps on the home row and bottom row
- Layer access through hold and combo actions

Additional layers provide:
- Full symbol access in Symbol layer
- Navigation with arrow keys and editing controls
- Number row and function keys
- Media controls and specialized gaming layout
- Bluetooth device management

---

## Combo System

For a comprehensive reference of all keyboard combos, see the [COMBOS.md](COMBOS.md) file.

### Key Layer Access Combos

| Combo Keys | Action | Active Layers |
|------------|--------|---------------|
| D+F (12+13) | Toggle Symbol / Return to Default | All |
| J+K (16+17) | Toggle Symbol / Return to Default | All |
| M+K (26+17) | Toggle Navigation / Return to Default | All |
| M+COMMA (26+27) | Toggle Function / Return to Default | All |
| W+E+R (1+2+3) | Toggle Gaming / Return to Default | All |
| B+N (24+25) | Toggle Bluetooth | All except BT |
| R+T (3+4) | Toggle Bluetooth | All except BT |

### Frequently Used Combos

| Combo Keys | Action | Active Layers |
|------------|--------|---------------|
| Q+P (0+9) | Tilde (~) | Default |
| Q+W (0+1) | Escape | All |
| Z+SLASH (20+29) | Lock Session (Ctrl+Alt+L) | All |
| W+K (1+17) | Alt+F4 | Default |
| A+APOS (10+19) | Double Shift | All |
| X+DOT (21+28) | Paste Git Token | All |
| F+K (13+17) | GUI Key | All |

---

## Custom Behaviors

- **Mod-Tap (`mt`, `mth`, `mtb`):** Tap/hold with different behaviors (200ms tapping term)
  - `mt`: Tap-preferred
  - `mth`: Hold-preferred
  - `mtb`: Balanced

- **Sticky Layer (`sl`):** One-shot layer activation (5s timeout)

- **Long Sticky Key (`long_sk`):** Extended sticky key (30s timeout)

- **Layer-Tap (`lt`):** Tap for key, hold for layer

- **Layer-Mod Macro (`lm`):** Layer+modifier combination

- **Tap-Dance:** Multiple actions from single key
  - Single/double tap behaviors for I and O keys

---

## Macros

- **Zed-Em-Kay:** Types "ZMK" with shift
- **Open Terminal:** Ctrl+Alt+T
- **Double Shift:** Sends two shift keypresses
- **Paste Git Token:** Ctrl+Alt+P
- **Lock Session:** Ctrl+Alt+L
- **Quick Melee:** V key (for gaming)
- **Quick Hello:** Ctrl+C (for in-game communication)
- **Alt+F4:** Close window

---

## Configuration Highlights

- Bluetooth with +8dBm transmit power
- 30 minute sleep timeout
- Custom Bluetooth name: "Skeletyl"

---

## How to Use

1. Use the key position reference when modifying your keymap
2. Edit `skeletyl.keymap` to change layer and key assignments
3. Edit `skeletyl.combos` to modify combo behavior
4. Use the built-in macros and behaviors for advanced functionality

---

## Navigation Structure

The Skeletyl uses an intuitive layer navigation system with mirror-symmetric combos. Most layer-switching combos also work to return to the default layer when pressed again, creating a consistent and easy-to-remember interface.

---
