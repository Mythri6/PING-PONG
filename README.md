# Ping Pong - Pygame Version

A real-time Ping Pong game built using Python and Pygame. Play against an AI opponent, enjoy smooth ball physics, interactive game over screens, replay options, and immersive sound effects.  

---

## Features
- **Smooth Ball Physics:** Accurate collisions with paddles and walls, even at high speeds.  
- **AI Opponent:** Paddle automatically tracks the ball.  
- **Game Over Screen:** Displays the winner when a player reaches the winning score.  
- **Replay Options:** Choose "Best of 3", "Best of 5", or "Best of 7" to continue playing, or exit.  
- **Sound Effects:** Paddle hit, wall bounce, and scoring sounds for full game immersion.  

---

##  Project Structure

pygame-pingpong/
├── main.py
├── requirements.txt
├── game/
│ ├── game_engine.py
│ ├── paddle.py
│ └── ball.py
├── sounds/
│ ├── paddle_hit.wav
│ ├── wall_bounce.wav
│ └── score.wav
└── README.md

##  Installation

1. Clone the repository
2.Install dependencies: pip install -r requirements.txt
3. Run the game: python main.py

Use W / S keys to move your paddle up and down.
The AI controls the other paddle.
First player to reach the selected score wins.

Sound Effects

Make sure the sounds/ folder contains these WAV files:
paddle_hit.wav – played when ball hits a paddle.
wall_bounce.wav – played when ball hits top or bottom walls.
score.wav – played when a player scores a point.

Note: Only WAV or OGG formats are supported by Pygame. Convert MP3s if necessary.

Gameplay Instructions:

Launch the game with python main.py.
Play against the AI.
When a player reaches the winning score, the Game Over screen appears.
Choose a replay option (Best of 3, 5, 7) or press ESC to exit.
Enjoy the sounds and smooth gameplay!