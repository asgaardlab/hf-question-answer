### Documents:
- Extending Geneformer to Study Cell-Cell Communication 

I'm currently working with Geneformer for in silico perturbations to identify disease-driving genes. This approach allows us to observe the impact of gene deletions on a cell state to determine if a specific gene could be a potential driver for disease. Now, I'm interested in extending this analysis to study cell-cell communication.

My idea is to train the model on two different cell types, then simulate gene knockouts in one cell type and analyze the effects on the other cell type.

Would this approach be feasible for studying cell-cell communication using Geneformer?
Would this require retraining the model from scratch, or could we leverage fine-tuning for this task?
If fine-tuning can be applied, could you suggest a possible methodology to carry it out for this specific scenario?"
- Interpretation and plotting of the results of InSilicoPerturberStats.get_stats

Hi, I'm working on gene perturbation using the pre-trained Geneformer model and I was wondering if you could help me with the interpretation and plotting of the results of InSilicoPerturberStats.get_stats. 

I finished running InSilicoPerturber(emb_mode='cell').perturb_data on 1,000 disease cells and 1,000 healthy cells with 19,117 genes and conducted InSilicoPerturberStats.get_stats. 

Then I performed InSilicoPerturber(emb_mode='cell_and_gene').perturb_data separately on the same data. 

The parameters I used are as below:

isp = InSilicoPerturber(perturb_type='delete', 
                        perturb_rank_shift=None, 
                        genes_to_perturb='all', 
                        combos=0, 
                        anchor_gene=None, 
                        model_type='Pretrained', 
                        num_classes=0, 
                        emb_mode='cell_and_gene', 
                        cell_emb_style='mean_pool', 
                        cell_states_to_model={'state_key': 'group', 'start_state': 'opc_gaba', 'goal_state': 'other', 'alt_states': []}, 
                        max_ncells=2000, 
                        emb_layer=-1, 
                        forward_batch_size=32, 
                        nproc=16
                        )

isp.perturb_data(model_directory='Geneformer/', 
                 input_data_file='tokenized_.dataset', 
                 output_directory='./', 
                 output_prefix='perturbed'
                 )

ispstats = InSilicoPerturberStats(mode='goal_state_shift', 
                                  combos=0, 
                                  anchor_gene=None, 
                                  cell_states_to_model={'state_key': 'group', 'start_state': 'opc_gaba', 'goal_state': 'other', 'alt_states': []}
                                  )

ispstats.get_stats(input_data_directory='./',
                   null_dist_data_directory=None,
                   output_directory='./',
                   output_prefix='stats_emb_mode_gene'
                   )

I found the two output stats.csv files have identical values regardless of emb_mode. They have 14,497 genes on rows and 9 columns: "", "Gene", "Gene_name", "Ensembl_ID", "Shift_to_goal_end", "Goal_end_vs_random_pval", "Goal_end_FDR", "N_Detections",  and "Sig". 

I was wondering if "Shift_to_goal_end" represents the cosine similarity shift in the paper. And I'm not very clear on how I should interpret the main columns. 

I thought the first two columns "" and "Gene" are just gene indices in my dataset and Geneformer model, respectively, and have nothing to do with gene ranking values. "N_Detections" should be the number of cells in which the gene was detected, and "Sig" denotes whether the deletion of this gene shifted the cell state from start_state to goal_state. Please correct me if I'm wrong.

I was wondering if you could briefly explain "Shift_to_goal_end", "Goal_end_vs_random_pval", and "Goal_end_FDR" for the interpretation of the results. How should I use "Shift_to_goal_end" for plotting the cosine similarity as in the paper, or gene/cell embedding plots? Thank you very much for your time and help!

Sincerely,
Su Wang
- Single gene perturbation error

Hi, I'm running InSilicoPerturber for a single gene:

for gene in tqdm(genes_to_perturb):
    output_directory = f'{work_directory}{gene}/'
    os.mkdir(output_directory)

    gene_id = df.at[gene, 'Ensembl_ID']

    shutil.copytree(f'{root_directory}tokenized_.dataset', f'{output_directory}tokenized_copy.dataset')

    isp = InSilicoPerturber(perturb_type='delete', 
                            perturb_rank_shift=None, 
                            genes_to_perturb=[gene_id], 
                            combos=0, 
                            anchor_gene=None, 
                            model_type='Pretrained', 
                            num_classes=0, 
                            emb_mode='cell_and_gene', 
                            cell_emb_style='mean_pool', 
                            cell_states_to_model=None, 
                            max_ncells=2000, 
                            emb_layer=-1, 
                            forward_batch_size=32, 
                            nproc=16
                            )

    isp.perturb_data(model_directory='Geneformer/', 
                     input_data_file=f'{output_directory}tokenized_copy.dataset', 
                     output_directory=output_directory, 
                     output_prefix='perturbed'
                     )

    ispstats = InSilicoPerturberStats(mode='mixture_model', 
                                      combos=0, 
                                      anchor_gene=None, 
                                      cell_states_to_model=None
                                      )

    ispstats.get_stats(input_data_directory=output_directory,
                       null_dist_data_directory=None,
                       output_directory=output_directory,
                       output_prefix='stats'
                       )

I tried both python3.8.10 and python3.10.12. For any gene, I got similar errors:

Traceback (most recent call last):
  File "/raid/swang12/Transformer31012/perturb_one.py", line 80, in <module>
    isp.perturb_data(model_directory='Geneformer/', 
  File "/home/swang12/anaconda3/envs/myenv/lib/python3.10/site-packages/geneformer/in_silico_perturber.py", line 981, in perturb_data
    self.in_silico_perturb(model,
  File "/home/swang12/anaconda3/envs/myenv/lib/python3.10/site-packages/geneformer/in_silico_perturber.py", line 1059, in in_silico_perturb
    cos_sims_data = quant_cos_sims(model, 
  File "/home/swang12/anaconda3/envs/myenv/lib/python3.10/site-packages/geneformer/in_silico_perturber.py", line 445, in quant_cos_sims
    cos_sims += [cos(minibatch_emb, minibatch_comparison).to("cpu")]
  File "/home/swang12/anaconda3/envs/myenv/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/swang12/anaconda3/envs/myenv/lib/python3.10/site-packages/torch/nn/modules/distance.py", line 87, in forward
    return F.cosine_similarity(x1, x2, self.dim, self.eps)
RuntimeError: The size of tensor a (2047) must match the size of tensor b (2046) at non-singleton dimension 1

Could you help me with this? Thank you very much!

Sincerely,
Su
### Keywords: gene, cell, geneformer, perturbation, data, cells, dataset, insilicoperturber, silico, output_directory