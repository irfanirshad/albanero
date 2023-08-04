def check(exp: bool, err_mssg: str, msg2: str = "Out of range") -> None:
    if not exp:
        print(f"Type failure: {err_mssg} {msg2}")
        # Normally you'd use assert to throw an exception..
        