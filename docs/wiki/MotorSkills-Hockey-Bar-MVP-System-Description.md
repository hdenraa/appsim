# MotorSkills Hockey Bar MVP system description

> Kilde: Google Drive-dokumentet **MotorSkills Hockey Bar MVP system description**  
> Formål: Repo-nær wiki-side til teknisk overblik over MVP-systemet.  
> Bemærk: GitHub-connectoren kunne ikke skrive direkte til GitHub Wiki, så denne side er oprettet som markdown i `docs/wiki/` og kan kopieres direkte til `appsim` Wiki.

## 1. Systemoverblik

MotorSkills Hockey Bar MVP består af tre hovedkomponenter:

1. **App**
   - Styrer gennemførelse af øvelser.
   - Fungerer som bro for logdata fra fysiske elementer til backend.
   - Understøtter softwareopdatering af elementer.

2. **Backend**
   - Lagrer og leverer øvelsesdefinitioner til appen.
   - Viser tilgængelige øvelser.
   - Lagrer og viser logdata.
   - Lagrer og viser brugsmetrikker.
   - Understøtter systemvedligehold.

3. **Interaktive elementer**
   - Engagerer brugeren i fysisk aktivitet.
   - Måler og rapporterer hvor godt aktiviteten udføres.

Systemets funktionalitet falder i fem hovedområder:

- Fysisk interaktion, træning og konkurrence.
- Startup og registrering af tilgængelige elementer.
- Gennemførelse af øvelser.
- Resultathåndtering.
- Supportinterface til drift, dataudtræk og vedligehold af øvelsesdefinitioner.

## 2. Fysisk interaktion

Under en øvelse sætter appen en task på et fysisk element. Brugeren løser tasken gennem fysisk aktivitet, hvorefter elementet rapporterer resultatet tilbage til appen.

Kommunikationen mellem app og elementer sker via **WebSocket over WiFi**:

- Appen starter en WebSocket-server.
- Hvert element forbinder til denne server.
- Alle enheder, der følger JSON-protokollen, kan i princippet fungere som fysisk element.

## 3. Hockey Bar-elementet

Det første og foreløbigt eneste element er **Hockey Bar**.

Når en task sættes på en bar:

- Signaliseres tasken til brugeren via NeoPixels.
- Brugeren løser tasken ved at spille pucken under baren.
- Baren registrerer puckens passage via sensorer.
- Baren vurderer om tasken er løst korrekt og rapporterer blandt andet tid, retning og hastighed.

### 3.1 Elektronik

Hockey Bar består af:

- Main PCB baseret på ESP32-S3.
- To sensor-PCB'er.
- USB-powerbank.
- LiPo UPS-batteri.

### 3.2 Firmwareområder

Firmware bør struktureres omkring følgende områder:

- Control flow.
- Exercise handling.
- WiFi og provisioning.
- Power management.
- Hardware handling:
  - Break beams.
  - Accelerometer.
  - Eksterne I2C-enheder.
  - 7-segment-display.
  - NeoPixels.
  - Push button.
- WebSocket-håndtering.
- OTA update.
- Kommunikationsprotokol og JSON-håndtering.

Særligt **exercise handling** og **eksterne I2C-enheder** bør isoleres tydeligt, da de vurderes som de mest foranderlige områder.

## 4. JSON-kommunikation

Al kommunikation mellem app og elementer er JSON-baseret.

Generelt message-format:

```json
{
  "deviceId": "xxxx",
  "messageId": null,
  "timestamp": "hh.mm.ss...",
  "elementId": 99,
  "payload": {}
}
```

Felter:

- `deviceId`: Unik ID for et element.
- `messageId`: Bruges til at korrelere svar med app-initierede beskeder.
- `timestamp`: Bruges til timing og behandlingstid.
- `elementId`: ID tildelt af appen og vist på elementets 7-segment-display.
- `payload`: Selve task- eller resultatindholdet.

Alle beskeder fra app til elementer skal indeholde en `task` i payload:

```json
{
  "task": "someTask"
}
```

Elementet kvitterer med:

```json
{
  "confirmedTask": "someTask"
}
```

## 5. Startup-flow

Startup består af app-skærme, Azure-skærme og processer:

1. Welcome screen.
2. Logon via Azure.
3. Create profile via Azure.
4. Start WebSocket-server.
5. Element provisioning.
6. Element identification handshake.
7. Element list/info screen.
8. Exercise list screen.

### 5.1 Welcome screen

Appen kræver WiFi og internetadgang. Første startup-step er derfor at validere disse forudsætninger.

Når kravene er opfyldt, kan brugeren:

- Logge ind.
- Oprette profil.
- Fortsætte anonymt med begrænset funktionalitet.

### 5.2 Logon og profil

