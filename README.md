# Market Analysis


### Sazonalidade Milho

Análise de sazonalidade do milho através dos preços médios diários apresentados durante um período de 5 anos, conforme `sazonalidade_dia_sequencial_milho.ipynb`.


### Scraper Fundamentus

Scraper para ler/coletar automaticamente dados de todas as empresas listadas no site http://fundamentus.com.br/, viabilizando uma análise mais automatizada dos valores fundamentalista destas empresas, conforme `scraper_fundamentus.ipynb`.  

Exemplo de dados exportados podem ser consultados no arquivo `scraper_fundamentus.csv` (dados exportados em 12 de abril de 2020).


### Scraper Suno Analítica

Scraper para ler/coletar histórico de dados fundamentalistas (demonstração de resultados, balanço patrimonial e demonstrativo de fluxo de caixa) apresentados no site https://www.sunoresearch.com.br/acoes/, possibilitando uma análise fundamentalista automatizada, conforme `scraper_suno_analitica.ipynb`.

**Atenção:** Futuramento poderá ser implementada a leitura de dados dos indicadores históricos.  
Infelizmente, muitos destes indicadores são calculados considerando a quantidade de ações, algo que a plataforma está calculando erroneamente (o cálculo na data de hoje: 18 de abril de 2020, é feito considerando somente a quantidade de ações do ticker consultado, e não sobre todas as ações existentes da empresa *ON + PN*, acarretando assim na apresentação de informações não incorretas).
