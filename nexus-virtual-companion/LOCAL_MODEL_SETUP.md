# Nexus Virtual Companion - Local Llama Model Integration

## Overview
Your Nexus Virtual Companion now supports **offline Llama model execution** using Ollama! This means you can run the AI companion without any API keys or internet connection (after initial setup).

## What's Changed
- ✅ Added support for local Llama models via Ollama
- ✅ Automatic fallback to OpenAI if local model is unavailable
- ✅ Keyword-based fallback responses when both AI systems fail
- ✅ Easy configuration via `.env` file

## Setup Instructions

### Step 1: Install Ollama (Windows)
Ollama is currently installing in the background. Once complete:
- Ollama will be available as a system service
- It will run automatically on startup
- API available at `http://localhost:11434`

### Step 2: Verify Ollama Installation
```powershell
# Check if Ollama is installed
ollama --version

# Start Ollama service (if not running)
ollama serve
```

### Step 3: Pull a Llama Model
After Ollama is installed, download one of these models:

**Recommended - Mistral (Fastest, 7B params, ~4GB)**
```powershell
ollama pull mistral
```

**Alternative - Llama2 (More capable, 7B params, ~4GB)**
```powershell
ollama pull llama2
```

**Alternative - Neural Chat (Optimized for conversation, 7B params, ~4GB)**
```powershell
ollama pull neural-chat
```

### Step 4: Configure Your App
Update `.env` file:
```ini
# Use local Llama model (recommended)
USE_LOCAL_MODEL=True
LLAMA_MODEL=mistral

# Or keep OpenAI as backup
OPENAI_API_KEY=your_key_here
```

### Step 5: Run the App
```powershell
cd "f:\New folder\nexus-virtual-companion"
python app.py
```

## Model Comparison

| Model | Size | Speed | Quality | Download |
|-------|------|-------|---------|----------|
| Mistral | 7B | ⚡⚡⚡ | ⭐⭐⭐⭐ | ~4GB |
| Llama2 | 7B | ⚡⚡ | ⭐⭐⭐⭐ | ~4GB |
| Llama2 | 13B | ⚡ | ⭐⭐⭐⭐⭐ | ~8GB |
| Neural-Chat | 7B | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ~4GB |

## How It Works

### Request Flow:
1. User sends message to the pet
2. App tries **local Llama model** first (via Ollama)
3. If local model unavailable, falls back to **OpenAI**
4. If both fail, uses **keyword-based responses**

### Benefits:
- 🔓 **No API keys needed** for offline use
- 🚀 **Fast responses** (2-5 seconds)
- 💾 **Privacy-first** - your data stays local
- 💰 **Free** - no API costs
- 🌐 **Works offline** - after model download

## Troubleshooting

### Ollama Won't Connect
```powershell
# Check if Ollama service is running
Get-Service -Name "Ollama" | Select Status

# Start Ollama manually
ollama serve
```

### Download Speed Too Slow
- Try downloading at off-peak hours
- Models are typically 4-8GB
- First model download takes ~5-10 minutes

### App Still Using OpenAI
- Verify `USE_LOCAL_MODEL=True` in `.env`
- Check Ollama is running: `http://localhost:11434`
- Check model is pulled: `ollama list`

### Out of Memory Error
- Consider using smaller models (Mistral 7B)
- Close other applications
- Ensure 8GB+ RAM available

## Model Details

### Mistral (Recommended for beginners)
- Fastest response time
- Good conversation quality
- Only 4GB download
- Best for quick interactions

### Llama2
- More powerful than Mistral
- Better long-form responses
- Available in 7B or 13B versions
- Slightly slower than Mistral

### Neural-Chat
- Fine-tuned for conversation
- Excellent personality adaptation
- 4GB download
- Good balance of speed and quality

## Advanced Configuration

### Use Different Model
```ini
LLAMA_MODEL=neural-chat
# or
LLAMA_MODEL=llama2
# or
LLAMA_MODEL=mistral
```

### Change API Endpoint
```ini
OLLAMA_API_URL=http://192.168.1.100:11434/api/generate
# For remote Ollama instance
```

### Disable Local Model (Use OpenAI only)
```ini
USE_LOCAL_MODEL=False
```

## Testing

Test the integration:
```powershell
# Start the app
python app.py

# In another terminal, test the local model
curl -X POST http://localhost:11434/api/generate -d @- <<'EOF'
{
  "model": "mistral",
  "prompt": "Hello, how are you?",
  "stream": false
}
EOF
```

## Performance Tips

1. **First Run**: Model loads into memory (~1-2 minutes first time)
2. **Subsequent Runs**: Much faster after warm-up
3. **GPU Acceleration**: Ollama auto-detects GPU (NVIDIA/AMD)
4. **Model Quantization**: Smaller models available (Q4, Q5)

## FAQ

**Q: Can I use Llama offline?**
A: Yes! After downloading the model, Ollama works completely offline.

**Q: Which model should I use?**
A: Start with Mistral - it's fast and good quality. Move to Llama2 if you need better responses.

**Q: How much storage do I need?**
A: ~4-8GB per model plus ~2GB for Ollama.

**Q: Can I run multiple models?**
A: Yes! Download as many as you want, switch via `LLAMA_MODEL` setting.

**Q: What if Ollama crashes?**
A: App automatically falls back to OpenAI or keyword responses.

## Next Steps

1. ✅ Wait for Ollama installation to complete
2. 🔽 Pull your chosen model: `ollama pull mistral`
3. 🔄 Restart the Flask app
4. 💬 Start chatting with your AI companion!

---

**Questions or issues?** Check the Ollama documentation: https://github.com/ollama/ollama