Autentifikation og profiloprettelse håndteres af Azure-standardfunktionalitet.

Profilen kan indeholde:

- Brugercredentials.
- Preferred access point.
- User group.
- Delingsindstillinger.
- Datatilladelser.
- Foretrukne exercise parameters.

### 5.3 WebSocket-server

Efter brugeridentifikation starter appen en WebSocket-server. Dette skal ske før element provisioning, fordi elementerne skal kende serverens IP og port.

### 5.4 Element provisioning

Elementer forbindes til relevant WiFi via provisioning.

Fra appens perspektiv:

1. Prompt for WiFi-password, hvis det ikke findes i profilen.
2. Broadcast UDP-pakker med credentials via Smart Config.

Standard Smart Config skal udvides, så server-IP og port sendes sammen med WiFi-credentials.

Fra elementets perspektiv:

1. Vis `PP` på 7-segment-display og vent på provisioning.
2. Forbind til WiFi.
3. Forbind til appens WebSocket-server.
4. Start WiFi-watchdog.
5. Gå tilbage til provisioning ved fejl.

Ved forbindelsesfejl vises `EE` på 7-segment-displayet.

### 5.5 Element identification handshake

Efter provisioning identificerer elementerne sig over for appen.

Flow:

1. Element sender identification JSON til appen.
2. Appen validerer om elementet kan håndteres.
3. Appen tildeler `elementId`.
4. Elementet viser tildelt ID på 7-segment-displayet.

Eksempel på element identification JSON:

```json
{
  "connected": true,
  "type": "Port",
  "hwVersion": "1.0",
  "swVersion": "1.0"
}
```

Appen svarer med:

```json
{
  "task": "init",
  "elementId": 99
}
```

Hvis elementet afvises, returneres `elementId = -1`, og elementet viser `IE`.

## 6. Exercise list og øvelsesdefinitioner

Exercise list dannes ud fra:

- Exercise definitions fra backend.
- Exercise popularity fra backend.
- Brugerens foretrukne øvelser, hvis profil findes.
- Tilgængelige fysiske elementer.

Hvis en øvelse kræver andre eller flere elementer end de tilgængelige, vises den stadig, men i en anden farve. Den kan afprøves via screen tapping, hvor tryk på skærmen simulerer at en fysisk task er løst.

Øvelsesdefinitioner gemmes som JSON i backend.

Forenklet format:

```json
{
  "exerciseList": [
    {
      "exercise": "Random time",
      "shortDesc": "Randomly choose ports",
      "longDesc": "The ports will randomly light up...",
      "outlines": [],
      "elements": [],
      "tasks": [],
      "endCondition": {
        "Type": "Time",
        "Condition": 10000
      },
      "parameters": []
    }
  ]
}
```

### 6.1 Presentation tags

De første tags i en øvelsesdefinition bruges til præsentation i appen, især på exercise list og exercise presentation screens.

`outlines` beskriver layoutet af elementer på execution-skærmen og kan variere afhængigt af tilgængelig hardware.

### 6.2 Elements tag

`elements` definerer hvilke elementtyper og versioner der kræves for at gennemføre en øvelse.

Eksempel:

```json
{
  "type": "Port",
  "minVersion": "1.0",
  "minNumber": 3,
  "maxNumber": 5
}
```

### 6.3 Tasks tag

`tasks` definerer de steps en øvelse gennemløber.

Eksempel:

```json
{
  "seq": 1,
  "type": "Port",
  "id": "Random",
  "setPayload": {
    "timeOpen": 2000,
    "silent": true
  }
}
```

Task-listen understøtter repetition:

```json
{
  "seq": 5,
  "type": "Repeat",
  "startSeq": 1,
  "repetitions": -1
}
```

### 6.4 Parameters tag

`parameters` definerer hvilke øvelsesparametre brugeren kan justere i appen.

Eksempel:

```json
{
  "name": "TimeOpen",
  "validValues": {
    "v1": -1,
    "v2": {
      "type": "numberType",
      "minValue": 500,
      "maxValue": 3000
    }
  }
}
```

## 7. Exercise execution

Exercise execution består af app-skærme og processer:

- Exercise introduction screen.
- Exercise parameters screen.
- Exercise elements layout screen.
- Optional document execution screen.
- Execution screen.
- Execution interpreter.
- Complete screen.
- Logging.

### 7.1 Introduction screen

Når en øvelse vælges, vises en introduktionsskærm med:

- Video, der viser hvordan øvelsen udføres.
- Tekstbeskrivelse fra `longDesc`.
- Start-knap.
- Test-knap til screen tapping.
- Parameters-knap.

### 7.2 Parameters screen

Hvis øvelsen har parametre, vises de på parameters screen. Felterne udfyldes med værdier fra brugerprofilen eller fra øvelsesdefinitionen.

