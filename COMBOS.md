# ZMK Keyboard Combos Guide

This document provides a comprehensive overview of the key combos configured for the Skeletyl keyboard. These combos enhance the keyboard's functionality by allowing quick access to various layers, special characters, and functions by pressing multiple keys simultaneously.

## Key Position Reference

The combos reference key positions based on the following layout:

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

## Layer Definitions

The firmware defines the following layers:

```
#define DEFAULT 0
#define SYMBOL 1
#define NAVIGATION 2
#define NUMBER 3
#define FUNCTION 4
#define MEDIA 5
#define GAMING 6
#define BT 7
#define TAB_LAYER 8
```

## Combo Types

The firmware implements three types of layer-switching combos:

1. **Toggle Layer Combos** (`tog`): Switch to a layer and stay there until toggled again
2. **Sticky Layer Combos** (`sl`): Temporarily switch to a layer for the next keypress
3. **Direct Layer Combos** (`to`): Switch directly to a specific layer

## Key Combo Reference

### Layer Access Combos

#### Number Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `E+I` | 2+7 | One-shot Number layer | DEFAULT |
| `1+2` | 1+2 | One-shot Number layer | DEFAULT and others |
| `7+8` | 7+8 | One-shot Number layer | DEFAULT and others |
| `8+9` | 8+9 | Toggle Number layer | DEFAULT and others |
| From Number layer: `1+2` or `7+8` or `8+9` | - | Return to DEFAULT | NUMBER |

#### Symbol Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `C+COMMA` | 22+27 | One-shot Symbol layer | DEFAULT |
| `11+12` (S+D) | 11+12 | One-shot Symbol layer | DEFAULT and others |
| `17+18` (K+L) | 17+18 | One-shot Symbol layer | DEFAULT and others |
| `D+F` | 12+13 | Toggle Symbol layer | DEFAULT and others |
| `J+K` | 16+17 | Toggle Symbol layer | DEFAULT and others |
| From Symbol layer: `D+F` or `J+K` | - | Return to DEFAULT | SYMBOL |

#### Navigation Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `D+K` | 12+17 | One-shot Navigation layer | DEFAULT |
| `27+28` (COMMA+DOT) | 27+28 | Go to Navigation layer | DEFAULT and others |
| `M+K` | 26+17 | Toggle Navigation layer | DEFAULT and others |
| From Navigation layer: `M+K` or `27+28` | - | Return to DEFAULT | NAVIGATION |

#### Function Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `21+22` (X+C) | 21+22 | One-shot Function layer | DEFAULT and others |
| `M+COMMA` | 26+27 | Toggle Function layer | DEFAULT and others |
| From Function layer: `M+COMMA` | - | Return to DEFAULT | FUNCTION |

#### Gaming Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `S+D+F` | 11+12+13 | Go to Gaming layer | DEFAULT |
| `1+2+3` (W+E+R) | 1+2+3 | Go to Gaming layer | DEFAULT and others |
| `11+2+13` | 11+2+13 | Toggle Gaming layer | DEFAULT and others |
| From Gaming layer: `1+2+3` | - | Return to DEFAULT | GAMING |

#### Bluetooth Layer Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `B+N` | 24+25 | Toggle Bluetooth layer | DEFAULT |
| `30+35` | 30+35 | Go to Bluetooth layer | DEFAULT and others |
| `3+4` (R+T) | 3+4 | Go to Bluetooth layer | DEFAULT and others |
| From BT layer: `30+35` or `3+4` | - | Return to DEFAULT | BT |
| `20+32+33+29` (Z+SPACE+ENTER+SLASH) | - | Clear all Bluetooth bindings | BT |

### Special Function Combos

| Combo Keys | Key Positions | Action | Active Layers |
|------------|--------------|--------|---------------|
| `25+26` (N+M) | 25+26 | Screenshot | DEFAULT and others |
| `0+1` (Q+W) | 0+1 | Escape | ALL |
| `Q+P` | 0+9 | Tilde (~) | DEFAULT |
| `Z+SLASH` | 20+29 | Lock Session (Ctrl+Alt+L) | DEFAULT |
| `G+H` | 14+15 | Open Terminal (Ctrl+Alt+T) | DEFAULT |
| `A+QUOT` | 10+19 | Double Shift | DEFAULT |
| `F+K` | 13+17 | GUI (Windows/Super) key | DEFAULT |
| `X+DOT` | 21+28 | Paste Git Token | DEFAULT |
| `W+K` | 1+17 | Alt+F4 | DEFAULT |

## Timeout Configuration

Combos are configured with various timeout periods based on their complexity:

- Most layer-switching combos: 25ms timeout
- Gaming layer combos: 15-30ms timeout
- Special function combos: 20-50ms timeout

## Customizing Combos

To modify or add new combos:

1. Edit the `/home/yogi/prog/zmk-breadboard/config/skeletyl.combos` file
2. Follow the existing pattern for defining new combos:

```c
combo_name {
    timeout-ms = <XX>;         // Timeout in milliseconds
    key-positions = <X Y>;     // Key position numbers
    bindings = <&action>;      // Action to perform
    layers = <LAYERS>;         // Layers where combo is active
};
```

## Additional Notes

- All combo definitions are in the `/home/yogi/prog/zmk-breadboard/config/skeletyl.combos` file
- Combos help maximize the functionality of this small keyboard layout
- Layer-specific combos allow for quick toggling between layers and returning to the default layer
- The firmware includes specialized macros for gaming and system operations
