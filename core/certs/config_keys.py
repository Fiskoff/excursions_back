from pathlib import Path
from pydantic import BaseModel


class AuthJWT(BaseModel):
    private_key: str
    public_key: str
    algorithm: str

    @classmethod
    def load_from_files(cls, private_key_path, public_key_path, algorithm="RS256"):
        with open(private_key_path, 'r') as private_file, open(public_key_path, 'r') as public_file:
            private_key = private_file.read()
            public_key = public_file.read()
        return cls(private_key=private_key, public_key=public_key, algorithm=algorithm)


base_dir = Path(__file__).resolve().parent
jwt_private_path = base_dir / "jwt-private.pem"
jwt_public_path = base_dir / "jwt-public.pem"

auth_jwt = AuthJWT.load_from_files(jwt_private_path, jwt_public_path)
