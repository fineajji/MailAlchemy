import argparse

# Function to generate email permutations
def generate_email_permutations(names, domain="domain.com"):
    email_permutations = []
    for name in names:
        parts = name.strip().split()
        first = parts[0]
        last = parts[-1]
        middle = parts[1] if len(parts) > 2 else ""

        # Generate all permutations in original case, lowercase, and uppercase
        permutations = [
            f"{first}@{domain}",                          # fn
            f"{last}@{domain}",                           # ln
            f"{first}{last}@{domain}",                    # fnln
            f"{first}.{last}@{domain}",                   # fn.ln
            f"{first[0]}{last}@{domain}",                 # filn
            f"{first[0]}.{last}@{domain}",                # fi.ln
            f"{first}{last[0]}@{domain}",                 # fnli
            f"{first}.{last[0]}@{domain}",                # fn.li
            f"{first[0]}{last[0]}@{domain}",              # fili
            f"{first[0]}.{last[0]}@{domain}",             # fi.li
            f"{last}{first}@{domain}",                    # lnfn
            f"{last}.{first}@{domain}",                   # ln.fn
            f"{last}{first[0]}@{domain}",                 # lnfi
            f"{last}.{first[0]}@{domain}",                # ln.fi
            f"{last[0]}{first}@{domain}",                 # lifn
            f"{last[0]}.{first}@{domain}",                # li.fn
            f"{last[0]}{first[0]}@{domain}",              # lifi
            f"{last[0]}.{first[0]}@{domain}",             # li.fi
            f"{first[0]}{middle[0] if middle else ''}{last}@{domain}",  # fimiln
            f"{first[0]}{middle[0] if middle else ''}.{last}@{domain}", # fimi.ln
            f"{first}{middle[0] if middle else ''}{last}@{domain}",     # fnmiln
            f"{first}.{middle[0] if middle else ''}.{last}@{domain}",   # fn.mi.ln
            f"{first}{middle}{last}@{domain}",                          # fnmnln
            f"{first}.{middle}.{last}@{domain}",                        # fn.mn.ln
            f"{first}-{last}@{domain}",                 # fn-ln
            f"{first[0]}-{last}@{domain}",              # fi-ln
            f"{first}-{last[0]}@{domain}",              # fn-li
            f"{first[0]}-{last[0]}@{domain}",           # fi-li
            f"{last}-{first}@{domain}",                 # ln-fn
            f"{last}-{first[0]}@{domain}",              # ln-fi
            f"{last[0]}-{first}@{domain}",              # li-fn
            f"{last[0]}-{first[0]}@{domain}",           # li-fi
            f"{first[0]}{middle[0] if middle else ''}-{last}@{domain}",   # fimi-ln
            f"{first}-{middle[0] if middle else ''}-{last}@{domain}",     # fn-mi-ln
            f"{first}-{middle}-{last}@{domain}",                          # fn-mn-ln
            f"{first}_{last}@{domain}",                 # fn_ln
            f"{first[0]}_{last}@{domain}",              # fi_ln
            f"{first}_{last[0]}@{domain}",              # fn_li
            f"{first[0]}_{last[0]}@{domain}",           # fi_li
            f"{last}_{first}@{domain}",                 # ln_fn
            f"{last}_{first[0]}@{domain}",              # ln_fi
            f"{last[0]}_{first}@{domain}",              # li_fn
            f"{last[0]}_{first[0]}@{domain}",           # li_fi
            f"{first[0]}{middle[0] if middle else ''}_{last}@{domain}",   # fimi_ln
            f"{first}_{middle[0] if middle else ''}_{last}@{domain}",     # fn_mi_ln
            f"{first}_{middle}_{last}@{domain}",                            # fn_mn_ln
        ]
        
        # Add original case, lowercase, and uppercase variations
        email_permutations.extend(permutations)  # Original case
        email_permutations.extend([email.lower() for email in permutations])  # Lowercase
        email_permutations.extend([email.upper() for email in permutations])  # Uppercase

    return email_permutations

# Main function to handle command line arguments
def main():
    parser = argparse.ArgumentParser(description="Generate email permutations from names.")
    parser.add_argument("-d", "--domain", required=True, help="Domain for the emails.")
    parser.add_argument("-f", "--file", required=True, help="File containing names.")
    parser.add_argument("-o", "--output", required=True, help="Output file for email permutations.")

    args = parser.parse_args()

    # Read names from the file
    with open(args.file, "r") as file:
        names = file.readlines()

    # Generate email permutations
    emails = generate_email_permutations(names, domain=args.domain)

    # Write the emails to the output file
    with open(args.output, "w") as output_file:
        for email in emails:
            output_file.write(email + "\n")

if __name__ == "__main__":
    main()

