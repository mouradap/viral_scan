from subprocess import Popen, PIPE, run

def blast_unmapped_reads(input_file, virus_db, output_file):
    unmapped_extraction_command = 'samtools view -f 8  {input_file}'.format(input_file=input_file)
    map_read_command = """awk '{printf(">%s/%s\n%s\n",$1,(and(int($2),0x40)?1:2),$10);}'"""
    blast_command = 'blastn -db {virus_db} -out {output_file}'.format(virus_db=virus_db, output_file=output_file)

    unmapped_extracts = Popen(unmapped_extraction_command, stdout=PIPE)
    mapped_reads = Popen(map_read_command, stdin = unmapped_extracts.stdout)
    run(blast_command, stdin = mapped_reads.stdout)
