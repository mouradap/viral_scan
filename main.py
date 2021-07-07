import argparse
from transformers import aligner, indexer, sorter, variant_caller, blaster, virus_detector

# Argument Parser prepara como método de configurar
# inputs e outputs do nosso programa.

ap = argparse.ArgumentParser()
ap.add_argument(
    "-i",
    "--input",
    type=str,
    required=True,
    help="path to the input file"
    )
ap.add_argument(
    "-I",
    "--pair",
    type=str,
    required=True,
    help="path to the input pair file"
    )
ap.add_argument(
    "-ri",
    "--reference_index",
    type=bool,
    required=False,
    help="when true, creates index from reference genome"
)
ap.add_argument(
    "-r",
    "--reference_genome",
    type=str,
    required=True,
    help="path to the reference genome",
)
ap.add_argument(
    '-p',
    '--picard',
    type=str,
    required=True,
    help='Path to the picard.jar file'
)
ap.add_argument(
    '-s',
    '--snpeff',
    type=str,
    required=False,
    help='path to the snpeff.jar file.'
)
ap.add_argument(
    '-t',
    '--target',
    type=str,
    required=False,
    help='if provided, point to the path of a file containing targets for the variant caller.'
)
ap.add_argument(
    '-T',
    '--threads',
    type=int,
    required=False,
    help='number of threads used in bwa'
)
args = vars(ap.parse_args())

ref_genome = args['reference_genome']
r1 = args['input']
r2 = args['pair']
picard_jar = args['picard']
snpeff_jar = args['snpeff']
if 'target' in args.keys():
    targets = args['target']
threads = args['threads']

print("### Starting NGS pipeline for the bioinfotest! ###\n")

if 'reference_index' in args.keys():
    print("### Attempting to index the reference genome ###\n")
    indexer.reference_indexing(ref_genome)

print("### Analyzing quality of reads with FastQC ###\n")
qual = quality_analyzer.fastqc_analyzer(r1, r2, threads)
print(qual)

print("### Aligning reads to genome of reference ###\n")
aligner.sequence_aligner(ref_genome, r1, r2, threads)

print("### Sorting and filtering the reads with samtools and picard ###\n")
sorter.bam_sorting(r1, r2, picard_jar)

print("### Calling variants with FreeBayes ###\n")
variant_caller.variant_calling(ref_genome, r1, r2, targets)

print("### Attempting to map variants by function with snpEff ###\n")
functional_mapper.functional_mapping(r1, r2, snpeff_jar)

print("Pipeline complete!")

