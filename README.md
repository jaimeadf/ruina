# Ruína
Ruina Is Not an Agendator

Um script feito em [Python](https://www.python.org) para automaticamente agendar suas refeições nos restaurantes universitários da [UFSM](https://www.ufsm.br).

## Como funciona?
Ruína executa diariamente as 7 horas da manhã utilizando o [GitHub Actions](https://github.com/features/actions).
Ele lê seu cronograma definido no arquivo `config.yaml` e, por meio do aplicativo da UFSM, agenda todas as refeições
programadas para o dia posterior. Além disso, sempre que ocorrer algum erro durante os agendamentos, o [GitHub](https://github.com)
mandará um e-mail para você avisando que o script falhou.

## Como usar?
1. Crie um fork desse repositório e, dentro dele, siga as instruções seguintes.
2. Edite o arquivo `config.yaml` para se adequar ao seu cronograma (veja [Configuração](#Configuração)).
3. Dentro da aba `Settings`, seção `Secret and Variables` e item `Actions`, adicione duas secrets:
    - `Username`: Contendo sua matrícula da UFSM.
    - `Password`: Contendo sua senha da UFSM.
    - As secrets somente podem ser alteradas. Nem ninguém nem mesmo você terá acesso ao valor depois de adicionada.
    ![settings-guide](https://github.com/jaimeadf/agendator/assets/40345645/0641bf03-d5fd-45ad-9193-27dbaa8fe76d)
4. Dentro da aba `Actions`, clique em ativar workflows.
    ![actions-guide](https://github.com/jaimeadf/agendator/assets/40345645/d1efb8c1-6ccf-47c5-95cc-cd48a885c71c)
6. Pronto, a partir de agora, Ruína irá executar diariamente e agendar as suas refeições do dia seguinte. Você pode ver as logs e
executá-lo manualmente na aba `Actions`.

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
