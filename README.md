[▶ Play on Replit (Low performance)](https://replit.com/@rumbleFTW/sokobot#.replit)

# SokoBot

An indie Sokoban-esque game completely written in python.

- [Concepts](https://arxiv.org/abs/1807.00049)
- [Sprite ideas](https://gm48.net/game/994/count-downula)
- [Levels database](https://sokoban.info)

## Demo:

https://user-images.githubusercontent.com/85807431/194949704-3d8c9ced-650f-4fdc-8991-a5b74b4af991.mp4

## Run in local machine

1. Clone the repo
``` 
git clone https://github.com/rumbleFTW/sokobot.git
```
2. Navigate to folder
```
cd sokobot
```
3. Install Pygame
```
pip install pygame
```
4. Run main.py
```
python main.py
```

## Basics

1. The levels are stored in the ~./levels.py file in the form of a 2-D array.
2. The assets for the games were created with Piskel annd are stored in the ~./assets folder.
3. The solving algorithms are present in a .py file in the root directory.
4. The functions necessary for the main game loop are present in ~./funcs.py.
