def calculate_stress(material_properties, load):
    modulus_of_elasticity = material_properties['modulus_of_elasticity']
    beam_width = material_properties['beam_width']
    beam_height = material_properties['beam_height']

    area = beam_width * beam_height
    stress = load / area

    return stress

def calculate_strain(stress, material_properties):
    modulus_of_elasticity = material_properties['modulus_of_elasticity']

    strain = stress / modulus_of_elasticity

    return strain

def main():
    material_properties = {
        'modulus_of_elasticity': 200e9,  # Young's modulus in Pa
        'beam_width': 0.1,  # Width of the beam in meters
        'beam_height': 0.2  # Height of the beam in meters
    }

    load = 1000  # Applied load in Newtons

    stress = calculate_stress(material_properties, load)
    strain = calculate_strain(stress, material_properties)

    print(f"Stress: {stress} Pa")
    print(f"Strain: {strain}")

if __name__ == "__main__":
    main()
