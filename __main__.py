from src.regbot import run_bot_at_time
from src.user import User

if __name__ == "__main__":
    user = User()
    run_bot_at_time(user)