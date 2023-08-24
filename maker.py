import os

os.system("git clone https://github.com/LostRuins/koboldcpp.git")
os.chdir("koboldcpp")
os.system("make LLAMA_CUBLAS=1")
