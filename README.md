# ZMK Skeletyl Keyboard Configuration

This repository contains the ZMK firmware configuration for a Skeletyl split keyboard. Below is a summary of the keyboard's configuration including layers and behaviors.

## Keyboard Details

- **Keyboard Name**: "Yggdrasil" (Central) / "Skeletyl" (Breadboard)
- **Type**: Split keyboard
- **Power Settings**:
  - Bluetooth signal boost: +8dBm
  - Sleep timeout: 30 minutes (1,800,000ms)
  - Deep sleep enabled

## Layers

### 0: Default Layer
The main typing layer with standard QWERTY layout:
```
q w e r t    y u i o p
a s d f g    h j k l '
z x c v b    n m , . /
    _ _ space enter _ _
```

### 1: Symbol Layer
Contains symbols and brackets:
```
~ ! @ $ &    ] : ; - =
# ^ % * _    [ ( ) _ +
_ _ _ _ _    \ { } | _
    _ _ _ _ bspc _
```

### 2: Text Navigation Layer
Contains navigation controls and text editing functions:
```
a v alt tab _    r f y bspc pgup
shift x c ctrl g    b home up right del
z _ f4 f5 _     d left down end pgdn
    _ / space enter bspc _
```

### 3: Number Layer
Contains number keys:
```
1 2 3 4 5    6 7 8 9 0
_ _ _ _ _    _ _ _ _ _
_ _ _ _ _    _ _ _ _ _
    _ _ _ _ bspc _
```

### 4: Function Layer
Contains function keys:
```
f1 f2 f3 f4 f5    f6 f7 f8 f9 f10
f11 f12 _ _ _    _ _ _ _ _
_ _ _ _ _    _ _ _ _ _
    _ _ _ _ bspc _
```

### 5: Media Layer
Contains media controls:
```
_ _ _ _ _    prev vol- play vol+ next
_ _ _ _ _    _ _ _ _ _
_ _ _ _ _    _ _ _ _ _
    _ to0 _ _ _ _
```

### 6: Gaming Layer (Overwatch)
Optimized layout for playing Overwatch with shifted movement keys:
```
esc q w e r    2 3 i o to0
shift a s d 4    5 h j l enter
sticky-w z x c v    hello m tab . to0
    shift ctrl space q melee f
```
- WASD for movement
- Q for ultimate ability
- Number keys for hero abilities and weapon switching
- Space bar for jump
- Left Shift for hero-specific abilities
- F for quick actions
- Tab key available
- Quick access to communication (hello macro)
- Quick melee attack available
- Easy return to default layer (top-right key)

## Behaviors

### Mod-Tap Variants
1. `mt`: Tap-preferred mod-tap with 200ms tapping term
   - Prioritizes the tap behavior when pressed quickly

2. `mth`: Hold-preferred mod-tap with 200ms tapping term
   - Prioritizes the hold behavior

3. `mtb`: Balanced mod-tap with 200ms tapping term
   - Equal priority to tap and hold behaviors

### Sticky Key Behavior
- `long_sk`: Extended sticky key with 15 second timeout
  - Used for gaming layer to provide temporary sticky modifier

### Layer-Mod Behavior
- `lm`: Custom macro for Layer-Mod combination
  - Temporarily switches to a layer while holding a modifier

## Configuration Details

- Enhanced Bluetooth connectivity with higher power and improved reliability
- Split keyboard configuration with BLE
- USB support on both halves
- Battery reporting enabled
- Improved split connection reliability with optimized parameters

