# Localizador de telefones

## Descrição geral

Este projeto é um localizador de telefones que permite aos usuários buscar e encontrar números de telefone. Abaixo está uma descrição das principais pastas do projeto:

- **fonts**: Contém fontes utilizadas na interface do usuário.
- **logs**: Armazena arquivos de log que registram eventos e erros do sistema.
- **out**: Diretório onde são gerados os arquivos de saída, como relatórios ou resultados de buscas.
- **src**: Contém o código-fonte do projeto, incluindo scripts e módulos principais.
- **web_interface**: Inclui arquivos relacionados à interface web do projeto, como HTML, CSS e JavaScript.

## Executar localmente
Para executar o projeto localmente, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter os seguintes itens instalados em seu computador:
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Passo a passo

1. **Navegue até o diretório do projeto**:
    ```sh
    cd seu-repositorio
    ```
2. **Crie um ambiente virtual**: É uma boa prática criar um ambiente virtual para gerenciar as dependências do projeto. Execute os comandos abaixo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

5. **Execute o projeto**: Agora você pode executar o projeto. Dependendo da estrutura do projeto, o comando pode variar. Um exemplo comum seria:
    ```sh
    python run.py
    ```

### Testando o projeto

Para testar o projeto, vá até o navegador coloque o seu IP + porta padrão da aplicação ( porta 5000 ):
```sh
seu_ip:5000
```
Em seguida aperte o botão para executar e aguarde que apareça concluído

### Acompanhando a execução

- **Logs**: Verifique os arquivos na pasta `logs` para acompanhar eventos e erros registrados durante a execução.
- **Saída**: Os resultados das buscas e relatórios serão gerados na pasta `out`.

Seguindo esses passos, você conseguirá rodar, usar, testar e acompanhar a execução do projeto localmente.

### Observações importantes

- **Entrada**: O bot sempre irá buscar dados no Google das empresas que estiverem em `fonts` no arquivo `empresas.csv`






## Conhecimentos necessários para a aplicação

- Conhecimentos gerais de desenvolvimento de software
- Conhecimentos gerais de Aplicação Web
- Conhecimentos gerais de Web Scraping
- Conhecimentos gerais de manipulação de dados estruturados
- Conhecimentos gerais de manipulação de arquivos CSV
- Conhecimentos especificos de Python
- Conhecimentos especifico de Flask para aplicação Web
- Conhecimentos especifico de Pandas para Manipular dado estruturado e arquivo CSV
- Conhecimentos especificos de BS4 e requests para Web Scraping

## Regras de negócios usadas para a aplicação

- Para a aplicação não foram desenvolvidas muitas regras de negócios usando o minimo aceitável para definição.
- Para fins de definição de regras de negócio foi entendido que telefones de contato de uma empresa possui uma das 3 características:
    1. Possui (XX) X XXXX-XXXX ou (XX) XXXX-XXXX ou (XX) XXX-XXXX seria DDD (dois dígitos que representa lugar na UF), 3 ou 4 dígitos um hifen e 4 dígitos, podendo ou não ter um identificador fixo ou móvel
    2. 0800XXX-XXXX ou 4004XXX-XXX: seriam números comerciais contratados

## Procedimento para o desenvolvimento do projeto

1. Localização dos problemas associados: tentar descobrir telefone de contato de empresas buscando no Google.
2. Desenho do formato para correção do problema: selecionar empresa e localidade da empresa; buscar no google; localizar os telefones; entender o padrão de telefones no google; extrair os telefones; salvar os telefones.
3. Localizar formato de correção em larga escala: puxar empresas de um CSV; localizar empresa no google e extrair os dados necessários; salvar em um CSV
4. Permitir executar o bot a partir de aplicações WEB para facilitar uso de outras pessoas com menos conhecimento.

## Propostas de desafios

1. Tente aprimorar o Web Scraping, como você faria para localizar outras informações a partir do google.
1.1. Seria possível puxar outros dados além dos telefones (como email)?
1.2. Seria possível descobrir o site da empresa e se tiver site extrair mais informações de lá?
1.3. Seria possivel descobrir o instagram (ou outras redes) e puxar informações de lá?
2. Seria possível aprimorar a aplicação e conectar ela com esse bot de busca?
2.1. Incluir upload CSV?
2.2. Incluir opção de exportar o CSV?

