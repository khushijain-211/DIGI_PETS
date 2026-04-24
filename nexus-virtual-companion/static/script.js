/**
 * Nexus Advanced Virtual Companion - Enhanced Frontend
 * College-level interactive AI agent with typing animations
 */

// Pet SVG definitions remain the same
const PET_SVGS = {
    'dog': `
        <svg viewBox="0 0 200 200" width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="100" cy="130" rx="50" ry="60" fill="#8B6F47" opacity="0.9"/>
            <circle cx="100" cy="60" r="45" fill="#A0826D"/>
            <ellipse cx="70" cy="25" rx="15" ry="25" fill="#8B6F47"/>
            <ellipse cx="70" cy="28" rx="8" ry="15" fill="#C4B5A0"/>
            <ellipse cx="130" cy="25" rx="15" ry="25" fill="#8B6F47"/>
            <ellipse cx="130" cy="28" rx="8" ry="15" fill="#C4B5A0"/>
            <ellipse cx="100" cy="75" rx="25" ry="20" fill="#C4B5A0"/>
            <circle cx="75" cy="45" r="8" fill="#FFF"/>
            <circle cx="75" cy="45" r="7" fill="#000"/>
            <circle cx="77" cy="43" r="2.5" fill="#FFF"/>
            <circle cx="125" cy="45" r="8" fill="#FFF"/>
            <circle cx="125" cy="45" r="7" fill="#000"/>
            <circle cx="127" cy="43" r="2.5" fill="#FFF"/>
            <ellipse cx="85" cy="78" rx="8" ry="6" fill="#B8A696"/>
            <ellipse cx="115" cy="78" rx="8" ry="6" fill="#B8A696"/>
            <circle cx="100" cy="78" r="6" fill="#3D3D3D"/>
            <path d="M 100 78 L 100 88" stroke="#000" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M 95 86 Q 100 92 105 86" stroke="#000" stroke-width="2" fill="none" stroke-linecap="round"/>
            <ellipse cx="100" cy="92" rx="4" ry="5" fill="#FF6B9D"/>
            <path d="M 145 140 Q 170 125 175 90" stroke="#8B6F47" stroke-width="9" fill="none" stroke-linecap="round"/>
            <ellipse cx="75" cy="180" rx="12" ry="18" fill="#8B6F47"/>
            <ellipse cx="125" cy="180" rx="12" ry="18" fill="#8B6F47"/>
            <ellipse cx="75" cy="190" rx="6" ry="5" fill="#C4B5A0"/>
            <ellipse cx="125" cy="190" rx="6" ry="5" fill="#C4B5A0"/>
        </svg>
    `,
    'cat': `
        <svg viewBox="0 0 200 200" width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="100" cy="130" rx="48" ry="58" fill="#FFB347" opacity="0.9"/>
            <circle cx="100" cy="65" r="42" fill="#FFC968"/>
            <path d="M 65 30 L 55 0 L 75 18 Z" fill="#FFB347"/>
            <path d="M 68 26 L 62 8 L 72 19 Z" fill="#FFD699"/>
            <path d="M 135 30 L 145 0 L 125 18 Z" fill="#FFB347"/>
            <path d="M 132 26 L 138 8 L 128 19 Z" fill="#FFD699"/>
            <circle cx="77" cy="48" r="9" fill="#90EE90"/>
            <ellipse cx="77" cy="50" rx="2.5" ry="5" fill="#000"/>
            <circle cx="79" cy="46" r="2.5" fill="#FFF"/>
            <circle cx="123" cy="48" r="9" fill="#90EE90"/>
            <ellipse cx="123" cy="50" rx="2.5" ry="5" fill="#000"/>
            <circle cx="125" cy="46" r="2.5" fill="#FFF"/>
            <path d="M 100 75 L 96 83 L 100 85 L 104 83 Z" fill="#FFB6D9"/>
            <path d="M 100 75 Q 88 83 82 80" stroke="#000" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 100 75 Q 112 83 118 80" stroke="#000" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <line x1="50" y1="68" x2="25" y2="65" stroke="#000" stroke-width="1.5"/>
            <line x1="50" y1="78" x2="20" y2="80" stroke="#000" stroke-width="1.5"/>
            <line x1="150" y1="68" x2="175" y2="65" stroke="#000" stroke-width="1.5"/>
            <line x1="150" y1="78" x2="180" y2="80" stroke="#000" stroke-width="1.5"/>
            <path d="M 140 170 Q 165 185 170 145" stroke="#FFB347" stroke-width="11" fill="none" stroke-linecap="round"/>
            <path d="M 141 169 Q 164 182 168 145" stroke="#FF9500" stroke-width="4" fill="none" stroke-linecap="round"/>
            <ellipse cx="75" cy="180" rx="14" ry="20" fill="#FFB347"/>
            <ellipse cx="125" cy="180" rx="14" ry="20" fill="#FFB347"/>
            <circle cx="75" cy="193" r="6" fill="#FFD699"/>
            <circle cx="125" cy="193" r="6" fill="#FFD699"/>
        </svg>
    `,
    'rabbit': `
        <svg viewBox="0 0 200 200" width="200" height="200" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="100" cy="135" rx="45" ry="58" fill="#FFFACD" opacity="0.9"/>
            <ellipse cx="100" cy="140" rx="28" ry="35" fill="#FFFACD" opacity="0.5"/>
            <circle cx="100" cy="70" r="40" fill="#FFFACD"/>
            <ellipse cx="75" cy="15" rx="12" ry="42" fill="#FFFACD"/>
            <ellipse cx="75" cy="20" rx="7" ry="35" fill="#FFB6C1"/>
            <ellipse cx="125" cy="15" rx="12" ry="42" fill="#FFFACD"/>
            <ellipse cx="125" cy="20" rx="7" ry="35" fill="#FFB6C1"/>
            <circle cx="78" cy="52" r="8" fill="#FFF"/>
            <circle cx="78" cy="52" r="7" fill="#000"/>
            <circle cx="80" cy="50" r="2.5" fill="#FFF"/>
            <circle cx="122" cy="52" r="8" fill="#FFF"/>
            <circle cx="122" cy="52" r="7" fill="#000"/>
            <circle cx="124" cy="50" r="2.5" fill="#FFF"/>
            <circle cx="100" cy="75" r="5" fill="#FFB6C1"/>
            <circle cx="100" cy="72" r="2" fill="#FF69B4"/>
            <path d="M 100 75 Q 92 84 88 82" stroke="#000" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M 100 75 Q 108 84 112 82" stroke="#000" stroke-width="2" fill="none" stroke-linecap="round"/>
            <line x1="100" y1="68" x2="100" y2="58" stroke="#FFB6C1" stroke-width="1.5"/>
            <circle cx="100" cy="185" r="18" fill="#FFFACD"/>
            <circle cx="100" cy="185" r="14" fill="#FFF"/>
            <circle cx="100" cy="185" r="10" fill="#FFB6C1"/>
            <ellipse cx="75" cy="185" rx="13" ry="18" fill="#FFFACD"/>
            <ellipse cx="125" cy="185" rx="13" ry="18" fill="#FFFACD"/>
            <circle cx="75" cy="195" r="7" fill="#FFB6C1"/>
            <circle cx="125" cy="195" r="7" fill="#FFB6C1"/>
            <circle cx="70" cy="193" r="2" fill="#FF69B4"/>
            <circle cx="80" cy="193" r="2" fill="#FF69B4"/>
            <circle cx="120" cy="193" r="2" fill="#FF69B4"/>
            <circle cx="130" cy="193" r="2" fill="#FF69B4"/>
        </svg>
    `
};

