import json
import pandas as pd

# TODO: put in your user_name under annotation_output/image-labeling
user_name = ""
if user_name == "":
    raise ValueError("Please set your user_name in save_annotations_to_csv.py")

with open(f"annotation_output/image-labeling/{user_name}/user_state.json") as f:
    state = json.load(f)

rows = []
for image_id, labels in state["instance_id_to_label_to_value"].items():
    row = {"id": image_id}
    for label_entry, value in labels:
        schema = label_entry["schema"]
        # for multiselect, accumulate into a list
        if schema == "categories":
            row.setdefault("categories", []).append(value)
        else:
            row[schema] = value
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv(f"annotations_{user_name}.csv", index=False)