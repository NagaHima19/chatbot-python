import random
import requests
import tkinter as tk
from tkinter import scrolledtext, StringVar

class EmotionDetector:
    @staticmethod
    def get_emotion(text):
        emotions = {
            'happy': ['happy','joy', 'excitement', 'cheerful', 'positive'],
            'sad': ['sad', 'lonely', 'depressed', 'Emotinal','frustated'],
            'calm': ['calm', 'peaceful', 'relaxed','sleepy'],
            'energetic': ['energetic','energy', 'excitement',  'upbeat']
        }

        for emotion, keywords in emotions.items():
            if any(keyword in text.lower() for keyword in keywords):
                return emotion

        return 'neutral'

class SongRecommender:
    @staticmethod
    def recommend_song(emotion):
        
        songs_by_emotion = {
            'happy': ['Love you Zindagi', 'Sooraj Dooba Hain', 'mera mann','the Humma','Gunghroo','Shubharambh','Muqabla','Chinni chinni asha','Kai love Chedugudu','Cham Cham','Main hoon na','Mast Magan','Jab tak','Gerua',],
            'sad': ['Tum Hi Ho', 'judaii', 'Hamari Adhuri kahani','Duaa','Tere Hawale','Channa Mereya','Main dhoondhne ko Zamane','Ae dil hei Mushkil','Humnava mere','kabira','tera yaar hu main','Bekhayali','karige loga','Adiga Adiga','Oosupodu','povadhe prema','Oke oka Jeevitam','oh prema','attu nuvve','Phir kabhi'],
            'calm': ['Tum se hi', 'Duniya', 'pal','Ik Vaari Aa','Samjhawan','Humsafar','Ranjha','Jeene laga hoon','zehnaseeb','Subhanallah','Jab se tere naina','Iktara','Ajab si','Pilla Puli','Konte Chooputo','Neeve','Ye Mantramo','Uppenanta'],
            'energetic': ['Swag Se Swagat', 'Kar Gayi Chull', 'Buddhu Sa Mann','Matargashti','Lungi Dance.','Chammak challo',' Nashe si chadgayi','Badtameez Dil','Balam pichkari','Ramulo Ramula','Buttabomma','Oorugallu ke pilla','Arabic Kuttu','Naatu Naatu'],
        }

        return random.choice(songs_by_emotion.get(emotion, []))

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Song Recommender Chatbot")

        self.output_text = scrolledtext.ScrolledText(root, width=60, height=15)
        self.output_text.pack(padx=10, pady=10)

        self.label_input = tk.Label(root, text="Chatbot:")
        self.label_input.pack(pady=5)

        self.input_var = StringVar()
        self.input_entry = tk.Entry(root, width=40, textvariable=self.input_var)
        self.input_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_input)
        self.submit_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=5)

        self.conversation_index = 0
        self.current_emotion = None

    def submit_input(self):
        user_input = self.input_var.get()
        response = chatbot_response(user_input, self.conversation_index, self.current_emotion)

        self.update_chat_window(f"User: {user_input}\nChatbot: {response}\n\n")

        
        self.conversation_index += 1

       
        self.input_var.set("")

    def update_chat_window(self, message):
        self.output_text.insert(tk.END, message)

def chatbot_response(user_input, conversation_index, current_emotion):
    if conversation_index == 0:
        return "Hi there! How is your mood today? 😊"

    elif conversation_index == 1:
        emotion = EmotionDetector.get_emotion(user_input)
        if emotion == 'neutral':
            return "I couldn't determine your mood. Please provide more information."
        else:
            response = f"Great! I sense that you're feeling {emotion}. "
            response += f"How about listening to '{SongRecommender.recommend_song(emotion)}'? 🎵"
            return response

    elif conversation_index == 2:
        if 'thanks' in user_input.lower():
            return "You're welcome! If you need more recommendations or have other moods in mind, feel free to let me know. 😊"
        else:
            return "Thanks! If the song didn't match your mood, would you like another recommendation or suggest something else? 🤔"

    elif conversation_index == 3:
        if 'yes' in user_input.lower() or ('another' in user_input.lower() and 'song' in user_input.lower()):
            new_emotion = EmotionDetector.get_emotion(user_input)
            response = f"Of course! How about another song? I sense that you're feeling {new_emotion}. "
            response += f"How about listening to '{SongRecommender.recommend_song(new_emotion)}'? 🎵"
            return response
        else:
            return "No worries! If there's anything else on your mind or if you have a specific mood, let me know. 😊"

    else:
        return "I'm glad you're enjoying the recommendations! If you have any other requests or moods in mind, feel free to let me know. 😊"

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
