# Skeletyl Keyboard Key Positions Visual Aid

This document provides a visual representation of the key positions used in your ZMK combos configuration.

## Key Position Layout

Based on your configuration files and keyboard layout, here's a visual representation of the key positions:

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
╰────────┴────────┴────────┼────────┼────────┤   ├────────┼────────┼────────┴────────┴────────╯
                           │   30   │   31   │   │   32   │   33   │
                           │  SYM   │  ESC   │   │ SPACE  │  BSPC  │
                           ╰────────┴────────╯   ╰────────┴────────╯
                                                                   │   34   │   35   │
                                                                   │ ENTER  │  FUNC  │
                                                                   ╰────────┴────────╯
```

## Current Combos Reference

Here are your currently configured combos with their key positions:

| Combo Name | Key Positions | Keys | Action |
|------------|---------------|------|--------|
| combo_tgl3_mk | 26 17 | M + K | Toggle Layer 3 |
| combo_tgl3_kl | 17 18 | K + L | Toggle Layer 3 |
| combo_tgl3_mkl | 26 17 18 | M + K + L | Toggle Layer 3 |
| combo_layer0_leftup | 25 27 | N + COMMA | Go to Layer 0 |
| combo_layer0_leftupright | 25 27 28 | N + COMMA + DOT | Go to Layer 0 |
| combo_layer0_rightup | 28 27 | DOT + COMMA | Go to Layer 0 |
| combo_bluetooth_bn | 24 25 | B + N | Toggle Bluetooth Layer |
| combo_terminal_sl | 14 18 | G + L | Open Terminal |
| combo_gui_fk | 13 17 | F + K | GUI Key |
| combo_git_token_xdot | 21 28 | X + DOT | Paste Git Token |
| combo_double_shift_a_apos | 10 19 | A + APOS | Double Shift |
| combo_lock_session_z_slash | 20 29 | Z + SLASH | Lock Session (Ctrl+Alt+L) |
| combo_caps_dk | 12 17 | D + K | Caps Lock |
| combo_esc | 0 1 | Q + W | Escape |
| combo_gaming_wsd | 1 11 12 | W + S + D | Toggle Gaming Layer |
| combo_gaming_sdf | 11 12 13 | S + D + F | Go to Gaming Layer |
| combo_bt_clear_all | 10 19 | A + APOS | Clear BT Profiles (on BT layer) |
| combo_alt_f4 | 1 8 | W + O | Alt+F4 |
| combo_terminal_gh | 14 15 | G + H | Ctrl+Alt+T (Terminal) |
| combo_tilde_qp | 0 9 | Q + P | Tilde (~) |
| combo_gaming_gb | 14 24 | G + B | Toggle Gaming Layer |

## Notes for Creating New Combos

When creating new combos:

1. Use the visual aid above to determine key positions
2. Be careful not to create unintentional conflicts with existing combos
3. For layer-specific combos, remember to use the `layers = <X>` parameter
4. Adjust the timeout-ms value based on how quickly you want to trigger the combo:
   - Use 30-50ms for standard combos
   - Use 75ms+ for combos that are harder to press simultaneously

## Troubleshooting Combos

If a combo isn't working:

1. Check for position conflicts with other combos
2. Verify the positions match your intended keys
3. Check if the combo is restricted to specific layers
4. Try increasing the timeout-ms value slightly
5. Ensure your ZMK firmware is updated
