# Potato Labeling for Tweet Images
Label 1500 images using Potato
https://potato-annotation.readthedocs.io/en/latest/

## Setup
```bash
pip install potato-annotation
```

## How to run
 
```bash
potato start config.yaml -p 8000 
```
from the root directory. Go to `localhost:8000`

Once you register and start labeling, a log of your labeling activity will be created under `annotation_output/image-labeling/<your_username>/user_state.json`.
Your labeling activity will be automatically saved once you stop the local server.

## Directory Structure

```bash
potato_label_tweet_images/
├── annotation_output
│   └── image-labeling
│       └── <your_username>
│           └── user_state.json
├── config.yaml
├── data/
│   ├── images.jsonl
│   └── media/
│       └── images
└── layouts/
    └── task_layout.html
└── templates/
    └── image_layout.html
```