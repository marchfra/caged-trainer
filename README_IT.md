# CAGED Trainer

Genera un accordo e verifica se i modi scelti dall'utente sono modi validi che l'accordo può armonizzare.

## Indice

- [Installazione](#installazione)
    - [macOS](#macos)
    - [Esecuzione dal codice sorgente (macOS / Linux / Windows)](#esecuzione-dal-codice-sorgente-macos--linux--windows)
- [Utilizzo](#utilizzo)
    - [Interfaccia grafica](#interfaccia-grafica)
    - [Interfaccia testuale](#interfaccia-testuale)

## Installazione

### macOS

1. Scarica il più recente `CAGEDTrainer.dmg` dalla pagina [Release](https://github.com/marchfra/caged-trainer/releases).
2. Apri il file `CAGEDTrainer.dmg` e trascina l'app nella tua cartella `Applicazioni`.
3. **Importante**: siccome l'app non è firmata da uno sviluppatore certificato da Apple, macOS ne bloccherà l'esecuzione la prima volta che la apri.
    Per aprirla comunque:
    - Vai in **Impostazioni di Sistema** &rarr; **Privacy e Sicurezza**.
    - Scorri fino al messaggio che segnala che l'app è stata bloccata.
    - Clicca su **"Apri comunque"**, quindi conferma.

    Dopo la prima conferma manuale, macOS permetterà l'esecuzione dell'app normalmente.

### Esecuzione dal codice sorgente (macOS / Linux / Windows)

Se non stai usando macOS, o preferisci eseguire l'app dal sorgente, segui questi passaggi:

#### Prerequisiti

- git
- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (opzionale ma consigliato)

#### Passaggi

1. Clona la repository:

   ```shell
   git clone https://github.com/marchfra/caged-trainer.git
   cd caged-trainer
   ```

2. Crea e attiva un ambiente virtuale (solo se non usi uv):

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate  # su Windows: .venv\Scripts\activate
   pip install .
   ```

3. Avvia l'app:

    ```shell
    uv run src/gui.py  # python3 src/gui.py
    ```

    oppure, se vuoi usare l'interfaccia testuale,

    ```shell
    uv run src/main.py  # python3 src/main.py
    ```

## Utilizzo

### Interfaccia grafica

Una volta avviata l'applicazione, ti verrà mostrato un accordo insieme a una forma dell'accordo.

Sotto di esso troverai quattro sezioni, una per ciascuna scala. All'interno di ogni sezione ci sono dei checkbox per ciascun modo generato da quella scala; clicca sul checkbox se pensi che quel modo possa essere armonizzato dall'accordo visualizzato.

Quando hai finito, premi il pulsante "Check" per ottenere la risposta corretta e vedere come te la sei cavata. Per ottenere una nuova domanda, premi il pulsante "New chord".

#### Shortcut da tastiera

| Shortcut                  | Azione                                      |
|---------------------------|---------------------------------------------|
| <kbd>Enter</kbd>          | Verifica le risposte                        |
| <kbd>N</kbd>              | Nuovo accordo                               |
| <kbd>1</kbd>-<kbd>4</kbd> | Seleziona il primo checkbox della scala 1-4 |
| <kbd>Tab</kbd>            | Muoviti al prossimo checkbox                |
| <kbd>Space</kbd>          | Attiva/disattiva il checkbox selezionato    |

### Interfaccia testuale

Una volta avviata l'applicazione, ti verrà mostrato un accordo insieme a una forma dell'accordo.

Successivamente verrà mostrato un elenco di modi derivati dalla scala maggiore. Per selezionare i modi che l'accordo può armonizzare, inserisci il/i numero/i separati da uno spazio. Quando hai finito, premi <kbd>Invio</kbd>. Se pensi che non ci siano modi che l'accordo può armonizzare, premi semplicemente <kbd>Invio</kbd>.

Ripeti la procedura per ogni nuovo insieme di modi che apparirà fino a quando vedrai i risultati, quindi segui le istruzioni a schermo per ottenere un nuovo esercizio o uscire dall'app.
