import subprocess

def sequence_aligner(reference_genome, r1, r2, threads):
    bwa_align_command = 'bwa mem -t {threads} {ref_genome} {r1} {r2} | samtools sort -o {r1}_{r2}_BWA_sorted.bam'.format(
        ref_genome=reference_genome,
        r1 = r1,
        r2 = r2,
        threads=threads)
    samtools_index = 'samtools index {r1}_{r2}_BWA_sorted.bam'.format(
        r1=r1,
        r2=r2
    )

    print("Running alignment with bwa mem...")
    subprocess.run(bwa_align_command, shell=True)
    print("Done!\n")

    print("Indexing bam file...")
    subprocess.run(samtools_index, shell=True)
    print("Done!\n")

