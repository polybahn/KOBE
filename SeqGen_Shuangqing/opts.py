from argparse import ArgumentParser


def model_opts():
    """
    configuration for training and evaluation
    :param parser: parser
    :return: parsed config
    """
    parser = ArgumentParser(description="train.py")
    parser.add_argument('--config', default='default.yaml', type=str,
                        help="config file")
    parser.add_argument('--gpus', default=[], nargs='+', type=int,
                        help="Use CUDA on the listed devices.")
    parser.add_argument('--restore', default='', type=str,
                        help="restore checkpoint")
    parser.add_argument('--mode', default='train', type=str,
                        help="Mode selection")
    parser.add_argument('--expname', default='', type=str,
                        help="expeirment name")
    parser.add_argument('--batch_size', default=64, type=int)
    parser.add_argument('--beam_size', default=1, type=int)
    parser.add_argument('--save_individual', action='store_true', default=False,
                        help="save individual checkpoint")
    parser.add_argument('--pretrain', default='', type=str,
                        help="load pretrain encoder")

    # for prediction
    parser.add_argument('--prediciton_file', type=str,
                        help="Path to store predicted candidates during evaluation or prediction")
    parser.add_argument('--test_src', default='', type=str,
                        help="test source file")
    parser.add_argument('--test_tgt', default='', type=str,
                        help="test target file")
    parser.add_argument('--src_filter', type=int, default=0,
                        help="Maximum source sequence length")
    parser.add_argument('--tgt_filter', type=int, default=0,
                        help="Maximum target sequence length")
    parser.add_argument('--src_trun', type=int, default=0,
                        help="Truncate source sequence length")
    parser.add_argument('--tgt_trun', type=int, default=0,
                        help="Truncate target sequence length")
    parser.add_argument('--lower', action='store_true',
                        help='lower the case')
    return parser.parse_args()
