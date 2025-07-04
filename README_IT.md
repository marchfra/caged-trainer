# CAGED Trainer

Genera un accordo e verifica se i modi scelti dall'utente sono modi validi che l'accordo può armonizzare.

## Indice

- [Installazione](#installazione)
    - [macOS](#macos)
    - [Windows](#windows)
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

### Windows

1. Scarica il più recente `CAGED_Trainer_Setup.exe` dalla pagina [Releases](https://github.com/marchfra/caged-trainer/releases).
2. Apri il file `CAGED_Trainer_Setup.exe` e segui le istruzioni sullo schermo per installare l'applicazione.
3. Al termine dell'installazione troverai **CAGED Trainer** nel menu Start ed eventualmente come shortcut sul desktop, se hai scelto di crearlo durante l'installazione. Potrai disinstallarlo in ogni momento da **Impostazioni** &rarr; **App**.

#### Se appare il messaggio "PC protetto da Windows"

Poiché l'app non è firmata digitalmente, potresti vedere un avviso SmartScreen quando cerchi di avviare l'installazione:

1. Clicca su **"Ulteriori informazioni"**.
2. Poi clicca su **"Esegui comunque"** per avviare l'installazione.

Questo è un avviso comune per app nuove o non firmate, e non indica che il file sia dannoso.

#### Se Microsoft Defender blocca l'app

1. Apri il menu **Start** e cerca **"Sicurezza di Windows"**
2. Vai su **"Protezione da virus e minacce"**
3. Clicca su **"Cronologia della protezione"**
4. Trova l'avviso recente relativo a questa app (potrebbe dire "Minaccia in quarantena" o "Minaccia bloccata").
5. Cliccaci sopra e scegli **"Consenti sul dispositivo"** o **"Ripristina"**
6. Dopo averla sbloccata, prova a eseguire di nuovo l'app.

Dopo questa prima autorizzazione, Windows permetterà l'esecuzione dell'app normalmente.

### Esecuzione dal codice sorgente (macOS / Linux / Windows)

Se non stai usando macOS o Windows, o preferisci eseguire l'app dal sorgente, segui questi passaggi:

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
