## https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593/discussions/7

contains_question: yes

question_part: I am trying to use AST for the first time and i've followed all the documentations and tutorial but i encountered an error which i still can't find out what the error is the error is as follows /usr/local/lib/python3.10/dist-packages/transformers/models/audio_spectrogram_transformer/modeling_audio_spectrogram_transformer.py in forward(self, input_values) 85 distillation_tokens = self.distillation_token.expand(batch_size, -1, -1) 86 embeddings = torch.cat((cls_tokens, distillation_tokens, embeddings), dim=1) 87 embeddings = embeddings + self.position_embeddings 88 embeddings = self.dropout(embeddings) 89 RuntimeError: The size of tensor a (110) must match the size of tensor b (1214) at non-singleton dimension 1