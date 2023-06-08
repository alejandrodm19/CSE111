from formula import parse_formula

def make_periodic_table():
    periodic_table_list = [
        # [symbol, name, atomic_mass]
        ['Na', 'Sodium', 22.98976928],
        ["Ac", 	"Actinium",227],
        ['Sb', 'Antimony', 121.76],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ['Ar', 'Argon', 39.948],
        ['As', 'Arsenic', 74.9216],
        ['At', 'Astatine', 210],
        ['Ba', 'Barium', 137.327],
        ['Be', 'Beryllium', 9.012182],
        ['Bi', 'Bismuth', 208.9804],
        ['B', 'Boron', 10.811],
        ['Br', 'Bromine', 79.904],
        ['Cd', 'Cadmium', 112.411],
        ['Ca', 'Calcium', 40.078],
        ['C', 'Carbon', 12.0107],
        ['Ce', 'Cerium', 140.116],
        ['Cs', 'Cesium', 132.9054519],
        ['Cl', 'Chlorine', 35.453],
        ['Cr', 'Chromium', 51.9961],
        ['Co', 'Cobalt', 58.933195],
        ['Cu', 'Copper', 63.546],
        ['Dy', 'Dysprosium', 162.5],
        ['Er', 'Erbium', 167.259],
        ['Eu', 'Europium', 151.964],
        ['F', 'Fluorine', 18.9984032],
        ['Fr', 'Francium', 223],
        ['Gd', 'Gadolinium', 157.25],
        ['Ga', 'Gallium', 69.723],
        ['Ge', 'Germanium', 72.64],
        ['Au', 'Gold', 196.966569],
        ['Hf', 'Hafnium', 178.49],
        ['He', 'Helium', 4.002602],
        ['Ho', 'Holmium', 164.93032],
        ['H', 'Hydrogen', 1.00794],
        ['In', 'Indium', 114.818],
        ['I', 'Iodine', 126.90447],
        ['Ir', 'Iridium', 192.217],
        ['Fe', 'Iron', 55.845],
        ['Kr', 'Krypton', 83.798],
        ['La', 'Lanthanum', 138.90547],
        ['Pb', 'Lead', 207.2],
        ['Li', 'Lithium', 6.941],
        ['Lu', 'Lutetium', 174.9668],
        ['Mg', 'Magnesium', 24.305],
        ['Mn', 'Manganese', 54.938045],
        ['Hg', 'Mercury', 200.59],
        ['Mo', 'Molybdenum', 95.96],
        ['Nd', 'Neodymium', 144.242],
        ['Ne', 'Neon', 20.1797],
        ['Np', 'Neptunium', 237],
        ['Ni', 'Nickel', 58.6934],
        ['Nb', 'Niobium', 92.90638],
        ['N', 'Nitrogen', 14.0067],
        ['Os', 'Osmium', 190.23],
        ['O', 'Oxygen', 15.9994],
        ['Pd', 'Palladium', 106.42],
        ['P', 'Phosphorus', 30.973762],
        ['Pt', 'Platinum', 195.084],
        ['Pu', 'Plutonium', 244],
        ['Po', 'Polonium', 209],
        ['K', 'Potassium', 39.0983],
        ['Pr', 'Praseodymium', 140.90765],
        ['Pm', 'Promethium', 145],
        ['Pa', 'Protactinium', 231.03588],
        ['Ra', 'Radium', 226],
        ['Rn', 'Radon', 222],
        ['Re', 'Rhenium', 186.207],
        ['Rh', 'Rhodium', 102.9055],
        ['Rb', 'Rubidium', 85.4678],
        ['Ru', 'Ruthenium', 101.07],
        ['Sm', 'Samarium', 150.36],
        ['Sc', 'Scandium', 44.955912],
        ['Se', 'Selenium', 78.96],
        ['Si', 'Silicon', 28.0855],
        ['Sr', 'Strontium', 87.62],
        ['S', 'Sulfur', 32.065],
        ['Ta', 'Tantalum', 180.94788],
        ['Tc', 'Technetium', 98],
        ['Te', 'Tellurium', 127.6],
        ['Tb', 'Terbium', 158.92535],
        ['Tl', 'Thallium', 204.3833],
        ['Th', 'Thorium', 232.03806],
        ['Tm', 'Thulium', 168.93421],
        ['Sn', 'Tin', 118.71],
        ['Ti', 'Titanium', 47.867],
        ['W', 'Tungsten', 183.84],
        ['U', 'Uranium', 238.02891],
        ['V', 'Vanadium', 50.9415],
        ['Xe', 'Xenon', 131.293],
        ['Yb', 'Ytterbium', 173.054],
        ['Y', 'Yttrium', 88.90585],
        ['Zn', 'Zinc', 65.38],
        ['Zr', 'Zirconium', 91.224],
    ]
    periodic_table_dict = {}
    for element in periodic_table_list:
        periodic_table_dict[element[0]] = {'name': element[NAME_INDEX], 'atomic_mass': element[ATOMIC_MASS_INDEX]}
    return periodic_table_dict

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_molar_mass = 0.0

    for element_info in symbol_quantity_list:
        symbol = element_info[SYMBOL_INDEX]
        quantity = element_info[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol]
        element_molar_mass = atomic_mass["atomic_mass"] * quantity

        total_molar_mass += element_molar_mass
    
    return total_molar_mass




def main():
    formula = input("Enter the chemical formula of a molecule: ")
    mass = float(input("Enter the mass of the chemical sample in grams: "))
    periodic_table = make_periodic_table()
   
    symbol_quantity_list = parse_formula(formula, periodic_table)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    moles = mass / molar_mass

    print("Molar mass:", molar_mass)
    print("Number of moles:", moles)

# Call the main function
if __name__ == "__main__":
    main()
