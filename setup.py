
def installation_processes():
    import subprocess
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["wget", "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf"],cwd="models")


installation_processes()
