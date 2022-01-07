import pyranges as pr
from gencode_utr_fix import gencode_utr_fix


def test_gencode_utr_fix():
    gr = pr.data.gencode_gtf()
    gr_utr = gencode_utr_fix(gr)

    assert gr.df.shape == gr_utr.df.shape

    for i, df in gr_utr.df.groupby('transcript_id'):
        strand = df[df['Feature'] == 'transcript'].iloc[0]['Strand']

        for utr5 in df[df['Feature'] == 'five_prime_utr']['End']:
            for utr3 in df[df['Feature'] == 'three_prime_utr']['Start']:

                if strand == '+':
                    assert utr3 > utr5
                else:
                    assert utr3 < utr5
