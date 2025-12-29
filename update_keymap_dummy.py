import re

def transform_keymap(match):
    content = match.group(1)
    # Split into rows based on newlines or just process the whole block
    # The keymap structure is:
    # Row 0: 11 keys -> 12 keys (add &none at end)
    # Row 1: 11 keys -> 12 keys (add &none at end)
    # Row 2: 11 keys -> 12 keys (add &none at end)
    # Row 3: 6 keys -> 6 keys (no change)
    
    # We need to be careful not to break the syntax.
    # Let's split by lines and process.
    lines = content.strip().split('\n')
    new_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if it's a row definition (contains multiple bindings)
        if '&' in line:
            # Count bindings
            bindings = line.split('&')
            # Remove empty first element if line starts with &
            if bindings[0].strip() == '':
                bindings = bindings[1:]
            else:
                # This case is tricky, usually starts with &
                pass
            
            # Reconstruct bindings with & prefix
            bindings = ['&' + b.strip() for b in bindings if b.strip()]
            
            # Check if it's a main row (11 keys)
            if len(bindings) == 11:
                # Add &none (or &trans for non-default layers) to the end
                # We need to know if it's default layer or not.
                # But the regex context doesn't give us layer name easily.
                # However, we can infer from the content.
                # If the line contains &kp, &mt, &lt, it's likely a binding line.
                
                # Actually, simpler approach:
                # Just append a placeholder and let the user decide?
                # Or use &trans for everything except default layer?
                # The user request implies adding a column.
                
                # Let's just append `&none` for now, user can change it.
                # Wait, for non-default layers `&trans` is better.
                # But I can't easily distinguish.
                # Let's use `&trans` as it's safer for layers, and `&none` for default?
                # I'll use `&trans` for all, and then manually fix default layer if needed.
                # Actually, I'll read the file and do it with replace_string_in_file for better control.
                pass

    return match.group(0)

# I will use replace_string_in_file instead of this script for keymap updates.
