# Autonomous Driving Demo

*Un esperimento di guida autonoma con rilevamento ostacoli, segmentazione corsie e pianificazione percorso.*

---

## 🚗 Di cosa si tratta?

Questo progetto è una **demo sperimentale** per testare alcune tecniche di base per la guida autonoma. Non è un sistema pronto per l'uso reale, ma un modo per imparare e sperimentare con:

- **Rilevamento ostacoli** (auto, pedoni, ciclisti) usando **YOLOv8**.
- **Segmentazione delle corsie** con preprocessing, filtri di Canny e trasformata di Hough.
- **Mappatura 2D** (occupancy grid) e **pianificazione di un percorso semplice** con l'algoritmo **A**.

---

## 🎯 Cosa fa esattamente?

1. **Carica un'immagine** di test (es. una foto di una strada).
2. **Rileva gli ostacoli** (veicoli, pedoni, ciclisti) e disegna le *bounding box* con le etichette.
3. **Trova le linee della corsia** nella parte bassa dell'immagine, visualizza le linee medie e calcola uno scostamento approssimativo dal centro della corsia.
4. **Proietta gli ostacoli** su una griglia 2D (occupancy grid) in modo molto approssimativo.
5. **Pianifica un percorso** da un punto di partenza (centro in basso della mappa) verso un obiettivo più avanti, usando **A**.
6. **Mostra due finestre**:
  - *"Detections + Lanes"*: immagine originale con bounding box e corsie.
  - *"Occupancy Grid + Path"*: griglia 2D con ostacoli e percorso pianificato.

---

## 📁 File principali

- `**autonomous_demo.py**`: Lo script principale che fa tutto: detection, lane detection, occupancy grid e pianificazione.
- `**Images/your_image.jpg**`: Un'immagine di esempio per testare il sistema.
- `**yolov8n.pt**` (o un altro modello YOLO): il modello pre-addestrato per il rilevamento degli ostacoli.

> *Nota*: Il file `haarcascade_frontalface_default.xml` non serve per questa demo, è un residuo di test precedenti.

---

## ⚙️ Prerequisiti

- **Python 3.8+**
- Librerie necessarie (installabili con `pip`):
  ```bash
  pip install opencv-python numpy torch torchvision ultralytics networkx
  ```
- **Modello YOLO**: Scarica un modello (es. `yolov8n.pt`) e assicurati che la variabile `YOLO_MODEL` nel codice punti al file corretto.

---

## 🚀 Come avviarlo?

1. Assicurati di avere tutte le dipendenze installate.
2. Esegui:
  ```bash
   python autonomous_demo.py
  ```
3. Verranno aperte due finestre con i risultati. Premi un tasto per chiuderle.

---

## ⚙️ Parametri da personalizzare

Puoi modificare direttamente nello script:

- `**IMAGE_PATH**`: Percorso dell'immagine di input.
- `**YOLO_MODEL**`: Percorso del modello YOLO.
- `**DETECTION_CLASSES**`: Mappatura delle etichette grezze in categorie (es. `pedestrian`, `vehicle`, `cyclist`).
- `**OCC_GRID_SIZE_M`, `GRID_RESOLUTION**`: Dimensione e risoluzione della griglia 2D.
- **Soglia di confidenza** per la detection (es. `detect(..., conf_thresh=0.5)`).

---

## ⚠️ Limitazioni e avvertenze

⚠️ **Attenzione**: Questo è un **progetto didattico**, non un sistema pronto per la produzione o per il controllo reale di veicoli.

- **Distanze e proiezione**: La stima della distanza e la proiezione delle bounding box sulla griglia sono **molto approssimative**. Per mappe affidabili servono:
  - Calibrazione della camera.
  - Sensori aggiuntivi (stereo, LiDAR) o reti per la stima della profondità (es. **MiDaS**).
- **Lane detection**: Il metodo basato su Canny + Hough è **sensibile** a:
  - Illuminazione, ombre, condizioni meteo.
  - Segnaletica deteriorata.  
  Le reti di **segmentazione semantica** (es. ENet, SCNN) sono molto più robuste.
- **Tempo reale**: Per un funzionamento in tempo reale, servono:
  - Feed video/camera.
  - Modello ottimizzato e GPU.
- **Navigazione reale**: Per un sistema reale, servono:
  - **SLAM** (es. ORB-SLAM3, RTAB-Map) per costruire mappe metriche.
  - **Planner robusti** (es. D Lite, RRT, TEB) con controllo e valutazione della sicurezza.
- **Test e validazione**: Sono **assolutamente necessari** prima di qualsiasi uso in contesti critici per la sicurezza.

---

## 💡 Idee per estendere il progetto

Se vuoi portarlo al livello successivo, ecco alcune idee:

- **Cambiare il modello di detection**: Prova con **YOLOv5** o **Detectron2**.
- **Aggiungere la stima della profondità**: Usa **MiDaS** per migliorare la proiezione sulla griglia.
- **Lavorare con video**: Trasforma la pipeline per accettare input da video/camera e ottimizza l'inference con la GPU.
- **Integrare SLAM**: Usa **ORB-SLAM3** o **RTAB-Map** per costruire mappe metriche multi-frame.
- **Segmentazione semantica per le corsie**: Sostituisci Canny + Hough con reti come **ENet** o **SCNN**.
- **Planner avanzati**: Prova con **D Lite**, **RRT**, o **TEB**, e considera le dinamiche del veicolo per il tracking e il controllo (es. **Model Predictive Control**, **Pure Pursuit**).

---

## 📚 Risorse utili

- [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics) per l'object detection.
- [MiDaS](https://github.com/isl-org/MiDaS) per la stima della profondità monoculare.
- [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) / [RTAB-Map](https://github.com/introlab/rtabmap) per lo SLAM.
- [ROS Navigation Stack](http://wiki.ros.org/navigation) per l'integrazione robotica/autonoma.  
</canvaentity
