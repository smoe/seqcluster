# Re-aligner small RNA sequence from SAM/BAM file (miRBase annotation)
import os.path as op

import pysam
from bcbio import bam

import seqcluster.libs.logger as mylog

logger = mylog.getLogger(__name__)

def _read_precursor(precursor, sps):
    """
    read precurso file for that species
    """
    haripin = {}
    with open(precursor) as in_handle:
        for line in in_handle:
            if line.startswith(">"):
                name = line.strip().replace(">", " ").split()[0]
            else:
                haripin[name] = line.strip()
    return hairpin

def _download_mirbase(precursor, reference, version="22"):
    """
    Download files from mirbase
    """
    if not precursors or not reference:
        print "Working with version %s" % version

def _annotate(read, mirbase_ref):
    """
    Using SAM/BAM coordinates, mismatches and realign to annotate isomiRs
    """

def _realign(hit):
    """
    The actual fn that will realign the sequence
    """

def _realign_hits(read):
    """
    realign read to the list precursors
    """
    for genome in read.precursors:
        new_hit = _realign(read.sequence, genome)

def _sort_by_name(bam_fn):
    """
    sort bam file by name sequence
    """

def _read_bam(bam_fn):
    """
    read bam file and perform realignment of hits
    """

def miraligner(args):
    """
    Realign BAM hits to miRBAse to get better accuracy and annotation
    """
    config = {"algorithm": {"num_cores":1}}
    print args
    for bam_fn in args.files:
        logger.info("Reading %s" % bam_fn)
        bam_fn = bam.sam_to_bam(bam_fn, config)
        bam_sort_by_n = op.splitext(bam_fn)[0] + "_sort"
        pysam.sort("-n", bam_fn, bam_sort_by_n)