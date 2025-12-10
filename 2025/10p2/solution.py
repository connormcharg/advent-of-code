import sys
import re
from z3 import *

def solve_with_z3(input_data):
    machines = parse_input(input_data)
    total_presses = 0

    for idx, (buttons, targets) in enumerate(machines):
        # Create an optimizer instance
        opt = Optimize()
        
        # Create an integer variable for each button (b_0, b_1, etc.)
        # These represent how many times we press each button.
        btn_vars = [Int(f'b_{i}') for i in range(len(buttons))]
        
        # Constraint 1: We cannot press a button a negative amount of times
        for v in btn_vars:
            opt.add(v >= 0)
            
        # Constraint 2: The sum of button effects must equal the target for EACH counter
        # We iterate through every target counter (0, 1, 2...)
        for counter_idx, target_val in enumerate(targets):
            # We sum (presses * 1) for every button that affects this specific counter
            # The 'buttons' list contains tuples of indices affected by that button.
            # e.g., if button 0 is (1,3), it affects counters 1 and 3.
            
            # We build the summation expression for z3
            expression = Sum([
                btn_vars[b_idx] 
                for b_idx, affected_indices in enumerate(buttons) 
                if counter_idx in affected_indices
            ])
            
            opt.add(expression == target_val)
            
        # Objective: Minimize the total sum of button presses
        opt.minimize(Sum(btn_vars))
        
        # Check satisfiability
        if opt.check() == sat:
            model = opt.model()
            # Calculate total presses for this machine
            machine_presses = sum(model[v].as_long() for v in btn_vars)
            total_presses += machine_presses
        else:
            print(f"Machine {idx+1}: No solution possible.")

    return total_presses

def parse_input(data):
    machines = []
    lines = data.strip().split('\n')
    for line in lines:
        if not line.strip(): continue
        
        # Parse Targets { ... }
        target_match = re.search(r'\{(.*?)\}', line)
        if not target_match: continue
        targets = [int(x) for x in target_match.group(1).split(',')]
        
        # Parse Buttons (...)
        # The regex finds all occurrences of items inside parentheses
        button_matches = re.findall(r'\(([\d,]*?)\)', line)
        buttons = []
        for b_str in button_matches:
            if not b_str.strip():
                # Button affects nothing
                buttons.append(set())
            else:
                # Convert "0,1,2" -> set(0, 1, 2)
                buttons.append(set(map(int, b_str.split(','))))
        
        machines.append((buttons, targets))
    return machines

# --- PASTE YOUR FULL INPUT BELOW ---
input_str = open(0).read()

print(f"Total Minimum Presses: {solve_with_z3(input_str)}")