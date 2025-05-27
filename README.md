# AnaliseDeSentimentosB3

No contexto do mercado financeiro, a informação exerce um papel fundamental na tomada de decisão dos investidores. Com a ampla disponibilidade de notícias e relatórios, torna-se cada vez mais desafiador filtrar e interpretar dados de forma rápida e eficiente. Nesse cenário, técnicas de Inteligência Artificial, especialmente as relacionadas ao Processamento de Linguagem Natural (PLN), ganham destaque como ferramentas poderosas para automatizar a análise textual e extrair insights relevantes.

Este projeto tem como objetivo investigar a influência do sentimento presente em notícias financeiras sobre a precificação de ativos negociados na Bolsa de Valores brasileira. A hipótese central é que o conteúdo emocional de uma notícia, seja ele positivo, neutro ou negativo, pode impactar o comportamento dos investidores e, consequentemente, refletir nos preços dos ativos.

Para isso, utilizamos o modelo FinBERT-PT-BR, uma adaptação para o português do modelo FinBERT, que foi treinado especificamente para a análise de sentimentos em textos do domínio financeiro. Com ele, foi possível classificar automaticamente centenas de notícias com base em seu sentimento predominante.

A partir das classificações geradas, buscamos relacionar a evolução dos sentimentos com os retornos diários das ações da PETR4, uma das mais negociadas na B3. A análise considerou tanto a distribuição dos sentimentos ao longo do tempo quanto a correlação estatística entre essas variações e os movimentos do mercado.

Dessa forma, este trabalho propõe uma abordagem inovadora para compreender o papel das notícias no comportamento dos investidores, utilizando Inteligência Artificial como aliada na interpretação de grandes volumes de informação textual.

