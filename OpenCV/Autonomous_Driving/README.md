Autonomous Driving Demo (Obstacle Detection, Lane Segmentation, Navigation)

Rilevamento e classificazione ostacoli (auto, pedoni, ciclisti) via modello YOLO.
Segmentazione / rilevamento corsia (lane detection) con preprocessing, Canny e Hough.
Mappa di occupazione 2D (occupancy grid) e pianificazione di percorso semplice (A*).
Cosa fa
Carica un'immagine di test.
Esegue object detection per rilevare veicoli, pedoni e ciclisti; disegna bounding box e label.
Rileva le linee di corsia nella parte inferiore dell'immagine; visualizza le linee medie della corsia e calcola uno scostamento approssimativo dalla centro-corsia*
Proietta in modo molto approssimativo i bounding box rilevati su una occupancy grid 2D.
Esegue A* per pianificare un percorso semplice da una posizione di partenza (centro fondo della mappa) verso un obiettivo avanti nella mappa.
Mostra due finestre: "Detections + Lanes" e "Occupancy Grid + Path".
File principali
autonomous_demo.py — script tutto-in-uno che implementa detection, lane detection, occupany grid e planner.

Images/your_image.jpg — immagine di esempio (sostituire con la tua).
yolov8n.pt (o altro modello YOLO) 
haarcascade_frontalface_default.xml — (non richiesto per questa demo, solo negli esempi precedenti).
Prerequisiti
Python 3.8+
pip install:
opencv-python
numpy
torch
torchvision
ultralytics
networkx

Scarica un modello YOLO (es. yolov8n.pt) e assicurati che YOLO_MODEL punti al file corretto.
Esegui: python autonomous_demo.py
Verranno aperte le finestre con i risultati; premi un tasto per chiudere.
Parametri modificabili (nel file)
IMAGE_PATH — percorso immagine di input.
YOLO_MODEL — percorso del modello YOLO.
DETECTION_CLASSES — mappatura etichette raw → categorie (pedestrian, vehicle, cyclist).
OCC_GRID_SIZE_M, GRID_RESOLUTION — dimensione e risoluzione della occupancy grid.
Soglia confidence per detection (detect(..., conf_thresh=...)).
Limitazioni e avvertenze (importanti)
Progetto didattico: non è un sistema pronto per produzione né adatto al controllo reale di veicoli.
Stima della distanza e proiezione bounding-box → occupancy grid sono estremamente approssimative; per mappe affidabili servono calibrazione camera, stereo/LiDAR o reti di depth estimation (es. MiDaS) o sensori aggiuntivi.
Lane detection basata su Canny + Hough: sensibile a illuminazione, ombre, condizioni meteo e segnaletica deteriorata. Reti di segmentation sono più robuste.
Per funzionamento in tempo reale: usare feed video/camera, modello ottimizzato e GPU.
Per navigazione reale: usare SLAM (ORB-SLAM3, RTAB-Map) per costruire mappe metriche, e planner robusti (D* Lite, RRT*, TEB) con controllo e valutazione di sicurezza.
Test e validazione estesi richiesti prima di qualsiasi uso in sicurezza critica.
Possibili estensioni (suggerite)
Sostituire YOLOv8 con yolov5 o Detectron2.
Aggiungere stima della profondità monoculare (MiDaS) per migliorare la proiezione in mappa.
Trasformare pipeline per input video/camera e ottimizzare inference GPU.
Integrare SLAM per mappa metriche multi-frame.
Sostituire lane detection classica con rete di semantic segmentation (ENet, SCNN).
Usare planner avanzati e considerare dinamiche del veicolo per tracking e controllo (model predictive control, pure pursuit).
Risorse utili
YOLOv8 (ultralytics) per object detection.
MiDaS per depth estimation monoculare.
ORB-SLAM3 / RTAB-Map per SLAM.
ROS Navigation Stack per integrazione robotica/autonoma.
