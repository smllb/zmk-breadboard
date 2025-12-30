# Skeletyl 3x6 Keyboard Key Positions Visual Aid

This document provides a visual representation of the key positions for your modified 3x6 Skeletyl keyboard.

## Key Position Layout

Based on your configuration files and keyboard layout, here's a visual representation of the key positions:

```
╭────────┬────────┬────────┬────────┬────────┬────────╮   ╭────────┬────────┬────────┬────────┬────────┬────────╮
│   0    │   1    │   2    │   3    │   4    │   5    │   │   6    │   7    │   8    │   9    │   10   │   11   │
│  ESC   │   Q    │   W    │   E    │   R    │   T    │   │   Y    │   U    │   I    │   O    │   P    │  NONE  │
├────────┼────────┼────────┼────────┼────────┼────────┤   ├────────┼────────┼────────┼────────┼────────┼────────┤
│   12   │   13   │   14   │   15   │   16   │   17   │   │   18   │   19   │   20   │   21   │   22   │   23   │
│ LSHFT  │   A    │   S    │   D    │   F    │   G    │   │   H    │   J    │   K    │   L    │  APOS  │ LC(BS) │
├────────┼────────┼────────┼────────┼────────┼────────┤   ├────────┼────────┼────────┼────────┼────────┼────────┤
│   24   │   25   │   26   │   27   │   28   │   29   │   │   30   │   31   │   32   │   33   │   34   │   35   │
│ LCTRL  │   Z    │   X    │   C    │   V    │   B    │   │   N    │   M    │ COMMA  │  DOT   │ SLASH  │  NONE  │
╰────────┴────────┴────────┴────────┴────────┴────────╯   ╰────────┴────────┴────────┴────────┴────────┴────────╯

                           ╭────────┬────────┬────────╮   ╭────────┬────────┬────────╮
                           │   36   │   37   │   38   │   │   39   │   40   │   41   │
                           │   X    │  NONE  │ SPACE  │   │ ENTER  │  NAV   │ MEDIA  │
                           ╰────────┴────────┴────────╯   ╰────────┴────────┴────────╯
```

## Matrix Position Reference

This visual aid shows the mapping between physical key positions and matrix coordinates. You can use these positions when configuring your keymap or planning your layout.

### Understanding the Matrix

Each key is identified by a linear index number (0-41) corresponding to the ZMK matrix transform.
- The labels show the default key assignments in the base layer

### Current Layout Structure

- **Top row**: Standard number/letter keys (Q-P)
- **Middle row**: Home row keys (A-APOS)
- **Bottom row**: Bottom row keys (Z-SLASH)
- **Thumb clusters**: Space and Enter keys plus additional positions

## Using This Reference

When modifying your keymap:
1. Use this visual aid to identify the position of keys you want to modify
2. Refer to the matrix position when making changes to your configuration
3. Maintain the logical flow of your layout across different layers
