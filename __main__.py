from WWURegistrationBot.regbot import run_bot_at_time
from WWURegistrationBot.user import User

if __name__ == "__main__":
    user = User()
    run_bot_at_time(user)
