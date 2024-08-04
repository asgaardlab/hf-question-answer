## https://huggingface.co/InstaDeepAI/nucleotide-transformer-2.5b-1000g/discussions/3

contains_question: yes

question_part: 
1. **Data Interpretation:** The paper mentions the use of 3202 high-coverage human genomes, totaling 20.5 trillion nucleotides. From my understanding, considering that each human genome is about 3.2 billion nucleotides, and accounting for diploid genomes, the calculation, 3.2B * 2 * 3202 =  20,492.8B = 20.5T, seems to match up with your figures. Can anyone confirm if this interpretation is correct or if there's something I'm missing?

2. **Handling Large Data Volumes:** In handling data from the 1000 Genomes Project, I've encountered the challenge of managing large volumes of data. With each genome being about 3GB and considering diploidy, the data for 3202 samples would be roughly 18.76TB (= 3GB * 2 * 3202) . How did the team manage such a vast amount of training data? Did you utilize the entire dataset directly for training, or were there specific preprocessing or reduction techniques applied?

3. **FASTA File Generation Issues:** I've been facing difficulties in generating FASTA files from VCF files, with processes taking an excessive amount of time even on high-spec servers. I've tried using tools like `bcftools consensus` and `gatk FastaAlternateReferenceMaker` but to no avail. I'm curious about the tools or methods the team used for this conversion process and would appreciate any suggestions or recommendations.