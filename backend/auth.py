from passlib.context import CryptContext

pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")


# deprecated="auto" → Passlib will automatically mark older algorithms as deprecated when you add newer ones.
# Example: if you configure both sha256_crypt and bcrypt, Passlib will prefer bcrypt for new hashes and treat sha256_crypt as deprecated.

# deprecated=True → Explicitly mark a scheme as deprecated. It will still verify old hashes but won’t be used for new ones.

def hash_password(old_password):
    return pwd.hash(old_password)

def verify_password(plain_password,hashed_password):
    return pwd.verify(plain_password,hashed_password)


