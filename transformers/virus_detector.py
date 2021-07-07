import subprocess

def detect_viruses(virus_ref, r1, r2, threads):
    unmapped_extraction_command = 'samtools view -f 8  {r1}_{r2}_BWA.BAM > {r1}_{r2}_BWA_Unmapped.bam'.format(
        r1=r1,
        r2=r2)
    bwa_align_command = 'bwa mem -t {threads} {ref_genome} {r1}_{r2}_BWA_Unmapped.bam | samtools sort -o {r1}_{r2}_BWA_viruses_sorted.bam'.format(
        ref_genome=virus_ref,
        r1 = r1,
        r2 = r2,
        threads=threads)
    samtools_index = 'samtools index {r1}_{r2}_BWA_viruses_sorted.bam'.format(
        r1=r1,
        r2=r2
    )
    retrieve_viruses_command = 'samtools idxstats {r1}_{r2}_BWA_viruses_sorted.bam > viruses.txt'.format(
        r1=r1,
        r2=r2
    )

    print("Extracting unmapped reads from BAM...")
    subprocess.run(unmapped_extraction_command, shell=True)
    print("Done!\n")

    print("Running alignment with bwa mem...")
    subprocess.run(bwa_align_command, shell=True)
    print("Done!\n")

    print("Indexing bam file...")
    subprocess.run(samtools_index, shell=True)
    print("Done!\n")

    print("Retrieving viruses reads...")
    subprocess.run(retrieve_viruses_command, shell=True)
    print("Done!\n")