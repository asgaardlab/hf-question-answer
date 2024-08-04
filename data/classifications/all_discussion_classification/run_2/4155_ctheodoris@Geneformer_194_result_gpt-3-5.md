## https://huggingface.co/ctheodoris/Geneformer/discussions/194

contains_question: yes

question_part: I was wondering if "Shift_to_goal_end" represents the cosine similarity shift in the paper. And I'm not very clear on how I should interpret the main columns.

I thought the first two columns "" and "Gene" are just gene indices in my dataset and Geneformer model, respectively, and have nothing to do with gene ranking values. "N_Detections" should be the number of cells in which the gene was detected, and "Sig" denotes whether the deletion of this gene shifted the cell state from start_state to goal_state. Please correct me if I'm wrong.

I was wondering if you could briefly explain "Shift_to_goal_end", "Goal_end_vs_random_pval", and "Goal_end_FDR" for the interpretation of the results. How should I use "Shift_to_goal_end" for plotting the cosine similarity as in the paper, or gene/cell embedding plots? Thank you very much for your time and help!