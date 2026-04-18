import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_highlight_reel(clip_paths, output_name="highlight_reel.mp4"):
    # 🚀 TEMP DEMO VERSION (no MoviePy)

    print("Creating highlight reel from:", clip_paths)

    # fake output path
    output_path = os.path.join(OUTPUT_DIR, output_name)

    # create dummy file so UI thinks it worked
    with open(output_path, "w") as f:
        f.write("Demo reel placeholder")

    return output_path