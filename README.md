# Análise de Stemming e Lematização em Espanhol

Este repositório contém um código em Python que exemplifica o uso de **stemming** e **lematização** na língua espanhola, utilizando as bibliotecas **NLTK** e **spaCy**. A atividade faz parte do curso de Processamento de Linguagem Natural (PLN) e demonstra como diferentes textos podem resultar em saídas semelhantes após esses processos.

## 📌 Objetivo
Implementar e ilustrar os conceitos de **stemming** e **lematização** em textos em espanhol, além de mostrar um caso onde diferentes frases levam à mesma saída. O resultado final consiste em **vetores ordenados contendo stems e lemas**.

## 🛠 Tecnologias Utilizadas
- Python
- NLTK (Natural Language Toolkit)
- spaCy

## 🚀 Como Rodar o Código
### 1️⃣ Instale as dependências:
Abra o terminal e execute:
```bash
pip install nltk spacy
python -m spacy download es_core_news_sm
```

### 2️⃣ Execute o script
Rodando o código em Python:
```bash
python app.py
```

## 📜 Estrutura do Código
1. **Tokenização:** Separação das palavras nas frases.
2. **Stemming:** Redução das palavras ao seu radical usando o **SnowballStemmer**.
3. **Lematização:** Transformação das palavras em sua forma base usando o modelo **spaCy**.
4. **Ordenação:** Remoção de duplicatas e organização alfabética dos resultados.
5. **Comparação:** Verificação se diferentes frases geram a mesma saída.

## 📚 Referências
- [Documentação do NLTK](https://www.nltk.org/)
- [Documentação do spaCy](https://spacy.io/)

## 📌 Autor
Desenvolvido como parte das atividades acadêmicas de PLN. Sinta-se à vontade para contribuir e aprimorar o código! 🚀

