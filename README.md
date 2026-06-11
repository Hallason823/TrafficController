# TrafficController

Smart traffic light controller using a trained EfficientNet-B0 model to dynamically adjust green times based on detected car counts.

## Setup

```bash
cp ../TransitCarCounting/EFFICIENTNET_best.pth model/
pip install -r requirements.txt
```

Upload `arduino/semaforo.ino` via Arduino IDE.

## Arduino Pins

| Lane   | Green | Yellow | Red |
|--------|-------|--------|-----|
| Right  | 4     | 3      | 2   |
| Bottom | 7     | 6      | 5   |

## Run

```bash
python src/main.py [--port COM3] [--camera 1] [--model model/EFFICIENTNET_best.pth] [--n-frames 5]
```

## Timing Logic

Base green: 30s — Yellow: 10s fixed (model runs during this window)

`diff = right_cars − bottom_cars`  
`next_right = max(10, 30 + diff × 10)` | `next_bottom = max(10, 30 − diff × 10)`

## Serial Protocol

| Direction    | Message     | Meaning                  |
|--------------|-------------|--------------------------|
| PC → Arduino | `R,30\n`    | Right green for 30s      |
| PC → Arduino | `B,20\n`    | Bottom green for 20s     |
| Arduino → PC | `DONE\n`    | Phase complete           |
| Arduino → PC | `READY\n`   | Arduino initialized      |
