import subprocess
import os

os.system("git clone https://github.com/LostRuins/koboldcpp.git
print("cloned")
os.system("cd koboldcpp")
os.system("make LLAMA_CUBLAS=1")
