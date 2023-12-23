# HTML Code Generator - Fine-Tuning Falcon-7b-instruct sharded version Model

Welcome to my project, where i have fine-tuned falcon-7b to generated HTML code from natural language prompts.

## Overview

- **Model**: Falcon-7b-instruct sharded version , HF: vilsonrodrigues/falcon-7b-instruct-sharded
- **Fine-tuning**: PEFT & QLoRA - For memory-efficient and high-performance model fine-tuning
- **[Dataset](https://huggingface.co/datasets/jawerty/html_dataset)**: Natural language prompts with its equivalent HTML code
 
# Access the notebooks through colab:

Fine tuning notebook: https://colab.research.google.com/drive/1d1N8qCMXLr-aDUIsyCO699myWaEMU_wv?usp=sharing

BLEU Evaluation notebook: https://colab.research.google.com/drive/1Qh7b_llmpf2hSEdSwN59R_HDd5cgnp83?usp=sharing

API Notebook:  https://colab.research.google.com/drive/14NecwLL5ro1tzdrKJR-cTgTB8bLLPrvu?usp=sharing

Streamlit Frontent - streamlit_frontend.py

# Training Loss

![W B Chart 22_12_2023, 21_00_55](https://github.com/R-Shyam-sundar/HTML-Code-Generation-from-Natural-Language-prompts/assets/82640234/102baec6-fc33-4f24-8574-9de26f76be39)

# Running Streamlit Frontend

1. Run the FastAPI_+_Uvicorn.ipynb notebook, and recieve the deployed public link.
2. Update the public link in streamlit_frontend.py
3. streamlit run streamlit_frontend.py

4. ![Screenshot from 2023-12-23 12-34-26](https://github.com/R-Shyam-sundar/HTML-Code-Generation-from-Natural-Language-prompts/assets/82640234/944f5013-3c0d-4579-bbc7-9345b50518e5)
