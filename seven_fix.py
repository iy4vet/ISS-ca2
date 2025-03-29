def find_cube_pairs(target):            # fix: added colon at the end of function defn
    solutions = []                      # fix: removed terminating semicolon
    max_num = round(target ** (1 / 3))  # fix: renamed targ to target; changed *** to ** for exponent operator

    for a in range(1, max_num + 1):     # fix: changed ranges to range; added colon at the end of for statement
        for b in range(a, max_num + 1): # fix: (same as above)
            if a**3 + b**3 == target:   # fix: renamed targ to target; changed *** to ** for exponent operator; added colon at the end of if statement
                solutions.append((a, b))# fix: renamed sol to solutions; removed terminating semicolon
    return solutions                    # fix: renamed sol to solutions


pairs = find_cube_pairs(1729)           # fix: removed terminating comma
print("Valid cube pairs for 1729:")     # fix: changed printf to print; removed terminating comma; changed 1728 to 1729
for a, b in pairs:                      # fix: renamed pair to pairs; added colon at the end of for statement
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # fix: changed printf to print; changed **2 to **3 for correct exponentiation in the f-string; changed 1728 to 1729
