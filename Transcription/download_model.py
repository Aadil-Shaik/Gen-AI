from pyannote.audio import Pipeline
import torch
import os

HF_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Download the diarization model
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=HF_AUTH_TOKEN
)

pipeline.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

# Save the entire pipeline directly
save_dir = "diarization_model"
os.makedirs(save_dir, exist_ok=True)

pipeline_save_path = os.path.join(save_dir, "pipeline.pkl")
torch.save(pipeline, pipeline_save_path)

print(f"Pipeline saved at {pipeline_save_path}")
