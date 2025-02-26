import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Leer las contraseñas del archivo
    try:
        with open('top-10000-passwords.txt', 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return "Error: Password file not found"

    # Si use_salts es True, leer las sales
    salts = []
    if use_salts:
        try:
            with open('known-salts.txt', 'r') as f:
                salts = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return "Error: Salts file not found"

    # Probar cada contraseña
    for password in passwords:
        # Caso sin sales
        if not use_salts:
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
            if hashed == hash:
                return password
        # Caso con sales
        else:
            # Probar cada combinación de prepend y append para cada sal
            for salt in salts:
                # Prepend (sal + contraseña)
                prepended = salt + password
                hashed_prepend = hashlib.sha1(prepended.encode('utf-8')).hexdigest()
                if hashed_prepend == hash:
                    return password
                
                # Append (contraseña + sal)
                appended = password + salt
                hashed_append = hashlib.sha1(appended.encode('utf-8')).hexdigest()
                if hashed_append == hash:
                    return password

    # Si no se encuentra coincidencia
    return "PASSWORD NOT IN DATABASE"