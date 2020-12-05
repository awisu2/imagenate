# imagenatepy

## install

```bash
pip install git+https://github.com/awisu2/imagenatepy.git
```

## usage

### create

```bash
imagenate create --height 100 --width 100 --color '#F00' -o red_100x100.png
imagenate create --height 100 --width 100 --color '#0F0' -o green_100x100.png
imagenate create --height 100 --width 100 --color '#00F' -o blue_100x100.png
imagenate create --height 100 --width 100 --color '#FF0' -o yellow_100x100.png
```

### concat

```bash
imagenate concat -i red_100x100.png green_100x100.png blue_100x100.png yellow_100x100.png -o concat.png -r 2 -c 2
```