class NexusCompanion {
    constructor() {
        this.currentState = null;
        this.currentPetType = null;
        this.foodMenuOpen = false;
        this.currentFoods = [];
        this.messageCount = 0;
        this.isTyping = false;
        this.initializeSelectionScreen();
    }

    initializeSelectionScreen() {
        fetch('/api/pets')
            .then(response => response.json())
            .then(pets => {
                const petOptions = document.getElementById('petOptions');
                petOptions.innerHTML = pets.map(pet => `
                    <div class="pet-option" onclick="nexus.selectPet('${pet.type}')">
                        <div class="pet-option-emoji">${pet.emoji}</div>
                        <div class="pet-option-name">${pet.name}</div>
                    </div>
                `).join('');
            })
            .catch(err => console.error('Error loading pets:', err));
    }

    selectPet(petType) {
        fetch('/api/select-pet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pet_type: petType })
        })
            .then(response => response.json())
            .then(data => {
                this.currentPetType = petType;
                this.currentFoods = data.foods;

                document.getElementById('petSelectionOverlay').style.display = 'none';
                document.getElementById('mainContainer').style.display = 'flex';

                document.getElementById('petTitle').textContent = `${data.state.pet_emoji} ${data.state.pet_name}`;

                this.init();
                this.typeMessage(data.message, 'nexus');
            })
            .catch(err => console.error('Error selecting pet:', err));
    }

    init() {
        const petContainer = document.getElementById('pet');
        petContainer.innerHTML = PET_SVGS[this.currentPetType];

        // Event listeners
        document.getElementById('sendBtn').addEventListener('click', () => this.sendMessage());
        document.getElementById('messageInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !this.isTyping) this.sendMessage();
        });
        document.getElementById('petBtn').addEventListener('click', () => this.pet());
        document.getElementById('feedMenuBtn').addEventListener('click', () => this.toggleFoodMenu());
        document.getElementById('resetBtn').addEventListener('click', () => this.reset());

        this.loadFoodOptions();
        this.updateState();

        setInterval(() => this.updateState(), 30000);
        document.getElementById('messageInput').focus();
    }

    loadFoodOptions() {
        const foodOptions = document.getElementById('foodOptions');
        foodOptions.innerHTML = this.currentFoods.map(food => `
            <button class="food-btn" onclick="nexus.feed('${food.name}')">
                <span class="food-emoji">${food.emoji}</span> ${food.name}
            </button>
        `).join('');
    }

    toggleFoodMenu() {
        const menu = document.getElementById('foodMenu');
        this.foodMenuOpen = !this.foodMenuOpen;
        menu.style.display = this.foodMenuOpen ? 'block' : 'none';
        if (this.foodMenuOpen) {
            this.addNexusMessage("What would you like to feed me? 🍽️");
        }
    }

    async updateState() {
        try {
            const response = await fetch('/api/state');
            this.currentState = await response.json();
            this.updateUI();
        } catch (error) {
            console.error('Error updating state:', error);
        }
    }

    updateUI() {
        if (!this.currentState) return;

        const { happiness, hunger, affection, energy, mood } = this.currentState;

        document.getElementById('happinessFill').style.width = happiness + '%';
        document.getElementById('happinessValue').textContent = Math.round(happiness);

        document.getElementById('hungerFill').style.width = hunger + '%';
        document.getElementById('hungerValue').textContent = Math.round(hunger);

        document.getElementById('affectionFill').style.width = affection + '%';
        document.getElementById('affectionValue').textContent = Math.round(affection);

        document.getElementById('energyFill').style.width = energy + '%';
        document.getElementById('energyValue').textContent = Math.round(energy);

        const moodText = document.getElementById('moodText');
        moodText.textContent = mood.charAt(0).toUpperCase() + mood.slice(1);
        this.updateMoodColor(mood);
        this.updatePetAnimation(mood);
    }

    updateMoodColor(mood) {
        const moodColors = {
            'ecstatic': { color: '#FFD700', shadow: 'rgba(255, 215, 0, 0.8)' },
            'happy': { color: '#FFA500', shadow: 'rgba(255, 165, 0, 0.6)' },
            'neutral': { color: '#B0B0C8', shadow: 'rgba(176, 176, 200, 0.4)' },
            'sad': { color: '#FF69B4', shadow: 'rgba(255, 105, 180, 0.5)' },
            'depressed': { color: '#FF6B6B', shadow: 'rgba(255, 107, 107, 0.5)' }
        };

        const moodStyle = moodColors[mood] || moodColors['neutral'];
        const indicator = document.getElementById('moodIndicator');
        indicator.style.borderColor = moodStyle.color;
        indicator.style.color = moodStyle.color;
        indicator.style.boxShadow = `0 0 25px ${moodStyle.shadow}`;
    }

    updatePetAnimation(mood) {
        const petElement = document.getElementById('pet');
        petElement.style.animation = 'none';

        setTimeout(() => {
            if (mood === 'ecstatic') {
                petElement.style.animation = 'bounce 0.6s ease-in-out';
            } else if (mood === 'happy') {
                petElement.style.animation = 'idle 3s ease-in-out infinite';
            }
        }, 10);
    }

    addUserMessage(message) {
        const chatContainer = document.getElementById('chatContainer');
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble user-message';
        bubble.textContent = message;
        chatContainer.appendChild(bubble);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    addNexusMessage(message) {
        const chatContainer = document.getElementById('chatContainer');
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble nexus-message';
        bubble.textContent = message;
        chatContainer.appendChild(bubble);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    async typeMessage(message, sender) {
        const chatContainer = document.getElementById('chatContainer');
        const bubble = document.createElement('div');
        bubble.className = `chat-bubble ${sender === 'user' ? 'user-message' : 'nexus-message'}`;
        bubble.textContent = '';
        chatContainer.appendChild(bubble);

        this.isTyping = true;
        let charIndex = 0;

        const typeInterval = setInterval(() => {
            if (charIndex < message.length) {
                bubble.textContent += message[charIndex];
                charIndex++;
                chatContainer.scrollTop = chatContainer.scrollHeight;
            } else {
                clearInterval(typeInterval);
                this.isTyping = false;
            }
        }, 15);
    }

    async sendMessage() {
        const input = document.getElementById('messageInput');
        const message = input.value.trim();

        if (!message || this.isTyping) return;

        input.value = '';
        this.addUserMessage(message);

        try {
            const response = await fetch('/api/talk', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            // Add slight delay for natural conversation feel
            setTimeout(() => {
                this.typeMessage(data.message, 'nexus');
            }, 300);

            this.updateState();
        } catch (error) {
            console.error('Error sending message:', error);
            this.addNexusMessage("Sorry, I had trouble understanding that. Could you rephrase?");
        }
    }

    async pet() {
        try {
            const response = await fetch('/api/pet', { method: 'POST' });
            const data = await response.json();
            this.typeMessage(data.message, 'nexus');
            this.updateState();
        } catch (error) {
            console.error('Error petting:', error);
        }
    }

    async feed(foodName) {
        try {
            const response = await fetch('/api/feed', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ food: foodName })
            });

            const data = await response.json();
            this.toggleFoodMenu();
            this.typeMessage(data.message, 'nexus');
            this.updateState();
        } catch (error) {
            console.error('Error feeding:', error);
        }
    }

    async reset() {
        if (confirm('Switch to a different companion?')) {
            document.getElementById('mainContainer').style.display = 'none';
            document.getElementById('petSelectionOverlay').style.display = 'flex';
            document.getElementById('chatContainer').innerHTML = '';
            this.currentState = null;
        }
    }
}

