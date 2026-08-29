# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: InterviewNotes
class UserManager:
    _profiles = {}
    _current_profile = None

    @classmethod
    def add_profile(cls, name, email="", phone="", role="candidate") -> dict:
        cls._profiles[name] = {"name": name, "email": email, "phone": phone, "role": role}
        cls._current_profile = name
        return cls._profiles[name]

    @classmethod
    def switch_profile(cls, name: str) -> dict | None:
        if name not in cls._profiles:
            raise ValueError(f"Profile '{name}' not found")
        cls._current_profile = name
        return cls._profiles[name]

    @classmethod
    def get_current(cls) -> dict | None:
        return cls._profiles.get(cls._current_profile) if cls._current_profile else None

    @classmethod
    def list_profiles(cls) -> dict:
        return cls._profiles
