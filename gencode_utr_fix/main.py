import click
from tqdm import tqdm
import pyranges as pr


class UtrUpdater:

    def __init__(self, gr: pr.PyRanges):
        self.starts, self.ends = self.cds_start_end(gr)

    @staticmethod
    def cds_start_end(gr: pr.PyRanges):
        print('Calculating CDS locations...')

        starts = dict()
        ends = dict()

        for i, df in tqdm(gr.df.groupby('transcript_id')):

            df = df[df['Feature'] == 'CDS']

            if df.shape[0] == 0:
                continue

            starts[i] = df['Start'].min()
            ends[i] = df['End'].max()

        return starts, ends

    def __call__(self, row):
        if row['Feature'] == 'UTR':
            cds_start = self.starts[row['transcript_id']]
            cds_end = self.ends[row['transcript_id']]

            if row['Start'] < cds_start:
                row['Feature'] = 'five_prime_utr'
            elif cds_end < row['End']:
                row['Feature'] = 'three_prime_utr'
            else:
                raise ValueError('UTR type cannot determined')
        return row


def gencode_utr_fix(gr):
    """
    Update gtf pyranges objects UTRs.

    Args:
      gr: (pyranges.PyRanges) pyrange for GTF.
    """
    update_utr_row = UtrUpdater(gr)
    print('Calculating UTR side...')
    return gr.apply(lambda df: df.apply(update_utr_row, axis=1))


@click.command()
@click.option('--input_gtf', help='Number of greetings.')
@click.option('--output_gtf', help='The person to greet.')
def cli(input_gtf, output_gtf):
    print('Reading GTF...')
    gr = pr.read_gtf(input_gtf)
    gr_utr = gencode_utr_fix(gr)
    gr_utr.to_gtf(output_gtf)


if __name__ == '__main__':
    cli()
