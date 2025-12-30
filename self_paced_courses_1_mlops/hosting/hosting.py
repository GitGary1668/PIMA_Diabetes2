from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_PIMA2"))
api.upload_folder(
    folder_path="self_paced_courses_1_mlops/deployment",
    repo_id="GaryWilliams1668/HFSpaceName-PIMA-Diabetes2",                      # enter the Hugging Face username here
    repo_type="space",
    path_in_repo="",                          # optional: subfolder path inside the repo
)
