# Projeto-PDI
Projeto da disciplina de Introdução ao Processamento Digital de Imagens na UFPB, como o professor Augusto de Holanda. Os integrantes são Pedro Benício, Pedro Garrafielo, Vinícius Fernandes e Guilerme Muniz.

#Tecnologias usadas

-Python3.10
-OpenCV
-NumPy
-Matplotlib
-Pillow
-Tkinter

#Pré-requisitos no Linux/Debian

Antes de criar o ambiente virtual deve-se instalar o Tkinter e Pillow:

sudo apt update
sudo apt install python3-tk python3-pil python3-pil.imagetk -y

Para instalar Python, pip e venv(se necessário):

sudo apt update
sudo apt install python3 python3-pip python3-venv -y

#Criar e ativar o ambiente virtual

python3 -m venv venv
source venv/bin/activate

#Instalar as bibliotecas necessárias

pip install opencv-python numpy matplotlib pillow
