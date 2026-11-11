# ChatBot Personalizado

Agente conversacional desenvolvido em Python utilizando Microsoft Foundry,
Azure AI Projects e a OpenAI Responses API.

## Pré-requisitos

- Windows PowerShell
- Python 3.14 ou superior
- Azure CLI
- Acesso ao projeto no Microsoft Foundry
- Um agente configurado no Microsoft Foundry

## Instalação

Clone o repositório:

```powershell
git clone https://github.com/Rafaelsecond/ChatBot-Personalizado.git
cd ChatBot-Personalizado
```

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Configuração

Crie o arquivo `.env` a partir do modelo:

```powershell
Copy-Item .env.example .env
```

Se o arquivo `.env` já existir, edite-o sem substituí-lo.

Configure as variáveis:

```env
FOUNDRY_PROJECT_ENDPOINT=https://<resource-name>.services.ai.azure.com/api/projects/<project-name>
FOUNDRY_AGENT_NAME=<agent-name>
```

O endpoint deve ser o endpoint-base do projeto e terminar em:

```text
/api/projects/<project-name>
```

Não inclua no endpoint o caminho específico do agente, como
`/agents/<agent-name>/endpoint/protocols/openai/`.

> Nunca publique o arquivo `.env`. Ele pode conter informações sensíveis e é
> ignorado pelo Git.

## Autenticação no Azure

Faça login pelo Azure CLI:

```powershell
az login
```

O projeto utiliza `DefaultAzureCredential` para localizar as credenciais
disponíveis no ambiente.

## Execução

Com o ambiente virtual ativo, execute:

```powershell
python run_agent.py
```

Digite uma mensagem quando o programa solicitar.

## Estrutura do projeto

- `run_agent.py`: executa o agente conversacional.
- `requirements.txt`: lista de dependências Python.
- `.env.example`: modelo das variáveis de ambiente.
- `install.ps1`: script de instalação do ambiente.
- `INSTRUCTIONS.md`: instruções complementares do projeto.

Os arquivos `.env` e `.venv` são locais e não devem ser enviados ao GitHub.

## Solução de problemas

### Variáveis de ambiente ausentes

Confirme se o arquivo `.env` contém:

```env
FOUNDRY_PROJECT_ENDPOINT=...
FOUNDRY_AGENT_NAME=...
```

Depois de alterar o `.env`, feche e reabra o terminal ou reinicie o VS Code.

### Erro de autenticação

Execute:

```powershell
az login
```

Depois tente executar o agente novamente.

### Erro 404

Confirme se `FOUNDRY_PROJECT_ENDPOINT` aponta para o endpoint-base do projeto:

```text
https://<resource-name>.services.ai.azure.com/api/projects/<project-name>
```

O endpoint não deve conter o caminho específico do agente.

### Dependências inconsistentes

Execute:

```powershell
python -m pip install -r requirements.txt
python -m pip check
```

## Próximos passos

- Organizar e versionar as instruções do agente.
- Adicionar uma base de conhecimento.
- Implementar RAG utilizando Azure AI Search ou recursos gerenciados do
  Microsoft Foundry.
- Adicionar testes automatizados.
- Configurar validações automáticas no GitHub Actions.
