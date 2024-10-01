## Índices
* [Objetivo](#Objetivo)
* [Requisitos do Projeto](#RequisitosdoProjeto)
  *  [Requisitos Funcionais](#RequisitosFuncionais)
  *  [Requisitos Não Funcionais](#RequisitosNãoFuncionais) 
* [Infraestrutura](#Infraestrutura)
* [Tecnologias Utilizadas](#TecnologiasUtilizadas)
* [Alertas e recomendações](#AlertaseRecomendações)


# Objetivo
Este projeto tem como objetivo recomendar dentre vários produtos, produtos similares utilizando um produto base. Com foco em aumentar as vendas em casos de falta de um produto específico, podendo ser substituído por outro que se encontra disponível e que tenha alguma similaridade com o item faltante.


# Requisitos do Projeto
## Requisitos Funcionais

## Requisitos Não Funcionais


# Infraestrutura

# Tecnologias Utilizadas
Back-End:
  * Python
    * Poetry
      * Flask
      * SkLearn
      * Pandas
      * Numpy
      * Re
     
      
Front-End:
 * Angular
 * Axios
 * HTML
 * CSS

   
Banco de dados:
  * SQL Server


  # Banco de dados
  > [!WARNING]
  > Este projeto utiliza SQL Server. Para configurar o banco de dados
  1. Baixe o SQL Server neste link: https://www.microsoft.com/pt-br/sql-server/sql-server-downloads
  2. Inicie sua instância do SQL Server.
  3. Abra o arquivo conf.ini que tem de exemplo e preencha cada variável necessária na classe ConfiguracaoBancoDados.
     * As variáveis que devem ser preenchidas são:
       * DRIVER | Exemplo = ODBC Driver 17 for SQL Server
       * SERVER | Exemplo = localhost
       * DATABASE | Exemplo = RecomendacaoProdutos
  5. Após isto inicie a API, verifique se o inicia da API não está retornando nenhum erro sobre o banco de dados.
  

# Configurações iniciais
Para clonar o repositório, você precisa ter o Git Bash, GitHub Desktop ou se preferir pode clonar o projeto via CURL/WGET.

1. Faça o clone do repositório
    * Git Bash: git clone https://github.com/AmarildoZoletJunior/ProjetoTCCPrivado.git
    * Curl: curl -L https://github.com/AmarildoZoletJunior/ProjetoTCCPrivado/archive/refs/heads/master.zip --output ProjetoTCCPrivado.zip
2. Para instalar todas as dependências do poetry, inicie um cmd apontado para a pasta principal do projeto.
    * Digite `pip install poetry`
    * Após o download, verifique se foi feito o download 100% sem erros.
    * Digite `poetry install` e verifique se foi instalado 100% sem erros.

# Alertas e Recomendações
> [!WARNING]
> As recomendações dependem 100% da qualidade dos dados, a recomendação leva em consideração as principais features como descrição, quantidade na embalagem, tipo de embalagem e marca. Então é necessário uma base com pelo menos 02(Dois) itens de cada seção.

> [!CAUTION]
> Para realizar novos treinamentos, somente é aceito arquivos CSV. Caso não seja importado arquivo no formato CSV, não será gerado um novo modelo treinado.

# Contribuições
> [!NOTE]
> Para contribuir com este projeto, abra um pull request para que possamos analisar suas edições e aprovar/rejeitar.

