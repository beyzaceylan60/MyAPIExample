from passlib.context import CryptContext

# bcrypt + passlib uyumlu ayar
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# bcrypt 72 byte limitine karşı güvenli truncate
def _normalize_password(password: str) -> str:
    return password[:72]


def hash_password(password: str) -> str:
    """
    Plain password'u bcrypt ile hashler
    """
    normalized = _normalize_password(password)
    return pwd_context.hash(normalized)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Kullanıcının girdiği şifre ile hash'i karşılaştırır
    """
    normalized = _normalize_password(plain_password)
    return pwd_context.verify(normalized, hashed_password)
