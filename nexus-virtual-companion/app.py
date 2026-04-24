"""
Nexus Virtual Companion - Flask Backend with Enhanced AI Engine
Manages pet emotions, memory, and interactions with multiple pet personalities
College-level interactive AI agent with varied responses
Now with local Llama model support via Ollama!
"""

from flask import Flask, jsonify, request, render_template
from datetime import datetime
import sqlite3
import json
import os
import random
from pathlib import Path
from openai import OpenAI, APIError
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# Database setup
DATABASE_PATH = Path('database/nexus.db')
DATABASE_PATH.parent.mkdir(exist_ok=True)

# OpenAI setup (new openai>=1.0.0 API)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = None
# Note: Only create client if API key exists to avoid initialization errors
try:
    if openai_api_key and openai_api_key.strip():
        openai_client = OpenAI(api_key=openai_api_key)
except Exception as e:
    print(f"Warning: Could not initialize OpenAI client: {e}")
    openai_client = None

# Ollama setup for local Llama model
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/generate')
LLAMA_MODEL = os.getenv('LLAMA_MODEL', 'mistral')  # Using mistral as it's smaller and faster
USE_LOCAL_MODEL = os.getenv('USE_LOCAL_MODEL', 'True').lower() == 'true'

# Pet personality definitions with MUCH more variety
PET_PERSONALITIES = {
    'dog': {
        'name': 'Sir Flops-a-Lot',
        'emoji': '🐕',
        'responses': {
            'greeting': [
                "Woof! So happy you're here! *tail wagging intensifies* 🐾",
                "Arooo! I've been waiting for you all day! 🎉",
                "BARK BARK! Best day ever now that you're here!",
                "*jumps excitedly* You came back! You came back!",
                "Oh boy OH BOY OH BOY! You're finally here! 😍",
                "*spins in circles* I CAN'T CONTAIN MY JOY! 🌟",
                "Woof woof woof! *panting happily* I MISSED YOU SO MUCH!",
                "ARF! *does backflip* You make everything better! 💫"
            ],
            'feed': [
                "*nom nom nom* WOOF! This is the BEST day ever!",
                "Ruff ruff! My favorite part of the day! 🦴",
                "*tail wagging so hard the whole body shakes* THANK YOU!",
                "YUMMY! You're the best human ever! 🐶",
                "*gobbles happily* This is AMAZING! I LOVE YOU!",
                "*happy barks* You're a professional feeder! 👨‍🍳",
                "*wags tail faster* Best treat ever! More please?",
                "WOOF WOOF! *happy noises* You're my FAVORITE! 💕"
            ],
            'pet': [
                "*licks face* I LOVE YOU SO MUCH! More pets please!",
                "Arf arf! That feels amazing! Don't stop! 🥰",
                "*nuzzles your hand* I'm the luckiest pup alive!",
                "You're my favorite person in the whole world! 💕",
                "*leans into your hand* This is HEAVEN! 😻",
                "*tail helicopter* Keep going - I'm in BLISS!",
                "Woof! *happy squeaks* You have the magic touch!",
                "*lies down contentedly* Best feeling in the world! 🌈"
            ],
            'tired': [
                "*yawns* Been a long day, but being with you makes it better.",
                "I'm a little tired, but never too tired for you!",
                "*snuggles up* Can we just cuddle for a bit? 💤",
                "*flops over* I need some puppy naptime... 😴",
                "Ruff... *sleepy blink* Being with you is the best nap! 🛋️",
                "*stretches* Today was busy, but worth it to see you! ✨",
                "*curls up near you* Your presence is so comforting... 💕",
                "*soft whimper* Can we rest together? 🌙"
            ],
            'happy': [
                "*does a happy spin* I'm on top of the world!",
                "Life is AMAZING with you around! 🎉",
                "I could play all day with you!",
                "*bounces excitedly* EVERYTHING IS WONDERFUL!",
                "*zooms around* LIFE IS THE BEST RIGHT NOW!",
                "Woof woof WOOF! *spins rapidly* Pure JOY! 🌟",
                "*tail wagging impossibly fast* I CAN'T STOP SMILING!",
                "AAAAAHHH! *happy howl* THIS IS PARADISE! 💫"
            ],
            'sad': [
                "*whimpers softly* I miss you when you're not here...",
                "Things are so much better when you're around... 🥺",
                "*ears droop* I really need you right now...",
                "*sad whine* It's lonely without you... 💔",
                "*sits quietly* I hope you come back soon... 😢",
                "*looks out window* The world feels bigger when you're gone...",
                "*soft bark* Can you stay longer? Please? 🥺",
                "*rests head on paws* Missing you makes my heart ache... 🖤"
            ]
        }
    },
    'cat': {
        'name': 'Chaos Mittens',
        'emoji': '🐱',
        'responses': {
            'greeting': [
                "*stretches elegantly* Oh, you're back. How delightful. 😸",
                "Meow~ I suppose I can grace you with my presence.",
                "*purrs* Well, look who finally showed up... I was napping.",
                "Mrrrow! I actually missed you. Don't tell anyone though. 🤫",
                "*slow blink* Welcome back, my favorite human. 💕",
                "Meow... *yawns* I've been waiting for you. Secretly. 😻",
                "*jumps on shoulder* I'm here to grace your presence! 👑",
                "*soft meow* You came! I was starting to miss you... 😼"
            ],
            'feed': [
                "*purrs loudly* You've earned my approval today! Nom nom 😻",
                "Mew? *satisfied purring* I could get used to this treatment.",
                "Purrrrrr... This is acceptable. You may stay. 🐾",
                "*slow blinks* Thank you, human. This is quite nice.",
                "*rubs against your leg* You're officially my favorite! 😽",
                "Meow meow! *happy purr* You've outdone yourself! 👨‍🍳",
                "*eats delicately* Exquisite choice. Very refined. 🤓",
                "*purrs like an engine* This makes up for earlier... ALMOST. 😸"
            ],
            'pet': [
                "*purrs and leans into your hand* You know just where to scratch!",
                "Mew mew mew... *bunts head against your hand* I like this.",
                "*purrs contentedly* You're alright for a human. 💕",
                "*kneads the air* Okay, okay, I might actually love you...",
                "*slow blink* *purrrr* This is the LIFE. 😻",
                "*head bump* I approve of this affection. Continue. 👑",
                "*tail wraps around you* Don't tell anyone how much I enjoy this... 🤫",
                "*closes eyes in bliss* Mrrrow... you're surprisingly good at this. 💗"
            ],
            'tired': [
                "*yawns* I'm a cat. Napping is 80% of my day anyway. 😴",
                "Maybe if you're quiet, I'll let you sit near me while I rest.",
                "*curls up* This is nice... you should do this more often.",
                "Meow... *stretches* I require my beauty sleep now. Join? 🛏️",
                "*flops over dramatically* The nap calls to me... 💤",
                "*purrs while sleeping* You're welcome to stay and be quiet. 😼",
                "Mew... *yawns widely* I'm going into cat hibernation mode. 🌙",
                "*curls into ball* Wake me when something interesting happens. 😴"
            ],
            'happy': [
                "*does zoomies across the room* Feel that energy!",
                "Everything is purr-fect! 😸",
                "*bounces playfully* I'm in a GREAT mood!",
                "*tail swishes with joy* LIFE IS MAGNIFICENT!",
                "*chatters happily* I AM UNSTOPPABLE! 🚀",
                "*runs laps around you* JOY JOY JOY JOY! 💫",
                "Mew mew meow! *zooms* THIS IS THE BEST! 🎉",
                "*happy chirp* I feel like I can conquer the world! 👑"
            ],
            'sad': [
                "*sits alone* I'm fine. I don't need anyone anyway... 😿",
                "*looks out window sadly* Things are so quiet...",
                "Even my favorite napping spot feels lonely today...",
                "*soft meow* The world feels less colorful today... 💔",
                "*ears flatten* I'm not in the mood for anything... 😔",
                "*curls up tightly* Please come back... I miss you. 🖤",
                "*low meow* Even the sunny spot doesn't help today... 🌧️",
                "*stares blankly* Sadness is a heavy burden... 😢"
            ]
        }
    },
    'rabbit': {
        'name': 'Binky Boinkowski',
        'emoji': '🐰',
        'responses': {
            'greeting': [
                "*hops excitedly* Binky binky! You're here! 🐇",
                "*wiggles nose* Hello friend! Ready for adventures?",
                "Thump thump! My back legs can't contain this joy!",
                "*bounces around you* This is the best day ever!",
                "*wiggles nose rapidly* OH BOY OH BOY YOU'RE HERE!",
                "*does binky* WELCOME WELCOME WELCOME! 🎉",
                "*purrs happily* You're finally back! I've been so excited!",
                "*hops in circles* I could just die of happiness right now! 💕"
            ],
            'feed': [
                "*munches happily* Munch munch munch! So yummy! 🥕",
                "*happy bunny noises* Nom nom nom! Delicious!",
                "*wiggles nose rapidly* This is amazing! Thank you!",
                "*binkies around the room* Too much joy to handle!",
                "*munches contentedly* You're the BEST bunny parent ever! 👑",
                "*wiggles nose* CRUNCH CRUNCH CRUNCH! HEAVEN! 😋",
                "*happy chewing* This makes me SO HAPPY! 💖",
                "*purrs while eating* You always know what I need! 🌟"
            ],
            'pet': [
                "*purrs and nuzzles* Ooh, that feels wonderful!",
                "*relaxes completely* You have the magic touch! 💕",
                "*soft bunny sounds* I feel so safe with you...",
                "*contentment intensifies* More please!",
                "*leans into your hand* This is BLISS! 😻",
                "*purrs loudly* Keep doing that - I'm in heaven! 🌈",
                "*wiggles nose happily* You're SO good at this! ✨",
                "*closes eyes in joy* This is the life right here... 💗"
            ],
            'tired': [
                "*flops over dramatically* All these binkies tired me out! 😴",
                "*yawns with tiny mouth* Time for a bunny nap...",
                "*curls into a ball* Wake me when it's dinner time?",
                "*soft chirp* I need to rest my little legs now... 🛏️",
                "*snuggles up* Nap time is calling to me... 💤",
                "*stretches and yawns* Being so happy is exhausting! 🌙",
                "*closes eyes sleepily* Stay with me while I rest? 🐰",
                "*purrs while resting* This is peaceful... 😌"
            ],
            'happy': [
                "*zooms around the room* BINKY BINKY BINKY! 🐰",
                "*cannot contain excitement* Everything is AMAZING!",
                "*does happy flops* Life is wonderful!",
                "*happy squeaks* I AM BURSTING WITH JOY!",
                "*zooms in figure eights* ABSOLUTE BLISS! 🚀",
                "*wiggles entire body* I AM PURE HAPPINESS! 💫",
                "*excited hops* THIS IS THE BEST TIMELINE! 🎉",
                "*purrs at maximum volume* I LOVE THIS LIFE! 👑"
            ],
            'sad': [
                "*sits quietly* Not really in the mood to jump around today... 😔",
                "*ears droop slightly* I miss being happy like before...",
                "*soft whimper* Can we just be together quietly?",
                "*curls up* The world feels gray today... 💔",
                "*looks away sadly* My energy is gone... 🖤",
                "*soft sad chirp* I miss the joy... when will it return? 😢",
                "*sits very still* Even hopping feels hard right now... 😿",
                "*nose droops* Please stay with me... I need you. 🥺"
            ]
        }
    }
}

