import subprocess

def reference_indexing(reference_genome):
    bwa_index_command = 'bwa index {ref_genome}'.format(ref_genome=reference_genome)
    samtools_index_command = 'samtools faidx {ref_genome}'.format(ref_genome=reference_genome)
    subprocess.run(bwa_index_command, shell=True)
    subprocess.run(samtools_index_command, shell=True)

