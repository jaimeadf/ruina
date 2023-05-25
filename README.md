# Ruína
Ruina Is Not an Agendator

Um script feito em [Python](https://www.python.org) para automaticamente agendar suas refeições nos restaurantes universitários da [UFSM](https://www.ufsm.br).

## Como funciona?
Ruína 
a diariamente as 7 horas da manhã utilizando o [GitHub Actions](https://github.com/features/actions).
Ele lê seu cronograma definido no arquivo `config.yaml` e, por meio do aplicativo da UFSM, agenda todas as refeições
programadas para o dia posterior. Além disso, sempre que ocorrer algum erro durante os agendamentos, o [GitHub](https://github.com)
mandará um e-mail para você avisando que o script falhou.

## Como usar?
1. Crie um fork desse repositório e, dentro dele, siga as instruções seguintes.
2. Edite o arquivo `config.yaml` para se adequar ao seu cronograma (veja [Configuração](#Configuração)).
3. Dentro da aba `Settings`, seção `Secret and Variables` e item `Actions`, adicione duas secrets:
    - `Username`: Contendo sua matrícula da UFSM.
    - `Password`: Contendo sua senha da UFSM.
    - As secrets são variáveis privadas que somente podem ser alteradas. Nem ninguém, nem mesmo você terá acesso ao seu valor, depois de adicionada.
    ![secrets-guide](https://github.com/jaimeadf/ruina/assets/40345645/5dbf88a6-238e-4bf2-a1d5-679ee9284dfe)
4. Dentro da aba `Actions`, clique em ativar workflows.
    ![enable-actions-guide](https://github.com/jaimeadf/ruina/assets/40345645/51d51b12-948b-4ff0-a651-b8e60fa01995)
6. Depois, ainda dentro dessa aba, clique em `Ruina` e ativar.
    ![enable-workflow-guide](https://github.com/jaimeadf/ruina/assets/40345645/c3a42713-0a4a-4e2f-b156-9693c62dbae4)
8. Pronto, a partir de agora, Ruína irá executar diariamente e agendar as suas refeições do dia seguinte. Você pode ver as logs e
executá-la manualmente na aba `Actions`.

> Por favor, sempre que não for almoçar, cancele o agendamento ou disponibilize a refeição.

## Configuração
A configuração é feita a partir da edição do arquivo [config.yaml](config.yaml) que contém as seguintes opções:

### Environment
> ⚠️ Não é recomendado alterar as configurações dessa seção. As informações padrões foram obtidas
> a partir da engenharia reversa do aplicativo UFSMDigital.

- `app`: O nome do aplicativo realizando o log in.
- `device-id`: O identificador único do dispositivo.
- `device-info`: Informações sobre o dispositivo, incluindo o tipo e o sistema operacional.
- `message-token`: Uma constante que não descobri a utilidade.

### Schedules
A seção de `schedules` permite você definir uma lista de cronogramas para diferentes dias da semana.
Cada cronograma consiste nas seguintes opções:
- `weekday`: O dia da semana para o cronograma (por exemplo, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
- `restaurant`: O restaurante associado ao agendamento (1 para o RU I e 2 para o RU II).
- `vegetarian`: Se o agendamento será com a opção vegetariana (true ou false).
- `coffee`: Se o agendamente inclui o café da manhã (true ou false).
- `lunch`: Se o agendamento inclui o almoço (true ou false).
- `dinner`: Se o agendamento inclui a janta (true ou false).

## Agradecimentos
Obrigado, [@guikage](https://github.com/guikage) pela ideia de nome.

<hr />

Desenvolvido com ☕ por [@jaimeadf](https://github.com/jaimeadf) para propósitos educacionais.