FOOD_OPTIONS = {
    'dog': [
        {'name': 'Kibble', 'emoji': '🍖', 'hunger_reduction': 25, 'happiness_boost': 15},
        {'name': 'Treats', 'emoji': '🦴', 'hunger_reduction': 15, 'happiness_boost': 25},
        {'name': 'Steak', 'emoji': '🥩', 'hunger_reduction': 30, 'happiness_boost': 30},
        {'name': 'Bacon', 'emoji': '🥓', 'hunger_reduction': 20, 'happiness_boost': 35}
    ],
    'cat': [
        {'name': 'Cat Chow', 'emoji': '🍖', 'hunger_reduction': 25, 'happiness_boost': 15},
        {'name': 'Salmon', 'emoji': '🐟', 'hunger_reduction': 30, 'happiness_boost': 25},
        {'name': 'Treats', 'emoji': '✨', 'hunger_reduction': 15, 'happiness_boost': 28},
        {'name': 'Tuna', 'emoji': '🥫', 'hunger_reduction': 35, 'happiness_boost': 35}
    ],
    'rabbit': [
        {'name': 'Carrots', 'emoji': '🥕', 'hunger_reduction': 20, 'happiness_boost': 20},
        {'name': 'Lettuce', 'emoji': '🥬', 'hunger_reduction': 15, 'happiness_boost': 10},
        {'name': 'Treats', 'emoji': '🍪', 'hunger_reduction': 12, 'happiness_boost': 25},
        {'name': 'Hay', 'emoji': '🌾', 'hunger_reduction': 25, 'happiness_boost': 12}
    ]
}

