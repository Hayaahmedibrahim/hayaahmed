#haia mohamed 748007157

def triangle_type_checker(side1, side2, side3):
    """
    Determine the type of triangle based on its three sides.

    Parameters:
        side1 (int): Length of the first side
        side2 (int): Length of the second side
        side3 (int): Length of the third side

    Returns:
        str: "Equilateral" if all sides are equal,
             "Isosceles" if only two sides are equal,
             "Scalene" if no sides are equal
    """
    # Check if all three sides are equal
    if side1 == side2 == side3:
        return "Equilateral"
    # Check if any two sides are equal
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"
    # If no sides are equal, it must be scalene
    else:
        return "Scalene"


def main():
    """
    Main function to get user input and return the type of triangle.

    Returns:
        str: The type of triangle (Equilateral, Isosceles, or Scalene)
    """
    # Prompt user for input of all three sides
    side1 = int(input("Enter length of side 1: "))
    side2 = int(input("Enter length of side 2: "))
    side3 = int(input("Enter length of side 3: "))

    # Call the triangle_type_checker function to determine triangle type
    triangle_type = triangle_type_checker(side1, side2, side3)

    # Return the result instead of printing directly
    return triangle_type


# Program execution starts here
# The result of main() is printed so the user sees the triangle type
main()
    
