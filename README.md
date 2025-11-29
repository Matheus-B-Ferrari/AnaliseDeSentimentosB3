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

## [Dados](https://github.com/Matheus-B-Ferrari/AnaliseDeSentimentosB3/blob/main/Coleta_e_Processamento.ipynb)

### Coleta de Notícias

O conjunto de dados foi construído através de coleta automatizada diária via GitHub Actions, executada às 23h30 (UTC-3). Foram utilizadas duas abordagens:
- **RSS Feeds**: Para portais Exame e Infomoney
- **Web Scraping**: Para Valor Econômico (BeautifulSoup4)

**Período**: 01/05/2025 a 01/09/2025 (4 meses)  
**Total de notícias**: 8.762




<img width="1390" height="490" alt="image" src="https://github.com/user-attachments/assets/e2d0f688-d1cf-4f1b-bc7c-099b9e7deff7" />

<img width="690" height="490" alt="image" src="https://github.com/user-attachments/assets/e1753035-0bf6-43d2-8233-b1b191d2c14a" />



### Dados de Mercado

Dados históricos de fechamento dos preços obtidos via biblioteca yfinance:
- **Ativos analisados**: PETR4.SA, VALE3.SA, EMBR3.SA, BOVA11.SA
- **Período**: Maio a setembro de 2025
- **Total de pregões**: 85 dias úteis



<img width="533" height="188" alt="image" src="https://github.com/user-attachments/assets/7c69609d-9902-4b92-88dd-c8b13dc2d825" />


## Modelos Utilizados

#### [LSTM (Long Short-Term Memory)](https://github.com/Matheus-B-Ferrari/AnaliseDeSentimentosB3/blob/main/TCC_Unificado_LSTM.ipynb)
- 1 camada LSTM com 64 neurônios
- Dropout de 20%
- Camada densa intermediária (32 neurônios, ReLU)
- Camada de saída (1 neurônio, ativação linear)
- Otimizador: Adam (α = 0.001)
- Loss: MAE
- Épocas: 100, Batch size: 8

#### [SVR (Support Vector Regression)](https://github.com/Matheus-B-Ferrari/AnaliseDeSentimentosB3/blob/main/TCC_Unificado_SVR.ipynb)
- Kernel: RBF
- Parâmetro C = 1.0
- Gamma: 'scale' (adaptativo)

## Resultados

### LSTM

<img width="846" height="238" alt="image" src="https://github.com/user-attachments/assets/951f9fe9-e0f3-45b5-9e40-24debaa1b6c6" />

<img width="1183" height="584" alt="image" src="https://github.com/user-attachments/assets/bda30d27-4aab-49d3-ba6c-36e4b1ef14c8" />

<img width="1381" height="779" alt="image" src="https://github.com/user-attachments/assets/4a86a826-1576-4ab6-ad18-0d3d7e8e39a4" />


### SVR

<img width="831" height="221" alt="image" src="https://github.com/user-attachments/assets/e9ba8dde-dd56-4f82-a229-443e9cc9504c" />

<img width="1183" height="584" alt="image" src="https://github.com/user-attachments/assets/3ccdf8fc-f9fa-4eb7-8985-5e4ab298777d" />

<img width="1381" height="779" alt="image" src="https://github.com/user-attachments/assets/b2c87855-f61e-4e18-8845-df4132830e77" />



### Comparação entre Modelos

<img width="842" height="119" alt="image" src="https://github.com/user-attachments/assets/846f30f9-e481-4c92-be91-fa2ae6a95a0f" />


BOVA11.SA obteve a maior taxa de melhoria estatisticamente significante




## Conclusão

Este estudo demonstra que a integração de análise de sentimento com modelos de aprendizado de máquina pode melhorar significativamente a previsão de preços de ativos na B3, especialmente quando:
- Utilizam-se arquiteturas que exploram relações temporais (LSTM)
- O horizonte de previsão permite tempo para o sentimento afetar preços (≥ 2 dias)
- O ativo analisado é um índice agregado (BOVA11)

