## https://huggingface.co/nvidia/mit-b0/discussions/3

contains_question: yes

question_part: I am trying to containerize and fine-tune SegFormer model so I want to load the pre-trained from local folder only but this code `SegformerForSemanticSegmentation.from_pretrained(
        pretrained_model_name_or_path=PATH,
        local_files_only=True,
        num_labels=num_classes,
    )` give me error `huggingface_hub.utils._validators.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/home/ellen/pretrained/mit-b0'. Use 'repo_type' argument if needed.`