
# Automação no Portal SEFAZ MA

## Descrição

Este projeto realiza a automação do acesso e consulta de informações no Portal da Secretaria da Fazenda do Maranhão (SEFAZ-MA). Utilizando o framework BotCity e a biblioteca `webdriver_manager`, o bot navega pela interface web do portal, interage com os elementos da página e preenche formulários automaticamente, incluindo campos como IE da empresa, CPF do sócio, número do protocolo DIEF e períodos de consulta.

## Funcionalidades

- Acesso ao Portal SEFAZ-MA e navegação automatizada entre páginas.
- Preenchimento automático de dados (IE da empresa, CPF do sócio, DIEF).
- Inserção de datas específicas para consulta.
- Uso de comandos JavaScript para manipular diretamente elementos como campos de data.
- Redirecionamento por meio de múltiplos iframes e cliques em botões dentro da interface.

## Estrutura do Projeto

```bash
/
├── resources/
│   ├── botao_NF-E.png
│   ├── botao_redirecionamento.png
│   ├── btt_fechar.png
│   ├── bttn_fechar.png
│   ├── data_final.png
│   ├── data_inicial.png
│   ├── dia1.png
│   ├── dia2.png
│   ├── inicial.png
│   ├── primeiro_redirecionamento.png
│   ├── redirecionamento_principal.png
│   ├── start.png
├── .gitignore
├── Bot_Portal_SEFAZ_MA.botproj      # Arquivo de configuração do projeto BotCity
├── bot.py                           # Código principal da automação
├── build.bat                        # Script de build para Windows
├── build.ps1                        # Script de build para PowerShell
├── build.sh                         # Script de build para Linux/macOS
├── captcha.png                      # Imagem de exemplo de captcha
├── readme.md                        # Documento README com instruções
├── requirements.txt                 # Arquivo com as dependências do projeto
├── Semtitulo.png
└── teste.png
```

- **`resources/`**: Contém todas as imagens usadas para localizar os elementos da página (botões, campos de datas, etc.) através de matching de imagem.
- **`bot.py`**: Arquivo Python que contém toda a lógica de automação, incluindo a navegação no portal e o preenchimento dos campos.
- **`requirements.txt`**: Dependências Python necessárias para o funcionamento do bot.

## Tecnologias Utilizadas

- **[BotCity Web](https://botcity.dev/)**: Framework utilizado para automação de processos repetitivos em interface web.
- **[webdriver-manager](https://pypi.org/project/webdriver-manager/)**: Gerenciador do driver para navegação com Google Chrome.
- **[BotCity Maestro](https://botcity.dev/maestro)**: Plataforma de orquestração e monitoramento de bots.

## Como Funciona

1. O bot acessa a página inicial do Portal SEFAZ-MA.
2. Um fluxo de redirecionamento é seguido, clicando em diversos botões até acessar o formulário desejado.
3. O formulário é preenchido automaticamente com o IE da empresa, CPF do sócio, DIEF e o período de consulta (datas de início e fim).
4. O JavaScript é utilizado para preencher campos de data diretamente, evitando eventuais limitações de interação com o calendário.
5. Após o preenchimento, o bot limpa o formulário e finaliza o processo.

## Requisitos de Instalação

Certifique-se de instalar todas as dependências necessárias antes de executar o projeto:

```bash
pip install --upgrade -r requirements.txt
```

Caso tenha problemas com dependências, certifique-se de estar utilizando o mesmo interpretador Python em sua IDE e no ambiente de execução do bot.

## Uso

Para rodar a automação:

1. Execute o script principal `bot.py`:

   ```bash
   python bot.py
   ```
2. O bot irá abrir uma janela do navegador, onde você poderá visualizar a automação em ação.
