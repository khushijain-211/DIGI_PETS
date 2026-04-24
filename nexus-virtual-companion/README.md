# Nexus - AI Virtual Companion

A dynamic virtual pet companion with emotional intelligence, memory capabilities, and real-time interaction.

## Features

### 🎯 Core Features

- **Real-time Interaction**: Dynamic frontend sprite that reacts to clicks, feeding, and chat input without page refreshes
- **Emotional Engine**: Tracks Happiness, Hunger, and Affection levels that decay over time
- **AI Agent Integration**: Powered by OpenAI GPT for intelligent, contextual conversations
- **Learning Capability**: Basic memory system with keyword matching for contextual responses
- **Responsive Design**: Works beautifully on desktop and mobile devices

### 🎮 Interactions

- **Feed**: Reduce hunger and increase happiness
- **Pet**: Increase affection and happiness
- **Talk**: Communicate with Nexus AI agent for engaging conversations
- **Reset**: Start fresh with a new companion

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **AI**: OpenAI GPT-3.5-turbo
- **Database**: SQLite (for pet personality and memory)

## Project Structure

```
nexus-virtual-companion/
├── app.py                 # Flask backend with emotion logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main interface
└── static/
    ├── style.css         # Responsive styling with animations
    ├── script.js         # Frontend interaction logic
└── database/
    └── nexus.db          # SQLite database (auto-created)
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- OpenAI API key (optional, for AI agent functionality)

### Steps

1. **Navigate to project directory**:
   ```bash
   cd nexus-virtual-companion
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key (optional)**:
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
   *Without an API key, the companion will use fallback responses*

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   ```
   http://127.0.0.1:5000
   ```

## AI Agent Features

The Nexus companion now includes an advanced AI agent powered by OpenAI's GPT-3.5-turbo:

- **Contextual Conversations**: The AI understands your messages and responds in character as your virtual pet
- **Personality Integration**: Responses match the selected pet type (dog, cat, rabbit) with appropriate emojis and tone
- **Memory Awareness**: The AI considers the pet's current emotional state (happiness, hunger, affection, energy)
- **Fallback Mode**: If no API key is provided, uses intelligent keyword-based responses

### API Key Setup

1. Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
2. Set the environment variable:
   ```bash
   export OPENAI_API_KEY="sk-your-key-here"
   ```
3. Restart the application

## API Endpoints

### GET `/api/state`
Get current pet state (happiness, hunger, affection, mood)

**Response**:
```json
{
  "happiness": 75,
  "hunger": 30,
  "affection": 60,
  "mood": "happy",
  "timestamp": "2024-04-24T10:30:00"
}
```

### POST `/api/feed`
Feed the pet (reduces hunger, increases happiness)

**Response**:
```json
{
  "message": "Nexus is eating happily!",
  "state": { ... }
}
```

### POST `/api/pet`
Pet the companion (increases affection and happiness)

**Response**:
```json
{
  "message": "Nexus purrs with joy!",
  "state": { ... }
}
```

### POST `/api/talk`
Send a message to Nexus

**Request**:
```json
{
  "message": "How are you doing?"
}
```

**Response**:
```json
{
  "message": "That's interesting! Tell me more!",
  "state": { ... },
  "memory_reference": "I remember you mentioned..."
}
```

### POST `/api/reset`
Reset pet to default state

**Response**:
```json
{
  "message": "Nexus has been reset!",
  "state": { ... }
}
```

## Emotional Engine Details

### Stats System

- **Happiness** (0-100): Affected by feeding, petting, and interactions
- **Hunger** (0-100): Increases over time, can be reduced by feeding
- **Affection** (0-100): Increased through petting and conversation

### Mood States

- **Ecstatic**: Average stats > 75
- **Happy**: Average stats 60-75
- **Neutral**: Average stats 40-60
- **Sad**: Average stats 20-40
- **Depressed**: Average stats < 20

### Stat Decay

Stats decay automatically over approximately 5-minute intervals:
- Happiness: -5 per cycle
- Hunger: +10 per cycle
- Affection: -3 per cycle

## Memory System

Nexus stores user inputs and references them in responses:

- Keywords are extracted from user messages (e.g., "tired", "happy", "stressed")
- Contextual responses are generated based on recent memories
- Previous interactions can be referenced (e.g., "You mentioned you were tired yesterday")

## Customization

### Modify Pet Appearance

Edit the SVG in `templates/index.html` to change the pet's visual design.

### Adjust Animation Timings

Modify the `@keyframes` animations in `static/style.css`:
- `idle`: Pet breathing animation
- `blink`: Eye blinking
- `smile`: Mouth movement

### Customize Colors

Update CSS variables in `static/style.css`:
```css
:root {
    --primary-color: #7B5CF6;
    --secondary-color: #6B4CE6;
    --accent-color: #FFD700;
    /* ... */
}
```

### Enhance Emotional Logic

Modify the `EmotionalEngine` class in `app.py`:
- Add new stats or emotional dimensions
- Implement more sophisticated memory analysis
- Integrate with external LLM APIs for advanced responses

## Future Enhancements

- **Voice Integration**: Text-to-speech and speech recognition
- **Advanced NLP**: Integration with OpenAI GPT API
- **Multi-pet System**: Create and manage multiple companions
- **Persistence**: Cloud synchronization for pet data
- **Customization**: Themes, pet designs, and environments
- **Social Features**: Share pet achievements and interactions

## Troubleshooting

### Port Already in Use
If port 5000 is occupied, modify `app.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Database Errors
Delete the `database/nexus.db` file to reset the database.

### CORS Issues
Ensure the frontend and backend are running on the same server (already configured in Flask).

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork, modify, and enhance Nexus! Possible areas for contribution:

- New emotional states or stat systems
- Enhanced memory and learning algorithms
- Visual improvements and new animations
- Mobile app wrapper
- Docker containerization

---

**Created**: 2024
**Status**: Active Development
**Maintained**: GitHub Copilot Assistant
