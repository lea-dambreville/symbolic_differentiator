## Goals For Furture Drafts: 
* Handle polynomials with subtraction and multiplication 

## Quick Overview 
The overall script is summarised in the last function called "poly_calc". 

The function parses a polynomial string, into a list of tuples which is then differentiated and finally reformated back to a polynomial string after differentation. 

As of now the script handles polynomials with addition only. 

## Going Through the code Line by Line 

**parse_superscript(poly_str) function** converts any superscript in the input from '²' to the classic '^2'. 
```python
def parse_supercript(poly_str):
    current_poly = poly_str
    for num in poly_str:
        if num in superscript_map:
            current_poly = current_poly.replace(num, f"^{superscript_map[num]}") 
    return current_poly
```
* `current_poly = poly_str` since python strings are immuatable (locked in memory), we need to create a working copy that is editable for our function to return
* `for num in poly_str` we iterate through the string passed in 
    * `if num in superscript_map` if the character we are iterating through `num` is a superscript character that can be found in our superscript_map dictionary then enter we enter the `if` block. 
        * `current_poly = current_poly.replace(num, f"{superscript_map[num]}")`replace that superscript with its normal script i.e '²' -> '2' by finding it's value in our superscript_map dictionary.
* `return current_poly` once the loop is finished we return the latest version of current_poly 

**parse_ploynomial(poly_str) function** turns a "human string" in standard format such as `12x^2 + 4` (no superscripts) into a computer friendly list of tuples to be used in the differentiation function. 

```python
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
```
*  `terms_raw = poly_str.replace(" ", "").split("+")` removes all spaces and cuts the string into pieces whever there is a `+`. If you input `12x^2 + 4` `terms_raw` becomes `['12x^2','4'].

* `for term in terms_raw` starts a sloop to inspect every term one by one

* `if "x^2 in term` checks if the term has a power ("$x^2")
  * `coeff, exp = term.splic("x^")` splics the string at the `x^`. For `12x^2`, `coeff` = `12` and `exp` = `2`.
  * `if coeff == "": coeff = 1` This handles cases like `x^2` where the "1" is invisible 
  * `parsed_terms.append((int(coeff), int(exp)))` converts the strings to integers and stores them as a pair (tuple).

* `elif "x" in term`: if there is no `^`, it check for a linear term like "3x".
  * `coeff = term.replace("x", "")` removes the `x`. It i was `5x` you would be left with 5.
  * `c = int(coeff) if coeff else 1`: If the user just typed `x`, the variable is empty, so it default the coefficient to `1`.
  * `parsed_terms.append((c, 1))` stores it as (c,1) because "x" is technically "x^1"

* `else` If there is no `x` at all, it's a constant like `4`
  * `parsed_terms.append((int(term), 0)): Stores it as a (number, 0) because constancts are effectively "x^0".

* `return parsed_terms` the function then returns the completed list of tuples - which is then refered to as "poly_list" in the next function "differentiate(poly_list)".

**differentiate(poly_list) function** is where the math happens.

```python
def differentiate(poly_list):
    derivative = []

    for coeff, exp in poly_list:
        if exp == 0:
            continue

        new_coeff = coeff * exp
        new_exp = exp - 1
        derivative.append((new_coeff, new_exp))

    return derivative
```
Just to reiterate the function is recieving a list of tuples such as `[(3,2), (4,1), (6,0)]` that represents `3x^2 + 4x + 6` as an arguement. 

* `derivative` we declare and empty list which will fill in and return later

* `for coeff, exp in poly_list` loops through our list of tuples

* `if exp == 0: continue` the derivative of a constant is "0" so we skip it entirely.

* `new_coeff = exp - 1` subtracts one from the power.

* `derivative.append((new_coeff, new_exp)) saves the new pair in the list we declared earlier.

**format_poly(derivative) function** takes a list of tuple and refomats it back to "human string" standard format for us. We use this to reformat you polynomial after it has been differentiated in our *differentiate(poly_list)* function.

```python
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
```

* `for c, e in dervative:` loop through the list of tuples 

  * `if not derivative: return "0"` if all terms were constants the result is just "0" i.e if the argument was an empty list return "0".

  * `if e == 0: terms.append(f"{c}")` if the new exponent is 0, just who the number e.g 5x^0 just becomes 5

  * `else: terms.append("f{c}x^{e})` for everything else, use the standard `^` notation

* `return " + ".join(terms)` glues all the pieces together with `+` signs in between and space on each side of the `+`. 

The **poly_calc(polystr) funcion** combines all the scipts logic together. 

```python
def poly_calc (poly_str):
    poly_list = parse_polynomial(poly_str)
    diff = differentiate(poly_list)
    return format_poly(diff)
```
It takes the polynomial in "human string" standard format and parses into a list of tuples using the `parse_polynomial(poly_str)` function which is then differentaties in the `differentiate(poly_list) `function and then reformated back to "human string" standard format by the function `fomat_poly(diff)` function which is what is returned. 
