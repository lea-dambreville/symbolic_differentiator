superscript_map = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'
}

poly_str = input("Please input in a univariate polynomial: ")

# parse_superscript 
def parse_supercript(poly_str):
    current_poly = poly_str
    for num in poly_str:
        if num in superscript_map:
            current_poly = current_poly.replace(num, f"^{superscript_map[num]}") #current_poly.replace() because you want to keep updating
    return current_poly # if the if condition returns "None" (there is not superscript) then return the original poly_str

def parse_polynomial(poly_str):
    terms_raw = poly_str.replace(" ", "").split("+")
    parsed_terms = []

    for term in terms_raw:
        if "x^" in term:
            coeff, exp = term.split("x^")
            if coeff == "":
                coeff = 1
            parsed_terms.append((int(coeff), int(exp)))

        elif "x" in term:
            coeff = term.replace("x", "")
            c = int(coeff) if coeff else 1
            parsed_terms.append((c, 1))

        else:
            parsed_terms.append((int(term), 0))

    return parsed_terms # i.e poly_list

def differentiate(poly_list):
    derivative = []

    for coeff, exp in poly_list:
        if exp == 0:
            continue

        new_coeff = coeff * exp
        new_exp = exp - 1
        derivative.append((new_coeff, new_exp))

    return derivative


def format_poly(derivative):
    if not derivative: return "0"
    terms = []
    for c, e in derivative:
        if e == 0:
            terms.append(f"{c}")
        elif e == 1:
            terms.append(f"{c}x")
        else:
            terms.append(
                f"{c}x^{e}")

    return " + ".join(terms)

def poly_calc (poly_str):
    string_poly = parse_supercript(poly_str)
    poly_list = parse_polynomial(string_poly)
    diff = differentiate(poly_list)
    return format_poly(diff)



print(poly_calc(poly_str))
