# imagenatepy

simple image manager for my study.

- cmmandable
- ibraryable
- sample of setup.py and setup.cfg for create python package

## install

```bash
pip install git+https://github.com/awisu2/imagenatepy.git
```

## usage

[samples](docs/samples.md): other samples document.

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

# with resize
imagenate concat -i red_100x100.png green_100x100.png blue_100x100.png yellow_100x100.png -o concat_resize_inner.png -r 2 -c 2  --resize_size hd
imagenate concat -i red_100x100.png green_100x100.png blue_100x100.png yellow_100x100.png -o concat_resize_outer.png -r 2 -c 2  --resize_size hd --resize_kind outer
imagenate concat -i red_100x100.png green_100x100.png blue_100x100.png yellow_100x100.png -o concat_resize_force.png -r 2 -c 2  --resize_size hd --resize_kind force
```
