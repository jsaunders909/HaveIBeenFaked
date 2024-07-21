# HaveIBeenFaked
Project repo for the Microsoft InternHacks 2024 - Have I been faked


# Installation
To install our work, first clone the repo:

```git clone https://github.com/jsaunders909/HaveIBeenFaked.git ```

Then install our package (ideally you use a virtual environment like conda).

```
cd HaveIBeenFaked
pip install -e .
```

# Running the Live Demo

You can run the live demo straight from the repo. First you can add your facial profile with the script:

```
python tests/add_to_db.py
```

You might have to click on the window that gets opened. Press enter to start, then 'f' to take a frontal image, 'l' and 'r' to take left and right images, take these at about a 45 degree angle. Press 's' once you have all your images.

You can then run the live demo with:

```
python tests/test.py
```


