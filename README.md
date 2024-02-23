# Market Analysis

## Notebooks

### Sazonalidade Milho

Análise de sazonalidade intra-anual do milho através dos preços médios diários apresentados durante um período de 5 anos, tendo o Meta Trader 5 como fonte dos dados, conforme `notebooks/sazonalidade_dia_sequencial_milho.ipynb`.


### Sazonalidade Dólar

Análise de sazonalidade intra-mensal do dólar através dos preços médios diários apresentados durante um período de 5 anos, tendo o Meta Trader 5 como fonte dos dados, conforme `notebooks/sazonalidade_intra_mensal_dolar.ipynb`.


### Fundamentus

Script de leitura de dados das empresas listadas no site http://fundamentus.com.br/, viabilizando uma análise mais automatizada de valores fundamentalista destas empresas, conforme `notebooks/fundamentus.ipynb`.  

Exemplo de dados exportados podem ser consultados no arquivo `outputs/fundamentus.csv` (verifique data da exportação).

### Status Invest

Script de leitura de dados das empresas listadas no site http://statusinvest.com.br/, viabilizando uma análise mais automatizada de valores fundamentalista destas empresas, conforme `notebooks/statusinvest.ipynb`.  

Exemplo de dados exportados podem ser consultados no arquivo `outputs/fundamentus.csv` (verifique data da exportação).

### Fundamentei

Script de leitura de dados das empresas disponíveis no site http://fundamentei.com.br/, viabilizando filtragem de empresas baseados nas informações de 'segmento de listagem', 'Tag Along por tipo de ações', 'Free Float por tipo de ação' e também pelas 'notas de usuários' da plataforma, conforme `notebooks/fundamentei.ipynb`.  

### Stocks Filter and Pre Analysis

v1 - Script faz leitura dos arquivos resultantes dos scripts 'Fundamentus', 'Status Invest' e 'Fundamentei', realizando filtros e pré-analises automatizadas baseadas em parametros.

v2 - Script faz leitura dos dados diretamente dos sites 'Status Invest' e 'Fundamentei', realizando pré-filtros e entregando um arquivo somente com as melhores, a serem então filtradas manualmente (filtrando somente as melhores por cada setor, ou confirme o investidor desejar frente aos indicadores apresentados).
