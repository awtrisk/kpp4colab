import subprocess

subprocess.run(["git", "clone", "https://github.com/LostRuins/koboldcpp.git"])

print("Repository cloned successfulily!")

subprocess.run(["cd", "koboldcpp"])
subprocess.run(["make", "LLAMA_CUBLAS=1"])
