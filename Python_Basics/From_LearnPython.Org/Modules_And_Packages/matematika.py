def faktorial(angka: int) -> int:
    """An integer function to caculate a factorial number. The argument number must be higher than 0!"""
    if angka <= 0:
        raise ValueError(f"Error expected the argument to be higher than 0. Got {angka}")