O uso do FinBERT-PT-BR preenche uma lacuna na literatura brasileira ao incorporar informações subjetivas de forma sistemática. A disponibilização do código e da base tratada contribui para o avanço da pesquisa em finanças computacionais no país.

Trabalhos futuros incluem ampliar o conjunto de dados, aplicar sentimento por ativo via NER e testar modelos adicionais como XGBoost e RNNs alternativas.


## Referências

[1] ARACI, D. FinBERT: Financial Sentiment Analysis with Pre-trained Language Models. 2019. Disponível em: https://arxiv.org/abs/1908.10063.

[2] BARBER, B. M.; ODEAN, T. All that glitters: The effect of attention and news on the buying behavior of individual and institutional investors. The Review of Financial Studies, Oxford University Press, v. 21, n. 2, p. 785–818, 2008.

[3] DEVLIN, J. et al. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. 2019. Disponível em: https://arxiv.org/abs/1810.04805.

[4] DRUCKER, H. et al. Support vector regression machines. In: MOZER, M.; JORDAN, M.; PETSCHE, T. (Ed.). Advances in Neural Information Processing Systems. MIT Press, 1996. v. 9. Disponível em: https://proceedings.neurips.cc/paper_files/paper/1996/file/d38901788c533e8286cb6400b40b386d-Paper.pdf.

[5] FAMA, E. F. Efficient capital markets: A review of theory and empirical work. The Journal of Finance, Wiley Online Library, v. 25, n. 2, p. 383–417, 1970.

[7] GU, W. jun et al. Predicting stock prices with finbert-lstm: Integrating news sentiment analysis. In: Proceedings of the 2024 8th International Conference on Cloud and Big Data Computing. ACM, 2024. (ICCBDC 2024), p. 67–72. Disponível em: http://dx.doi.org/10.1145/3694860.3694870.

[8] HALDER, S. FinBERT-LSTM: Deep Learning based stock price prediction using News Sentiment Analysis. 2022. Disponível em: https://arxiv.org/abs/2211.07392.

[9] HOCHREITER, S.; SCHMIDHUBER, J. Long short-term memory. Neural Computation, v. 9, p. 1735–1780, nov. 1997.

[10] KASTURE, P.; SHIRSATH, K. Enhancing stock market prediction: A hybrid rnn-lstm framework with sentiment analysis. Indian Journal Of Science And Technology, v. 17, p. 1880–1888, abr. 2024.

[11] LIU, B. Sentiment Analysis and Opinion Mining. San Rafael, CA: Morgan & Claypool Publishers, 2012. (Synthesis Lectures on Human Language Technologies).

[12] RICHARDSON, L. Beautiful Soup: Python Library for HTML and XML Parsing. 2007. Disponível em: https://www.crummy.com/software/BeautifulSoup/. Acesso em: 8 nov. 2025. Versão utilizada: BeautifulSoup4.

[13] SANTOS, L.; BIANCHI, R.; COSTA, A. Finbert-pt-br: Análise de sentimentos de textos em português do mercado financeiro. In: Anais do II Brazilian Workshop on Artificial Intelligence in Finance. Porto Alegre, RS, Brasil: SBC, 2023. p. 144–155. Disponível em: https://sol.sbc.org.br/index.php/bwaif/article/view/24960.

[14] TETLOCK, P. C. Giving content to investor sentiment: The role of media in the stock market. The Journal of Finance, Wiley Online Library, v. 62, n. 3, p. 1139–1168, 2007.

[15] TETLOCK, P. C. Chapter 18 - The role of media in finance. In: ANDERSON, S. P.; WALDFOGEL, J.; STRÖMBERG, D. (Ed.). Handbook of Media Economics. North-Holland, 2015, (Handbook of Media Economics, v. 1). p. 701–721. Disponível em: https://www.sciencedirect.com/science/article/pii/B9780444636850000188.

[17] VIEIRA, J. E. A. L. Modelo preditivo para precificação de ativos com integração de notícias do mercado financeiro e técnicas de machine learning. Dissertação (Mestrado) — Fundação Getúlio Vargas (FGV), São Paulo, 2025. Disponível em: https://repositorio.fgv.br/items/ca7c23d2-302c-4477-b9fe-f4102bdc523e.
