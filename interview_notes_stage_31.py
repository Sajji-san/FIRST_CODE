# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: InterviewNotes
class ProfileManager:
            def __init__(self):
                self.active_profile_id = None
                self.profiles = {}

            def add_profile(self, name, email, phone=None):
                profile_id = len(self.profiles) + 1
                self.profiles[profile_id] = {
                    'id': profile_id,
                    'name': name,
                    'email': email,
                    'phone': phone
                }
                return profile_id

            def set_active_profile(self, profile_id):
                if profile_id not in self.profiles:
                    raise ValueError(f"Профиль с ID {profile_id} не существует")
                self.active_profile_id = profile_id

            def get_active_profile(self):
                if self.active_profile_id is None or self.active_profile_id not in self.profiles:
                    return None
                return self.profiles[self.active_profile_id]

            def list_profiles(self):
                return list(self.profiles.values())

            def remove_profile(self, profile_id):
                if self.active_profile_id == profile_id:
                    raise ValueError("Нельзя удалить активный профиль")
                del self.profiles[profile_id]