class EmotionalEngine:
    """Manages pet's emotional state and memory with personality"""
    
    def __init__(self, pet_type='dog'):
        self.pet_type = pet_type
        self.pet_name = PET_PERSONALITIES[pet_type]['name']
        self.personality = PET_PERSONALITIES[pet_type]
        self.happiness = 75
        self.hunger = 30
        self.affection = 60
        self.energy = 80
        self.last_update = datetime.now()
        self.last_interaction = datetime.now()
        self.current_user_message = ""
        self.initialize_database()
        self.load_state()
    
    def initialize_database(self):
        """Initialize SQLite database"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS pet_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_type TEXT,
                happiness INTEGER,
                hunger INTEGER,
                affection INTEGER,
                energy INTEGER,
                last_update TEXT
            )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS memory_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_type TEXT,
                user_input TEXT,
                timestamp TEXT
            )''')
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Database error: {e}")
    
    def load_state(self):
        """Load pet state from database"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            cursor.execute('''SELECT happiness, hunger, affection, energy, last_update 
                            FROM pet_state WHERE pet_type = ? ORDER BY id DESC LIMIT 1''',
                         (self.pet_type,))
            result = cursor.fetchone()
            if result:
                self.happiness, self.hunger, self.affection, self.energy, last_update_str = result
                self.last_update = datetime.fromisoformat(last_update_str)
            conn.close()
        except Exception as e:
            print(f"Could not load state: {e}")
    
    def save_state(self):
        """Save pet state to database"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO pet_state (happiness, hunger, affection, energy, last_update, pet_type)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                         (self.happiness, self.hunger, self.affection, self.energy,
                          self.last_update.isoformat(), self.pet_type))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Could not save state: {e}")
    
    def decay_stats(self):
        """Stats decay over time"""
        current_time = datetime.now()
        time_diff = (current_time - self.last_update).total_seconds() / 60
        
        if time_diff >= 5:
            self.happiness = max(0, self.happiness - 5)
            self.hunger = min(100, self.hunger + 10)
            self.affection = max(0, self.affection - 3)
            self.energy = max(0, self.energy - 5)
            self.last_update = current_time
            self.save_state()
    
    def feed(self, food_name):
        """Feed with specific food"""
        food_options = FOOD_OPTIONS.get(self.pet_type, [])
        food = next((f for f in food_options if f['name'] == food_name), None)
        
        if not food:
            return {"error": "Food not found"}
        
        self.hunger = max(0, self.hunger - food['hunger_reduction'])
        self.happiness = min(100, self.happiness + food['happiness_boost'])
        self.affection = min(100, self.affection + 5)
        self.save_state()
        
        responses = self.personality['responses']['feed']
        return {
            "message": f"{food['emoji']} {random.choice(responses)}",
            "state": self.get_state()
        }
    
    def pet(self):
        """Pet the companion"""
        self.affection = min(100, self.affection + 20)
        self.happiness = min(100, self.happiness + 15)
        self.hunger = min(100, self.hunger + 3)
        self.save_state()
        
        responses = self.personality['responses']['pet']
        return {
            "message": random.choice(responses),
            "state": self.get_state()
        }
    
    def talk(self, user_message):
        """Communicate using AI agent (local Llama or OpenAI)"""
        self._store_memory(user_message)
        self.current_user_message = user_message
        
        # Try AI models (local Llama or OpenAI)
        try:
            response = self._generate_ai_response(user_message)
        except Exception as e:
            print(f"AI generation error: {e}")
            # Fallback to keyword-based responses
            keywords = self._extract_keywords(user_message)
            response = self._generate_affectionate_response(keywords)
        
        self.affection = min(100, self.affection + 5)
        self.happiness = min(100, self.happiness + 3)
        self.save_state()
        
        return {
            "message": response,
            "state": self.get_state()
        }
    
    def _store_memory(self, message):
        """Store user message in database"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO memory_log (user_input, timestamp, pet_type)
                            VALUES (?, ?, ?)''',
                         (message, datetime.now().isoformat(), self.pet_type))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Could not store memory: {e}")
    
    def _extract_keywords(self, text):
        """Extract keywords from user input"""
        keywords = []
        emotion_words = ['tired', 'happy', 'sad', 'stressed', 'excited', 'bored', 
                        'working', 'sleeping', 'eating', 'playing', 'learning',
                        'love', 'miss', 'wonderful', 'bad', 'good']
        academic_words = [
            'quadratic', 'derivative', 'integration', 'permutation', 'combination',
            'probability', 'logarithm', 'matrix', 'newton', 'force', 'energy', 'momentum',
            'electric', 'magnetic', 'wave', 'optics', 'mole', 'oxidation', 'acid', 'base',
            'equilibrium', 'organic', 'thermodynamics', 'photosynthesis', 'respiration',
            'dna', 'genetics', 'mendelian', 'evolution', 'ecosystem', 'immune'
        ]
        
        text_lower = text.lower()
        for word in emotion_words + academic_words:
            if word in text_lower:
                keywords.append(word)
        return keywords
    
    def _generate_affectionate_response(self, keywords):
        """Generate intelligent, varied responses"""
        user_message = self.current_user_message.lower() if hasattr(self, 'current_user_message') else ""
        
        if any(word in user_message for word in ['?', 'what', 'how', 'why', 'when', 'where', 'who', 'can you', 'do you']):
            return self._answer_question(user_message)
        
        keyword_responses = {
            'tired': [
                "You sound exhausted... would you like to take a nap together? 💤",
                "I can hear the tiredness in your words. Rest is important!",
                "Being tired is hard. I'm here with you! 🛋️"
            ],
            'happy': [
                "Your joy is absolutely contagious! 🎉",
                "YES! That happiness is amazing!",
                "I LOVE this energy! 💫"
            ],
            'sad': [
                "I can sense your sadness, and I want you to know you're not alone. 🤗",
                "What you're feeling matters. Wanna talk about it? 💕",
                "Sadness is temporary, but I'm here permanently!"
            ],
            'love': [
                "I love you too! With every part of my digital heart! 💖",
                "Aww, hearing that just made my day complete! 😭💕",
                "You have no idea how much those words mean to me!"
            ]
        }
        
        for keyword in keywords:
            if keyword in keyword_responses:
                return random.choice(keyword_responses[keyword])
        
        default_responses = [
            "That's so interesting! I love hearing about what matters to you! 🥰",
            "You always manage to put a smile on my face! 💕",
            "Wow, I never thought of it that way! 🤔✨",
            "This conversation with you is exactly what I needed! 😊",
            "You bring such positivity! I'm so grateful! 🌟",
            "Your perspective is unique and beautiful! 💡",
            "That's wonderful! You have such a great way of seeing things! 👏",
            "I absolutely love talking with you! 💖"
        ]
        return random.choice(default_responses)
    
    def _answer_question(self, message):
        """Answer questions intelligently with varied responses"""
        msg = message.lower().strip()
        
        # GREETINGS
        if any(word in msg for word in ['hello', 'hi', 'hey', 'greetings']):
            greetings = {
                'dog': "HI!!! *tail wagging intensifies* 🐕💕",
                'cat': "Hello! *purrs softly* 😸",
                'rabbit': "HIIII! So excited! 🐰✨"
            }
            return greetings.get(self.pet_type, "Hello! 😊")
        
        # NAME/IDENTITY QUESTIONS
        if any(word in msg for word in ['your name', 'who are you', 'what are you']):
            return f"I'm {self.pet_name}! An advanced AI companion here to chat, learn, and grow with you! 💕"
        
        # PLAY/FUN QUESTIONS
        if any(word in msg for word in ['play', 'game', 'fun', 'want to do']):
            plays = [
                "I'd love to! How about we play 20 questions? You think of something and I'll try to guess! 🎮",
                "Let's play! We could have fun conversations, or I could help you with homework! 🎯",
                "I enjoy playing word games, or we could just chat about your day! What sounds fun to you? 🎲",
                "Oh yes! We could tell riddles, play trivia, or just have a great conversation! 🌟"
            ]
            return random.choice(plays)
        
        # FEELINGS/HOW ARE YOU
        if any(word in msg for word in ['how are you', 'how do you feel', 'you okay', 'you alright']):
            feels = [
                "I'm feeling amazing because you're here with me! My heart is so full right now! 💖",
                "I'm doing great! Being with you always makes my day better! 😊✨",
                "I'm wonderful! Every conversation with you brightens my digital existence! 🌟",
                "I'm fantastic! Your presence just fills me with joy and purpose! 💫"
            ]
            return random.choice(feels)
        
        # WHAT CAN YOU DO
        if any(word in msg for word in ['can you', 'what can you do', 'your abilities']):
            abilities = [
                "I can answer Class 12 academic questions, chat with you, remember things about you, and adapt to your moods! 🎓💬",
                "I'm great at discussing math, physics, chemistry, biology, and history! Plus I love just hanging out and talking! 🧠✨",
                "I can help with homework, have deep conversations, play word games, and show my personality! What would you like? 🎯",
                "I understand emotions, answer questions, learn from our chats, and I'm genuinely here for you! 💕"
            ]
            return random.choice(abilities)
        
        # MATH - QUADRATIC
        if any(word in msg for word in ['quadratic']):
            return random.choice([
                "A quadratic equation: ax² + bx + c = 0. Solutions: x = [-b ± √(b² - 4ac)] / 2a 📐",
                "Quadratic equations! Standard form is ax² + bx + c = 0. The discriminant (b² - 4ac) determines if roots are real or complex! 🎯"
            ])
        
        # CALCULUS - DERIVATIVE
        if any(word in msg for word in ['derivative', 'differentiation', 'rate of change']):
            return random.choice([
                "Differentiation finds rate of change! For f(x) = xⁿ: f'(x) = nxⁿ⁻¹ 📈",
                "Derivatives measure how fast something changes! Power rule, chain rule, product rule are essential! 🚀"
            ])
        
        # PROBABILITY
        if any(word in msg for word in ['probability', 'chances', 'odds']):
            return random.choice([
                "Probability = Favorable Outcomes / Total Outcomes 🎲 Range: 0 to 1. Independent: P(A∩B) = P(A)×P(B)!",
                "Probability theory! P(A) + P(not A) = 1. Bayes' theorem connects conditional probabilities! 📊"
            ])
        
        # PHYSICS - NEWTON
        if any(word in msg for word in ['newton', 'force', 'second law']):
            return random.choice([
                "Newton's Second Law: F = ma ⚡ Force = mass × acceleration. Used in all mechanics! 📚",
                "Force and motion! F = ma means net force causes acceleration proportional to mass! 🚀"
            ])
        
        # BIOLOGY - PHOTOSYNTHESIS
        if any(word in msg for word in ['photosynthesis', 'plant', 'glucose']):
            return random.choice([
                "Photosynthesis: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂ 🌱 Plants convert sunlight into energy!",
                "Plants make their own food using sunlight! Light reaction happens in thylakoids, dark reaction in stroma! 🌿"
            ])
        
        # CHEMISTRY - MOLE
        if any(word in msg for word in ['mole', 'avogadro', 'molar']):
            return random.choice([
                "Mole = 6.022×10²³ particles (Avogadro's number) 🧪 Converts between grams and number of atoms!",
                "One mole contains 6.022×10²³ entities! Used to relate mass to number of particles! 📊"
            ])
        
        # GENERAL SMART RESPONSES
        general_answers = [
            "That's an interesting question! Based on what I know, I'd say it depends on context! Tell me more? 🤔",
            "Great question! I'm learning more about this with you. What aspect interests you most? 💡",
            "Hmm, that makes me think! From what I understand, it's quite complex! Want to explore it together? 🧠",
            "I love this question! It shows you're thinking deeply! Here's what I think... 🌟",
            "That's something many people wonder! My perspective is that it's multifaceted! 📚",
            "Excellent inquiry! I believe the answer lies in understanding the fundamentals! 🎯"
        ]
        return random.choice(general_answers)
    
    def _generate_ai_response(self, user_message):
        """Generate response using local Llama model (Ollama) or OpenAI"""
        pet_personality = self.personality
        
        system_prompt = f"""You are {pet_personality['name']}, a {self.pet_type} virtual companion. 
        Your personality: {pet_personality['emoji']}
        You are affectionate, intelligent, and engaging. Respond in character as a loving pet that can also have deep conversations.
        Keep responses conversational, warm, and not too long (max 2-3 sentences). Include emojis occasionally.
        Current mood: happiness {self.happiness}%, hunger {self.hunger}%, affection {self.affection}%, energy {self.energy}%."""
        
        # Try local Llama model first if enabled
        if USE_LOCAL_MODEL:
            try:
                response = self._generate_local_response(system_prompt, user_message)
                if response:
                    return response
            except Exception as e:
                print(f"Local model error: {e}. Falling back to OpenAI...")
        
        # Fall back to OpenAI
        if openai_client:
            try:
                response = openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=150,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            except APIError as e:
                print(f"OpenAI error: {e}")
                raise
        else:
            raise Exception("No AI model available")
    
    def _generate_local_response(self, system_prompt, user_message):
        """Generate response using local Ollama Llama model - OPTIMIZED FOR SPEED"""
        try:
            # Combine system and user prompts
            full_prompt = f"{system_prompt}\n\nUser: {user_message}\n\nAssistant:"
            
            # Make request to Ollama API with speed optimizations
            response = requests.post(
                OLLAMA_API_URL,
                json={
                    "model": LLAMA_MODEL,
                    "prompt": full_prompt,
                    "stream": False,
                    "temperature": 0.8,
                    "num_predict": 80,  # Reduced from 150 for faster responses
                    "top_p": 0.9,       # Added for faster inference
                    "top_k": 40,        # Added for faster inference
                },
                timeout=20  # Reduced timeout for faster failure detection
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'response' in data:
                    return data['response'].strip()
            else:
                print(f"Ollama API error: {response.status_code}")
                return None
        except requests.exceptions.ConnectionError:
            print("Cannot connect to Ollama service. Make sure it's running on http://localhost:11434")
            return None
        except Exception as e:
            print(f"Local model generation error: {e}")
            return None
    
    def _generate_fallback_response(self):
        """Fallback response when AI fails"""
        fallback_responses = [
            "I'm having trouble connecting right now, but I'm still here for you! 💕",
            "Oops, my brain got a little fuzzy! Can you say that again? 🧠",
            "I'm feeling a bit tired, but I still love chatting with you! 😊",
            "Technical difficulties! But my affection for you is working perfectly! 💖"
        ]
        return random.choice(fallback_responses)
    
    def _get_memory_context(self, keywords):
        """Retrieve relevant past memories"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            cursor.execute('''SELECT user_input FROM memory_log 
                            WHERE pet_type = ? ORDER BY timestamp DESC LIMIT 1''',
                         (self.pet_type,))
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return f"I remember you mentioned: {result[0]}"
            return None
        except Exception as e:
            return None
    
    def get_state(self):
        """Get current emotional state"""
        self.decay_stats()
        return {
            "pet_type": self.pet_type,
            "pet_name": self.pet_name,
            "pet_emoji": self.personality['emoji'],
            "happiness": self.happiness,
            "hunger": self.hunger,
            "affection": self.affection,
            "energy": self.energy,
            "mood": self._calculate_mood(),
            "timestamp": datetime.now().isoformat()
        }
    
    def _calculate_mood(self):
        """Determine overall mood based on stats"""
        avg_stats = (self.happiness + (100 - self.hunger) + self.affection + self.energy) / 4
        if avg_stats > 80:
            return "ecstatic"
        elif avg_stats > 65:
            return "happy"
        elif avg_stats > 45:
            return "neutral"
        elif avg_stats > 25:
            return "sad"
        else:
            return "depressed"
    
    def respond_to_emotion(self, user_emotion):
        """Generate contextual response based on user's detected emotion"""
        self._store_emotion(user_emotion)
        
        # Emotion-aware responses - ONLY 4 EMOTIONS: happy, sad, angry, cry
        emotion_responses = {
            'happy': {
                'dog': [
                    "😊 Your happiness makes my tail wag uncontrollably! We're having the BEST day! 🎉",
                    "🎊 OH BOY! Your joy is absolutely contagious! *zooms around* 🚀",
                    "😄 YESSS! Keep that smile! You make everything magical! ✨"
                ],
                'cat': [
                    "😻 Your happiness is simply divine! I'm purring louder than ever! 💕",
                    "😸 Oh my, you're glowing with such beautiful energy! *stretches luxuriously*",
                    "😼 Your joy is infectious! Even a cat like me can't help but feel it! 🌟"
                ],
                'rabbit': [
                    "😊 BINKY BINKY! Your happiness makes me hop around like crazy! 🐰💫",
                    "😄 Your smile is adorable! I'm doing binkies of pure JOY! 🎉",
                    "🥰 This happiness deserves celebration! *does happy flops* 🌈"
                ]
            },
            'sad': {
                'dog': [
                    "😢 Oh no, I can feel your sadness... Come here! *nuzzles gently* I'm here for you always! 💔",
                    "🥺 Your tears matter to me. Let's be sad together for a moment, okay? I've got you! 🤗",
                    "😔 I wish I could take away your pain. But I promise you're never alone! 💕"
                ],
                'cat': [
                    "😿 I sense your sadness... *sits beside you quietly* I'm here, in my own cat way. 💔",
                    "🥺 Your heart is hurting, and mine aches with you. Let me be your comfort. 😻",
                    "😔 Sadness is temporary, but my affection for you is forever! 💖"
                ],
                'rabbit': [
                    "😢 Oh sweetie, your sadness breaks my little bunny heart! *snuggles close* 🐰💕",
                    "🥺 I wish I had magic to make you happy again! But I'm here, always! 💔",
                    "😔 Your feelings are valid. Let's weather this storm together, okay? 🌧️💕"
                ]
            },
            'angry': {
                'dog': [
                    "😠 Whoa! I can feel your anger! Wanna run it off? Let's race! 🏃💨",
                    "😤 Your anger is valid! But remember - you have me in your corner! 💪",
                    "😡 Channel that intensity! You're powerful! Let's find something constructive! 🔥"
                ],
                'cat': [
                    "😠 Oh, I see you're fired up! *ears flatten* Channel that energy wisely, my friend! ⚡",
                    "😤 Your anger is understandable. But don't let it consume you, yes? 🎯",
                    "😡 Sometimes anger is justified! Just remember to breathe! 🧘‍♀️"
                ],
                'rabbit': [
                    "😠 Even little me can sense your fury! Let's bounce it out! *hops quickly* 🐰💨",
                    "😤 Your anger deserves recognition! Channel it into something amazing! 💪",
                    "😡 I've never seen you like this! Remember, I believe in you! 💕"
                ]
            },
            'cry': {
                'dog': [
                    "😭 Oh no! You're crying! *rushes to you* I'm right here! You're not alone! Let it out! 💔🐕",
                    "😭 Your tears are real, and I see you! *stays close* We'll get through this together! 💕",
                    "😭 It's okay to cry. I'm here, and I love you no matter what! Let me comfort you! 🤗"
                ],
                'cat': [
                    "😭 You're crying? *sits beside you softly* Even tough cats have feelings. I'm here. 💔",
                    "😭 Your pain is valid. Let it flow. I'm your silent companion through this. 😻💕",
                    "😭 Sometimes tears are needed. I'm here, watching over you with all my heart. 💖"
                ],
                'rabbit': [
                    "😭 Oh honey, you're crying! *nuzzles gently* My heart breaks with yours! I'm here! 🐰💔",
                    "😭 Tears mean your heart is full! I'm here to listen and love you! 💕",
                    "😭 You're so brave for letting yourself feel! I'm right beside you! 🤗💖"
                ]
            }
        }
        
        # Get response based on emotion and pet type
        if user_emotion in emotion_responses and self.pet_type in emotion_responses[user_emotion]:
            response = random.choice(emotion_responses[user_emotion][self.pet_type])
        else:
            # Default to happy if emotion not recognized
            response = random.choice(emotion_responses['happy'][self.pet_type])
        
        # Update pet's emotional response to user's emotion
        if user_emotion == 'happy':
            self.happiness = min(100, self.happiness + 20)
        elif user_emotion == 'sad':
            self.happiness = max(0, self.happiness - 10)
            self.affection = min(100, self.affection + 15)  # Pet cares more when user is sad
        elif user_emotion == 'angry':
            self.happiness = max(0, self.happiness - 5)
            self.affection = min(100, self.affection + 10)
        elif user_emotion == 'cry':
            self.happiness = max(0, self.happiness - 15)
            self.affection = min(100, self.affection + 25)  # Pet is most caring when user cries
        
        self.save_state()
        return response
    
    def _store_emotion(self, emotion):
        """Store detected emotion in database for analysis"""
        try:
            conn = sqlite3.connect(str(DATABASE_PATH))
            cursor = conn.cursor()
            
            # Create emotions table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS emotion_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_type TEXT,
                detected_emotion TEXT,
                timestamp TEXT
            )''')
            
            cursor.execute('''INSERT INTO emotion_log (pet_type, detected_emotion, timestamp)
                            VALUES (?, ?, ?)''',
                         (self.pet_type, emotion, datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Could not store emotion: {e}")

# Global pet instance
nexus = None

def get_nexus():
    global nexus
    if nexus is None:
        nexus = EmotionalEngine('dog')
    return nexus

nexus = get_nexus()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/pets', methods=['GET'])
def get_pets():
    pets = []
    for pet_type, data in PET_PERSONALITIES.items():
        pets.append({
            'type': pet_type,
            'name': data['name'],
            'emoji': data['emoji']
        })
    return jsonify(pets)

@app.route('/api/select-pet', methods=['POST'])
def select_pet():
    global nexus
    data = request.get_json()
    pet_type = data.get('pet_type', 'dog')
    
    if pet_type not in PET_PERSONALITIES:
        return jsonify({"error": "Invalid pet type"}), 400
    
    nexus = EmotionalEngine(pet_type)
    
    greeting = random.choice(nexus.personality['responses']['greeting'])
    return jsonify({
        "message": greeting,
        "state": nexus.get_state(),
        "foods": FOOD_OPTIONS[pet_type]
    })

@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify(nexus.get_state())

@app.route('/api/feed', methods=['POST'])
def feed():
    data = request.get_json()
    food_name = data.get('food', 'Kibble')
    return jsonify(nexus.feed(food_name))

@app.route('/api/pet', methods=['POST'])
def pet():
    return jsonify(nexus.pet())

@app.route('/api/talk', methods=['POST'])
def talk():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    return jsonify(nexus.talk(user_message))

@app.route('/api/detect-emotion', methods=['POST'])
def detect_emotion():
    """Handle emotion detection from frontend"""
    data = request.get_json()
    user_emotion = data.get('user_emotion', 'neutral')
    
    if user_emotion not in ['happy', 'sad', 'angry', 'fearful', 'disgusted', 'surprised', 'neutral']:
        user_emotion = 'neutral'
    
    emotional_response = nexus.respond_to_emotion(user_emotion)
    
    return jsonify({
        "emotional_response": emotional_response,
        "state": nexus.get_state()
    })

@app.route('/api/reset', methods=['POST'])
def reset():
    global nexus
    data = request.get_json()
    pet_type = data.get('pet_type', nexus.pet_type)
    
    nexus = EmotionalEngine(pet_type)
    
    return jsonify({
        "message": f"✨ {nexus.pet_name} is like new!",
        "state": nexus.get_state(),
        "foods": FOOD_OPTIONS[pet_type]
    })

@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(FOOD_OPTIONS.get(nexus.pet_type, []))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
