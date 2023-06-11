import telebot
import instaloader

bot_token = "6188258787:AAGiGXVQCvmgL90VzHZUjumyyk9nhXtcxDU"
bot = telebot.TeleBot(bot_token)
loader = instaloader.Instaloader()
loader.login("danz.o3224", "passcodeee@2005*#")
print("Logged!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Instagram profile info bot!")
    bot.send_message(message.chat.id, "Please enter the Instagram username or link:")

# Author  
@bot.message_handler(commands=['author'])
def send_hello(message):
    bot.send_message(message.chat.id, "Instagram: https://instagram.com/response.200")
    bot.send_message(message.chat.id, "Website: https://lone1177.blogspot.com/")
    bot.send_message(message.chat.id, "Telegram Group: https://t.me/lonemods")
    
# MessageHandlingArea
@bot.message_handler(func=lambda message: True)
def fetch_instagram_profile(message):
    global username_input
    username_input = message.text
    username_input=username_input.lower()
    try:
    	username_input=username_input.replace("https://instagram.com/", "")
    	username_input=username_input.replace("https://instagram.com/", "")
    	username_input=username_input.rsplit("?")
    	username_input=username_input[0]
    	username_input=username_input
    except:
    	username_input=username_input
    profile = get_user_info(username_input)
    try:
        bot.send_message(message.chat.id, f"Name: {profile.full_name}")
        bot.send_message(message.chat.id, f"Biography: {profile.biography}")
        bot.send_message(message.chat.id, f"Private: {profile.is_private}")
        bot.send_message(message.chat.id, f"Verified: {profile.is_verified}")
        bot.send_message(message.chat.id, f"Business account: {profile.is_business_account}")
        bot.send_message(message.chat.id, f"Profile Link: {profile.profile_pic_url}")
        bot.send_message(message.chat.id, f"Bio Link: {profile.external_url}")
        bot.send_message(message.chat.id, f"Follower Count: {profile.followers}")
        bot.send_message(message.chat.id, f"Follower Count: {profile.followers}")
    except:
        bot.send_message(message.chat.id, "Invalid Instagram username or profile does not exist.")

def get_user_info(username):
    try:
        x="Searched user:{}\n".format(username_input)
        with open("user.txt", "a+") as f:
        	f.write(str(x))
        print(x)
        profile = instaloader.Profile.from_username(loader.context, username)
        return profile
    except instaloader.exceptions.InvalidArgumentException:
        return None
    except instaloader.exceptions.ProfileNotExistsException:
        return None
    except instaloader.exceptions.BadCredentialsException:
        return None

bot.polling(non_stop=True)