/**
 * Emotion Detection Engine - Local Canvas-based Emotion Detection
 * Analyzes video feed to detect emotions without external ML dependencies
 */
class EmotionDetector {
    constructor(nexusCompanion) {
        this.nexus = nexusCompanion;
        this.isDetecting = false;
        this.currentEmotion = null;
        this.modelsLoaded = true;
        this.video = null;
        this.canvas = null;
        this.ctx = null;
        this.detectionInterval = null;
        this.emotionHistory = [];
        this.frameCount = 0;
        this.isTogglingDetection = false;
        this.lastToggleTime = 0;
        this.MIN_TOGGLE_INTERVAL = 500;
        this.emotionChangeThreshold = 8; // Need 8 consecutive frames of same emotion to change
        this.consecutiveEmotionCount = 0;
        this.detectedEmotionOnStart = null; // Store emotion once when detection starts
        
        // Only 4 emotions: happy, sad, angry, cry
        this.emotionMap = {
            'happy': { emoji: '😊', color: '#FFD700' },
            'sad': { emoji: '😢', color: '#FF69B4' },
            'angry': { emoji: '😠', color: '#FF6B6B' },
            'cry': { emoji: '😭', color: '#5B9BD5' }
        };

        this.setupEventListeners();
    }

    setupEventListeners() {
        const emotionToggleBtn = document.getElementById('emotionToggleBtn');
        const closeCameraBtn = document.getElementById('closeCameraBtn');
        const emotionPanel = document.getElementById('emotionPanel');

        if (emotionToggleBtn) {
            emotionToggleBtn.addEventListener('click', () => {
                const now = Date.now();
                if (!this.isTogglingDetection && (now - this.lastToggleTime) > this.MIN_TOGGLE_INTERVAL) {
                    this.lastToggleTime = now;
                    this.toggleEmotionDetection();
                }
            });
        }
        
        if (closeCameraBtn) {
            closeCameraBtn.addEventListener('click', () => {
                const now = Date.now();
                if (!this.isTogglingDetection && (now - this.lastToggleTime) > this.MIN_TOGGLE_INTERVAL) {
                    this.lastToggleTime = now;
                    this.stopEmotionDetection();
                }
            });
        }

        // Add close on ESC key press
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isDetecting && emotionPanel && emotionPanel.style.display === 'block') {
                console.log('🔑 ESC key pressed - closing camera');
                this.stopEmotionDetection();
            }
        });

        // Add close on clicking backdrop
        const emotionPanelBackdrop = document.getElementById('emotionPanelBackdrop');
        if (emotionPanelBackdrop) {
            emotionPanelBackdrop.addEventListener('click', () => {
                console.log('👆 Clicked backdrop - closing camera');
                this.stopEmotionDetection();
            });
        }
    }

    async loadModels() {
        return true;
    }

    async toggleEmotionDetection() {
        if (this.isTogglingDetection) return;
        this.isTogglingDetection = true;
        
        try {
            if (this.isDetecting) {
                this.stopEmotionDetection();
            } else {
                await this.startEmotionDetection();
            }
        } finally {
            // Reset the toggle flag after the operation
            setTimeout(() => {
                this.isTogglingDetection = false;
            }, 100);
        }
    }

    async startEmotionDetection() {
        try {
            this.nexus.addNexusMessage("🎥 Starting facial recognition... this helps me understand your emotions better! 💕");
            
            const emotionPanel = document.getElementById('emotionPanel');
            const emotionPanelBackdrop = document.getElementById('emotionPanelBackdrop');
            const emotionToggleBtn = document.getElementById('emotionToggleBtn');
            
            emotionPanel.style.display = 'block';
            emotionPanelBackdrop.style.display = 'block';
            emotionToggleBtn.classList.add('active');
            emotionToggleBtn.textContent = '📹';

            this.video = document.getElementById('emotionCamera');
            this.canvas = document.getElementById('emotionCanvas');
            this.ctx = this.canvas.getContext('2d', { willReadFrequently: true });

            // Reset emotion tracking for this session
            this.detectedEmotionOnStart = null;
            this.currentEmotion = null;
            this.consecutiveEmotionCount = 0;

            // Try to access webcam
            try {
                const stream = await navigator.mediaDevices.getUserMedia({
                    video: { 
                        width: { ideal: 320 }, 
                        height: { ideal: 240 },
                        facingMode: 'user'
                    }
                });

                this.video.srcObject = stream;
                this.video.onloadedmetadata = () => {
                    this.video.play();
                    this.isDetecting = true;
                    console.log('✅ Camera started, beginning emotion detection...');
                    this.startDetectionLoop();
                };
            } catch (cameraError) {
                console.warn('⚠️ Camera access denied, running in DEMO MODE');
                // Start demo mode - pick one random emotion and stick with it
                this.nexus.addNexusMessage("📷 Camera not available, starting DEMO MODE to show how emotions work!");
                this.video.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                
                // Pick one emotion for this session
                const emotions = ['happy', 'sad', 'angry', 'cry'];
                this.detectedEmotionOnStart = emotions[Math.floor(Math.random() * emotions.length)];
                console.log(`🎭 Demo mode - locked emotion: ${this.detectedEmotionOnStart}`);
                
                this.isDetecting = true;
                this.startDetectionLoop();
            }

        } catch (error) {
            console.error('Error in emotion detection setup:', error);
            this.nexus.addNexusMessage("😢 Could not start emotion detection: " + error.message);
            this.stopEmotionDetection();
        }
    }

    stopEmotionDetection() {
        if (this.video && this.video.srcObject) {
            this.video.srcObject.getTracks().forEach(track => track.stop());
        }

        this.isDetecting = false;
        clearInterval(this.detectionInterval);
        this.emotionHistory = [];
        this.frameCount = 0;
        this.consecutiveEmotionCount = 0;
        this.detectedEmotionOnStart = null;

        const emotionPanel = document.getElementById('emotionPanel');
        const emotionPanelBackdrop = document.getElementById('emotionPanelBackdrop');
        const emotionToggleBtn = document.getElementById('emotionToggleBtn');
        
        emotionPanel.style.display = 'none';
        emotionPanelBackdrop.style.display = 'none';
        emotionToggleBtn.classList.remove('active');
        emotionToggleBtn.textContent = '📹';

        this.nexus.addNexusMessage("Camera closed! But I'll always remember how you felt... 💭");
    }

    startDetectionLoop() {
        console.log('▶️ Starting detection loop - emotion will be stable once detected');
        this.detectionInterval = setInterval(async () => {
            await this.detectEmotion();
        }, 500); // Check every 500ms
    }

    async detectEmotion() {
        if (!this.isDetecting || !this.video) return;

        try {
            // Check if we have a real video stream
            const hasRealStream = this.video.srcObject && this.video.readyState === this.video.HAVE_ENOUGH_DATA;
            
            if (!hasRealStream && !this.video.style.background) {
                // Not in demo mode and no video ready
                return;
            }

            // Set canvas dimensions with fallback
            const width = this.video.videoWidth || 320;
            const height = this.video.videoHeight || 240;
            this.canvas.width = width;
            this.canvas.height = height;
            
            // Draw video to canvas (or create demo pattern)
            if (hasRealStream) {
                this.ctx.drawImage(this.video, 0, 0);
            } else {
                // Demo mode: create colorful pattern
                this.ctx.fillStyle = `hsl(${Math.random() * 360}, 70%, 50%)`;
                this.ctx.fillRect(0, 0, width, height);
            }
            
            // Get image data and analyze
            const imageData = this.ctx.getImageData(0, 0, width, height);
            const detectedEmotion = this.analyzeFrame(imageData);
            
            if (detectedEmotion) {
                // Check if this emotion matches our current emotion
                if (detectedEmotion === this.currentEmotion) {
                    // Same emotion detected, increment consistency counter
                    this.consecutiveEmotionCount++;
                } else {
                    // Different emotion detected, reset counter
                    this.consecutiveEmotionCount = 0;
                }
                
                // Only change emotion if we have consistent detections
                // OR if we haven't set an emotion yet
                if (!this.currentEmotion || 
                    (detectedEmotion !== this.currentEmotion && this.consecutiveEmotionCount >= this.emotionChangeThreshold)) {
                    
                    // Only log and update if emotion actually changed
                    if (detectedEmotion !== this.currentEmotion) {
                        this.currentEmotion = detectedEmotion;
                        console.log(`✅ Emotion locked in: ${detectedEmotion} (after ${this.consecutiveEmotionCount} consistent frames)`);
                        this.updateEmotionDisplay(detectedEmotion, 0.85);
                        await this.sendEmotionToPet(detectedEmotion);
                    }
                } else {
                    // Update display but don't change emotion or send new response
                    this.updateEmotionDisplay(this.currentEmotion || detectedEmotion, 0.85);
                }
            }
        } catch (error) {
            console.error('Error in emotion detection:', error);
        }
    }

    analyzeFrame(imageData) {
        const data = imageData.data;
        const width = imageData.width;
        const height = imageData.height;
        
        // Demo mode check: if we have no data or extremely uniform data, it's demo mode
        let isUniformData = true;
        if (data && data.length > 4) {
            const sampleR = data[0];
            const sampleG = data[1];
            const sampleB = data[2];
            
            // Check if more than 80% of pixels are identical (uniform gradient)
            let uniformPixels = 0;
            for (let i = 0; i < Math.min(data.length, 1000); i += 4) {
                if (Math.abs(data[i] - sampleR) < 20 && 
                    Math.abs(data[i+1] - sampleG) < 20 && 
                    Math.abs(data[i+2] - sampleB) < 20) {
                    uniformPixels++;
                }
            }
            
            isUniformData = (uniformPixels / (Math.min(data.length, 1000) / 4)) > 0.8;
        }
        
        // In demo mode, always return the locked emotion
        if (!data || data.length === 0 || isUniformData) {
            if (this.detectedEmotionOnStart) {
                console.log(`🎭 Demo mode - returning locked emotion: ${this.detectedEmotionOnStart}`);
                return this.detectedEmotionOnStart;
            }
            // Fallback - shouldn't reach here
            const emotions = ['happy', 'sad', 'angry', 'cry'];
            return emotions[Math.floor(Math.random() * emotions.length)];
        }
        
        // Real camera feed analysis
        let brightness = 0;
        let redAvg = 0, greenAvg = 0, blueAvg = 0;
        let darkPixels = 0;
        let brightPixels = 0;
        let pixelCount = 0;
        
        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];
            const pixelBrightness = (r + g + b) / 3;
            
            brightness += pixelBrightness;
            redAvg += r;
            greenAvg += g;
            blueAvg += b;
            
            if (pixelBrightness < 80) darkPixels++;
            if (pixelBrightness > 180) brightPixels++;
            pixelCount++;
        }
        
        brightness = brightness / pixelCount;
        redAvg = redAvg / pixelCount;
        greenAvg = greenAvg / pixelCount;
        blueAvg = blueAvg / pixelCount;
        
        const darkRatio = darkPixels / pixelCount;
        const brightRatio = brightPixels / pixelCount;
        const contrastRatio = Math.abs(brightRatio - darkRatio);
        
        // Analyze edges
        let edgeCount = 0;
        let edgeStrength = 0;
        for (let x = 2; x < width - 2; x += 2) {
            for (let y = 2; y < height - 2; y += 2) {
                const idx = (y * width + x) * 4;
                const nextIdx = (y * width + x + 1) * 4;
                if (idx < data.length && nextIdx < data.length) {
                    const current = (data[idx] + data[idx + 1] + data[idx + 2]) / 3;
                    const next = (data[nextIdx] + data[nextIdx + 1] + data[nextIdx + 2]) / 3;
                    const diff = Math.abs(current - next);
                    
                    if (diff > 40) {
                        edgeCount++;
                        edgeStrength += diff;
                    }
                }
            }
        }
        
        const edgeRatio = edgeCount / ((width / 2) * (height / 2));
        const maxColor = Math.max(redAvg, greenAvg, blueAvg);
        const redDominance = redAvg / (maxColor || 1);
        
        // Debug logging
        console.log(`📊 Detection: brightness=${brightness.toFixed(1)}, edges=${edgeRatio.toFixed(3)}, red=${redDominance.toFixed(2)}, dark=${darkRatio.toFixed(2)}, contrast=${contrastRatio.toFixed(2)}`);
        
        // **IMPROVED 4-EMOTION DETECTION - Better Balanced Thresholds**
        
        // Priority 1: CRY - Very dark face (tears or covered face)
        if (brightness < 80 || darkRatio > 0.60) {
            console.log(`😭 Detected: CRY (very dark face)`);
            return 'cry';
        }
        
        // Priority 2: HAPPY - Bright face with good edge definition (smiling/expressive)
        // Look for bright, well-lit faces with facial features visible
        if (brightness > 115 && edgeRatio > 0.040) {
            console.log(`😊 Detected: HAPPY (bright & expressive)`);
            return 'happy';
        }
        
        // Priority 3: SAD - Moderate to lower brightness with few strong edges (passive expression)
        // Less contrast = less tension = sadness
        if (brightness < 100 && contrastRatio < 0.12 && edgeRatio < 0.040) {
            console.log(`😢 Detected: SAD (dim & passive)`);
            return 'sad';
        }
        
        // Priority 4: ANGRY - High contrast + very strong edges (tense facial muscles)
        // Must be REALLY contrasty and edgy to be angry (strict threshold)
        if (contrastRatio > 0.22 && edgeRatio > 0.065) {
            console.log(`😠 Detected: ANGRY (high tension & contrast)`);
            return 'angry';
        }
        
        // Fallback detection based on brightness and edges
        if (brightness < 95) {
            console.log(`⚙️ Fallback: SAD (darker, low contrast)`);
            return 'sad';
        } else if (brightness > 110) {
            console.log(`⚙️ Fallback: HAPPY (bright and clear)`);
            return 'happy';
        }
        
        // Default middle ground
        console.log(`⚙️ Fallback: HAPPY (neutral/unclear)`);
        return 'happy';
    }

    getDominantEmotion() {
        if (this.emotionHistory.length === 0) return 'neutral';
        
        const emotionCounts = {};
        this.emotionHistory.forEach(emotion => {
            emotionCounts[emotion] = (emotionCounts[emotion] || 0) + 1;
        });
        
        return Object.keys(emotionCounts).reduce((a, b) => 
            emotionCounts[a] > emotionCounts[b] ? a : b
        );
    }

    updateEmotionDisplay(emotion, confidence) {
        const emotionInfo = this.emotionMap[emotion] || this.emotionMap['neutral'];
        const detectedEmotionEl = document.getElementById('detectedEmotion');
        const confidenceEl = document.getElementById('emotionConfidence');
        const badge = document.getElementById('userEmotionBadge');

        if (detectedEmotionEl) {
            detectedEmotionEl.textContent = `${emotionInfo.emoji} ${emotion.toUpperCase()}`;
            detectedEmotionEl.style.color = emotionInfo.color;
        }
        if (confidenceEl) {
            confidenceEl.textContent = `${(confidence * 100).toFixed(0)}% detected`;
        }
        
        if (badge) {
            badge.textContent = `${emotionInfo.emoji} ${emotion}`;
            badge.style.display = 'inline-block';
        }
    }

    async sendEmotionToPet(emotion) {
        try {
            const response = await fetch('/api/detect-emotion', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    user_emotion: emotion,
                    timestamp: new Date().toISOString()
                })
            });

            if (response.ok) {
                const data = await response.json();
                console.log('📨 Pet emotion response:', data);
                if (data.emotional_response) {
                    this.nexus.typeMessage(data.emotional_response, 'nexus');
                }
            }
        } catch (error) {
            console.error('Error sending emotion to pet:', error);
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.nexus = new NexusCompanion();
    window.emotionDetector = new EmotionDetector(window.nexus);
});
