import subprocess

# Run 'wget' in the 'models' directory
subprocess.run(
    ["wget", "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf"],
    cwd="models"
)
