def is_leap(year):
    """
    Determina se um ano é bissexto de acordo com o calendário gregoriano.

    A regra considera:
    - O ano deve ser divisível por 4.
    - Se for divisível por 100, NÃO é bissexto, a menos que...
    - Também seja divisível por 400.

    Args:
        year (int): O ano a ser verificado.

    Returns:
        bool: True se for bissexto, False caso contrário.
    """
    leap = False

    if year % 4 == 0:
        leap = True

        if year % 100 == 0:
            leap = False

            if year % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))
