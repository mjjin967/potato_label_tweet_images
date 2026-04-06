# Potato Labeling for Tweet Images
Label 1500 images using Potato
https://potato-annotation.readthedocs.io/en/latest/

## Setup
```bash
pip install potato-annotation flask
```

## How to run
To run the visualizer, run 
```bash
python visualizer/server.py --csv your_data.csv --images images_dir
```

For example, to see the annotations Jean has done, run
```bash
python visualizer/server.py --csv potato/annotations_jean.csv --images potato/data/media_jean
```

To run the labeler,
```bash
potato start <your_config_file> -p 8000 
```
from the root directory. Navigate to `localhost:8000` in your browser to start labeling.

Once you register with `<your_user_name>` and start labeling, a log of your labeling activity will be created under `annotation_output/image-labeling/<your_username>/user_state.json`.

Refer to section "Directory Structure" below for more.

**If you come up with new labels, you must add them in the config file.** Then simply restart the server. Your labeling activity will be automatically saved. Log in via the "Register" tab if "login" doesn't work.

To visualize your annotations, you must **save your annotations to a csv file**.
Put in your name in `save_annotations_to_csv.py` and save your annotations into a csv file.

## Directory Structure
```bash
potato/
├── annotation_output
│   └── image-labeling
│       └── <your_username>
│           └── user_state.json
├── config_<your_name>.yaml
├── save_annotations_to_csv.py
├── data/
│   ├── images_<your_name>.jsonl
│   └── media_<your_name>/
│       └── images ...
└── layouts/
│   └── task_layout.html
└── templates/
    └── image_layout.html
```