### 7.3 Elements layout screen

Når brugeren starter en øvelse, vises layoutet for de nødvendige elementer. Hvert element på skærmen har et ID, der matcher ID'et på det fysiske elements 7-segment-display.

Brugeren verificerer fysisk placering og fortsætter derefter til øvelsen.

### 7.4 Execution screen og interpreter

Når øvelsen starter, sender appen en start-task til alle relevante elementer:

```json
{
  "task": "start"
}
```

Elementerne kvitterer:

```json
{
  "confirmedTask": "start"
}
```

Når alle elementer er klar, sender appen `set` tasks til de elementer, der skal aktiveres:

```json
{
  "task": "set",
  "parameter1": "Val1",
  "parameterN": "ValN"
}
```

Hvis appen ikke modtager svar, skal brugeren informeres om at kontrollere elementet med det relevante ID.

### 7.5 Task result

Når elementet har modtaget en `set` task, venter det på at brugeren løser tasken eller at tasken timer ud.

Eksempel på resultat:

```json
{
  "solved": true,
  "time": 99999,
  "direction": 99999,
  "speed": 99999
}
```

`time` angives i millisekunder siden tasken blev sat.

### 7.6 Gameover

Når end condition er opfyldt, sender appen en `over` task til de anvendte elementer:

```json
{
  "task": "over",
  "result": 999
}
```

`result` er valgfri og kan vises på elementets 7-segment-display.

### 7.7 Exercise completed

Når øvelsen er afsluttet, kan brugeren:

- Prøve øvelsen igen.
- Gå tilbage til exercise list.
- Se og dele dokumenteret video, hvis document execution blev valgt.
- Få resultatet tilføjet til high score, hvis det kvalificerer.

## 8. Document execution og logging

Document execution er valgfri. Hvis valgt, optages video af brugeren under øvelsen. Videoen får exercise metrics lagt ovenpå, så resultatet kan dokumenteres.

Logging:

- ESP32-log fra hvert element streames til appen.
- Appen videresender elementlog til backend.
- Appen streamer også egen execution log og exercise metrics til backend.

## 9. Resultathåndtering

High score lists segmenteres efter øvelse og aldersgruppe.

Der findes tre typer:

1. **Lokal for app-instans**
   - Tilgængelig for anonymous users.
   - Gemmes på backend, men er kun tilgængelig fra den aktuelle device.

2. **Lokal for user group**
   - Tilgængelig for medlemmer af gruppen.

3. **Global high score list**
   - Fælles på tværs af installationer.
   - Kræver logged-in user.
   - Kræver at `document` parameter er sat.
   - Dokumentationsvideo deles automatisk på relevante sociale medier.

Result screen viser øvelsesresultat og placering på relevante high score lists.

## 10. System web page

Systemets web page hostes på Azure og kan bruges anonymt eller med login.

Formål:

- Gennemse exercise execution metrics.
- Gennemse alle øvelser.

Anonymous users får adgang til anonymiserede shared data. Logged-in users får også adgang til egne data og gruppedata.

Logged-in users kan:

- Tilføje øvelser til preferred exercises.
- Kommentere øvelser.
- Dele resultater med grupper eller globalt.

## 11. Supportinterface

Supportinterfacet understøtter fire funktioner:

1. SQL-adgang til exercise usage metrics.
2. File access til logdata.
3. File access til exercise definition JSON.
4. Upload af exercise definition JSON, inklusive test/release-feature.

## 12. Afklaringer og opfølgningspunkter

Følgende punkter fremstår som relevante at afklare eller omsætte til konkrete issues:

- Endelig firmwarestruktur og modulgrænser.
- Standardiseret JSON schema for app-element kommunikation.
- Fejlhåndtering for WiFi, WebSocket og element-timeout.
- Definition af Azure backend-komponenter og datamodeller.
- Implementeringsstatus for OTA update.
- Implementeringsstatus for power management.
- Implementeringsstatus for eksterne I2C-enheder.
- Format og lagring af exercise metrics og logs.
- Sikkerheds- og GDPR-model for brugerdata, deling og high score.
- Release-flow for exercise definition JSON.

## 13. Relation til repositories

Denne side beskriver den samlede MVP-løsning og bør derfor behandles som tværgående dokumentation i `appsim`.

Anbefalet fordeling:

- `appsim`: samlet systemoverblik, app-flow, backend-flow, exercise definitions, WebSocket-server og tværgående dokumentation.
- `element`: firmware, hardware abstraction, sensorhåndtering, display, provisioning, WebSocket-client og element-protokol.

Når denne side eller den egentlige GitHub Wiki opdateres væsentligt, bør det vurderes om `README.md`, `copilot-instructions.md`, `recommendations.md` eller `decisions.md` også skal opdateres.
