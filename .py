# vibe_checker_9000_extreme.py
# 💻✨ Vibe Checker 9000: Chaotic Deluxe Edition ✨💻
# made with love, memes, and a questionable sleep schedule 💖

import random
import time
import datetime


# 🌀 The sacred scrolls of vibes, chosen by the elders (aka me at 2am)
vibes = [
    "💅 Slay Queen Energy 💅",
    "😭 Existential Dread but Make it Fashion 😭",
    "🔥 Hot Girl Coding Summer 🔥",
    "👻 Ghosting Responsibilities 👻",
    "🌈 Main Character Moment 🌈",
    "🧃 Just Vibing, No Thoughts 🧃",
    "🤡 Clown Mode Activated 🤡",
    "🥹 Healing, Growing, and Blocking My Ex 🥹"
]

# ✨ Little digital pep talks for the soul ✨
quotes = [
    "✨ You are the sparkle in the debugging process ✨",
    "🚀 Don’t quit — you’re literally built different 🚀",
    "🧠 Your brain has so many tabs open, but it’s still iconic 🧠",
    "💖 Drink water. You’re 99% hot girl and 1% hydration 💖",
    "💻 If the code crashes, crash with style 💅"
]

# 🌧️ Fake weather because real weather is too chaotic
weather_moods = [
    "☀️ Sunny with a chance of slay ☀️",
    "🌧️ Rainy, but your drip is waterproof 🌧️",
    "🌬️ Windy and wildly iconic 🌬️",
    "❄️ Cold outside but your soul’s on fire ❄️"
]

# 🐸 For legal reasons, this part is emotional support
meme_animals = [
    "🐸 Kermit says: keep slayin'",
    "🦆 Duck with sunglasses approves your vibe",
    "🐱 Cat typing frantically... just like you",
    "🦄 Unicorn mode: enabled",
    "🐢 This turtle is vibing at its own speed and so are you"
]

def aesthetic_intro():
    # 💫 welcome screen that screams ✨aesthetic✨
    print("""
╔═════════════════════════════════╗
║  ✨ VIBE CHECKER 9000 DELUXE ✨ ║
╚═════════════════════════════════╝
    """)
    print("loading Gen-Z energy", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def scan_sequence(username):
    # 🧚‍♀️ pretend scanning for ~drama~ in your aura
    print(f"hi {username}! let's scan your chaotic aura 🌌")
    for _ in range(3):
        print("🔍 vibe scan in progress", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        print()
    print("✅ vibe successfully detected!")  # success!! you’re iconic.

def reveal_results():
    # 🎁 unwrap the digital tarot card of your current state
    vibe = random.choice(vibes)
    quote = random.choice(quotes)
    weather = random.choice(weather_moods)
    animal = random.choice(meme_animals)

    # ⏰ it’s giving timestamp realness
    now = datetime.datetime.now()
    timestamp = now.strftime("%A %I:%M %p")

    # 🪩 final results, served fresh
    print(f"\n🕒 it's {timestamp}, and here's your vibe report:")
    print(f"\n🔮 vibe: {vibe}")
    print(f"🌦️ weather mood: {weather}")
    print(f"💬 inspo: {quote}")
    print(f"{animal}")
    print("\n⚠️ warning: too much slayage detected ⚠️")

def main():
    aesthetic_intro()
    username = input("what’s your name bestie? 💖: ")  # yes i’m asking for your name. be polite.
    scan_sequence(username)
    reveal_results()
    print("\n🥰 remember: your vibe is unmatched. github can't even. 🥰")

# ✨ run the magic ✨
if __name__ == "__main__":
    main()

