import argparse
import distinct_n
import logging

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compute average distinct-N on a hypothesis file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('hypothesis', help="predicted text file, one example per line")
    parser.add_argument('-n', type=int, default=2, help="n to use as in distinct-N")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info('loading hypothesis file...')
    with open(args.hypothesis) as f:
        hypothesis = [sentence.split() for sentence in f.readlines()]

    for n in range(1, args.n + 1):
        r = distinct_n.distinct_n_corpus_level(sentences=hypothesis, n=n)
        print("Distinct-%d: %f" % (n, r))
