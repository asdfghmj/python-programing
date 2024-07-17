# calculate stress and strain for all different cross section area all user input


def calculate_stress(load, area):
  """Calculates stress."""
  return load / area

def calculate_strain(stress, modulus_of_elasticity):
  """Calculates strain."""
  return stress / modulus_of_elasticity

def calculate_area(cross_section_type, dimensions):
  """Calculates area based on cross-section type."""
  if cross_section_type == "rectangle":
    width, height = dimensions
    return width * height
  elif cross_section_type == "circle":
    radius = dimensions[0]
    return 3.14159 * radius**2
  else:
    raise ValueError("Invalid cross-section type.")

def main():
  """caalculate_stress_and_strain function to calculate stress and strain."""
  modulus_of_elasticity = float(input("Enter modulus of elasticity (Pa): "))
  load = float(input("Enter applied load (N): "))

  cross_section_type = input("Enter cross-section type (rectangle or circle): ")
  if cross_section_type == "rectangle":
    width = float(input("Enter width (m): "))
    height = float(input("Enter height (m): "))
    dimensions = (width, height)
  elif cross_section_type == "circle":
    radius = float(input("Enter radius (m): "))
    dimensions = (radius,)
  else:
    print("Invalid cross-section type.")
    return

  area = calculate_area(cross_section_type, dimensions)
  stress = calculate_stress(load, area)
  strain = calculate_strain(stress, modulus_of_elasticity)

  print(f"Stress: {stress} Pa")
  print(f"Strain: {strain}")

if __name__ == "__main__":
  main()
