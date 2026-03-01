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
    poly_list = parse_polynomial(poly_str)
    diff = differentiate(poly_list)
    return format_poly(diff)


print(poly_calc("12x^2 + 3x + 5x^4 + 4"))
print(poly_calc("x^2 + 6x + 10"))