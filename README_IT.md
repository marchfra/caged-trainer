# CAGED Trainer

Genera un accordo e verifica se l'elenco di modi forniti dall'utente contiene modi validi che l'accordo può armonizzare.

## Indice

- [Installazione](#installazione)
    - [File binario](#file-binario)
    - [Codice sorgente](#codice-sorgente)
- [Esecuzione dell'applicazione](#esecuzione-dellapplicazione)
    - [File binario](#file-binario-1)
    - [Codice sorgente](#codice-sorgente-1)
- [Utilizzo](#utilizzo)

## Installazione

### File binario

Il file binario compilato è disponibile solo per macOS.

Per scaricarlo, vai alla [pagina Release](https://github.com/marchfra/caged-trainer/releases) e clicca su **caged-trainer** (quello con un piccolo cubo alla sua sinistra).

Per poter aprire l'applicazione, apri il Terminale (puoi trovarlo in Applicazioni > Utility, oppure scrivendo "Terminale" in Spotlight) e digita le seguenti righe, premendo Invio dopo ciascuna:

```shell
xattr -d com.apple.quarantine '/percorso/del/file/caged-trainer'
```

Questo comando rimuove l'attributo "quarantena" che macOS applica ai file scaricati da internet. Rimuovere questo attributo consente all'app di funzionare senza avvisi di sicurezza. **Usa questo comando solo per file di cui ti fidi.**

```shell
chmod +x '/percorso/del/file/caged-trainer'
```

Questo comando rende il file eseguibile come programma. Senza questo permesso, cercando di eseguire il file potresti non ottenere alcun risultato oppure aprirlo in un editor di testo. Usa questo comando se vuoi essere in grado di eseguire il file.

Per impostazione predefinita, il percorso `/percorso/del/file/caged-trainer` dovrebbe essere `~/Downloads/caged-trainer`, ma se non sei sicuro del percorso dell'applicazione puoi trascinare il file dell'app nella finestra del Terminale al posto di scrivere il percorso. Questo inserirà automaticamente il percorso corretto.

Potrebbe esserti chiesta la password.

Ora puoi spostare il file dell'applicazione dove preferisci, e anche crearne copie.

## Codice sorgente

Puoi ottenere il codice sorgente compresso dalla [pagina Release](https://github.com/marchfra/caged-trainer/releases).

Per eseguire l'applicazione dal codice sorgente hai bisogno di un'installazione di Python. Se non hai Python installato, puoi scaricarlo da [python.org](https://python.org).

## Esecuzione dell'applicazione

### File binario

Per avviare l'app, è sufficiente fare doppio clic su di essa. Si aprirà una finestra del Terminale; è normale, l'applicazione viene eseguita all'interno del Terminale.

### Codice sorgente

**Usando `uv` (consigliato)**: se hai `uv` installato, esegui l'applicazione con

```shell
uv run main.py
```

Se non conosci `uv`, puoi saperne di più [qui](https://github.com/astral-sh/uv), oppure semplicemente usare il comando `python3` come mostrato sotto.

**Usando python**: esegui l'applicazione con

```shell
python3 main.py
```

## Utilizzo

Una volta avviata l'app, ti verrà mostrato un accordo insieme a una forma dell'accordo.

Successivamente verrà mostrato un elenco di modi derivati dalla scala maggiore. Per selezionare i modi che l'accordo può armonizzare, inserisci il/i numero/i separati da uno spazio. Quando hai finito, premi Invio. Se pensi che non ci siano modi che l'accordo può armonizzare, premi semplicemente Invio.

Ripeti la procedura per ogni nuovo insieme di modi che apparirà fino a quando vedrai i risultati, quindi segui le istruzioni a schermo per ottenere un nuovo esercizio o uscire dall'app.
