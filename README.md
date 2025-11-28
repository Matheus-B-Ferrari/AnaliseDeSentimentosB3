# Análise de Sentimento na Precificação de Ativos na Bolsa Brasileira

## Autores
- **Felipe da Silva Morishita Garbi**
- **Matheus Barbosa Ferrari**
- **Rogério de Oliveira** - *Orientador do projeto*

### [Artigo Completo](https://github.com/Matheus-B-Ferrari/AnaliseDeSentimentosB3/blob/main/Análise_de_Sentimento_na_Precificação_de_Ativos_na_Bolsa_Brasileira.pdf)

## Resumo

Este trabalho investiga o impacto da análise de sentimento de notícias financeiras na previsão de preços de ações da Bolsa de Valores Brasileira (B3). O objetivo é avaliar se a incorporação de features de sentimento extraídas através do FinBERT-PT-BR melhora a capacidade preditiva de modelos de aprendizado de máquina.

Foram coletadas 8.762 notícias de três portais brasileiros (Exame, Infomoney e Valor Econômico) entre maio e setembro de 2025, classificadas quanto ao sentimento e integradas aos dados históricos de preços de quatro ativos (PETR4, VALE3, EMBR3, BOVA11). Os modelos LSTM e SVR foram treinados com diferentes janelas temporais (7 e 14 dias) e horizontes de previsão (1, 2 e 5 dias).

Os principais resultados demonstram que o sentimento midiático pode complementar modelos quantitativos, especialmente em arquiteturas que exploram relações temporais nativamente, como a LSTM, com melhorias de até 38% no erro de previsão para horizontes de 5 dias.

## Dados

### Coleta de Notícias

O conjunto de dados foi construído através de coleta automatizada diária via GitHub Actions, executada às 23h30 (UTC-3). Foram utilizadas duas abordagens:
- **RSS Feeds**: Para portais Exame e Infomoney
- **Web Scraping**: Para Valor Econômico (BeautifulSoup4)

**Período**: 01/05/2025 a 01/09/2025 (4 meses)  
**Total de notícias**: 8.762

<br>
<img src="https://raw.githubusercontent.com/Matheus-B-Ferrari/AnaliseDeSentimentosB3/main/images/noticias_por_portal.png" width="600">
<br>

### Dados de Mercado

Dados históricos (open, high, low, close, volume) obtidos via biblioteca yfinance:
- **Ativos analisados**: PETR4.SA, VALE3.SA, EMBR3.SA, BOVA11.SA
- **Período**: Maio a setembro de 2025
- **Total de pregões**: 85 dias úteis



## Modelos Utilizados

#### LSTM (Long Short-Term Memory)
- 1 camada LSTM com 64 neurônios
- Dropout de 20%
- Camada densa intermediária (32 neurônios, ReLU)
- Camada de saída (1 neurônio, ativação linear)
- Otimizador: Adam (α = 0.001)
- Loss: MAE
- Épocas: 100, Batch size: 8

#### SVR (Support Vector Regression)
- Kernel: RBF
- Parâmetro C = 1.0
- Gamma: 'scale' (adaptativo)

## Resultados

### LSTM

<img width="846" height="238" alt="image" src="https://github.com/user-attachments/assets/951f9fe9-e0f3-45b5-9e40-24debaa1b6c6" />


### SVR

<img width="831" height="221" alt="image" src="https://github.com/user-attachments/assets/e9ba8dde-dd56-4f82-a229-443e9cc9504c" />



### Comparação entre Modelos

<img width="842" height="119" alt="image" src="https://github.com/user-attachments/assets/846f30f9-e481-4c92-be91-fa2ae6a95a0f" />



## Conclusão

Este estudo demonstra que a integração de análise de sentimento com modelos de aprendizado de máquina pode melhorar significativamente a previsão de preços de ativos na B3, especialmente quando:
- Utilizam-se arquiteturas que exploram relações temporais (LSTM)
- O horizonte de previsão permite tempo para o sentimento afetar preços (≥ 2 dias)
- O ativo analisado é um índice agregado (BOVA11)

A disponibilização pública da base de notícias e do código-fonte contribui para o avanço da pesquisa em finanças comportamentais no contexto brasileiro.

## Trabalhos Futuros

- Expansão da base de dados com mais fontes e períodos
- Reconhecimento de entidades para aplicar sentimento específico por ativo
- Testes com outros modelos (XGBoost, Transformers, GRU)
- Validação out-of-sample e backtesting em ambiente real
- Análise de diferentes formas de agregação (média ponderada, decaimento temporal)

## Referências

[1] Santos, L., Bianchi, R., & Costa, A. (2023). FinBERT-PT-BR: Análise de sentimentos de textos em português do mercado financeiro. Brazilian Workshop on Artificial Intelligence in Finance.

[2] Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. The Journal of Finance, 62(3), 1139-1168.

[3] Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735-1780.

[4] Vieira, J. E. A. L. (2025). Modelo preditivo para precificação de ativos com integração de notícias do mercado financeiro e técnicas de machine learning. FGV.

---

**Faculdade de Computação e Informática (FCI)**  
**Universidade Presbiteriana Mackenzie**  
**2025**
