import argparse
import torch


def model_config(parser):
    parser.add_argument('--word_dim', default=300, type=int)
    parser.add_argument('--d_e', default=300, type=int)
    parser.add_argument('--num_heads', default=5, type=int)
    parser.add_argument('--d_ff', default=300 * 4, type=int)

    parser.add_argument('--dist_mask', default=False, action='store_true')
    parser.add_argument('--alpha', default=1.5, type=float)
    parser.add_argument('--no_seg_emb', dest='seg_emb', action='store_false')
    parser.add_argument('--seg_emb_share', default=False, action='store_true')
    parser.add_argument('--pos_emb', default=False, action='store_true')

    parser.add_argument('--elmo_num', type=int, default=2)
    parser.add_argument('--no_elmo_feed_forward', dest='elmo_feed_forward', action='store_false')
    parser.add_argument('--elmo_dim', type=int, default=1024)

    parser.add_argument('--ss_emb', default=False, action='store_true')
    parser.add_argument('--ss_emb_tune', default=False, action='store_true')

    parser.add_argument('--no_lstm_bidirection', dest='lstm_bidirection', action='store_false')
    parser.add_argument('--lstm_num_layers', type=int, default=1)
    parser.add_argument('--lstm_hidden_dim', type=int, default=150)

    parser.add_argument('--fusion', default=False, action='store_true')
    parser.add_argument('--no_share_encoder', dest='share_encoder', action='store_false')

    return parser


def data_config(parser):
    parser.add_argument('--train_data_path', default='data/train.txt')
    parser.add_argument('--valid_data_path', default='data/dev.txt')
    parser.add_argument('--elmo_option_path', default='data/elmo/elmo_options.json')
    parser.add_argument('--elmo_weight_path', default='data/elmo/elmo_weights.hdf5')
    parser.add_argument('--ss_vector_path', default='data/sswe/sswe.pt')

    return parser


def train_config(parser):
    parser.add_argument('--device',
                        default='cuda:0' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--tune_embeddings', default=False, action='store_true')
    parser.add_argument('--dropout', type=float, default=0.1)
    parser.add_argument('--batch_size', type=int, default=64)
    parser.add_argument('--learning_rate', type=float, default=0.001)
    parser.add_argument('--lr_gamma', type=float, default=1.0)
    parser.add_argument('--weight_decay', type=float, default=0)
    parser.add_argument('--max_epoch', type=int, default=10)
    parser.add_argument('--print_every', type=int, default=100)
    parser.add_argument('--validate_every', type=int, default=100)
    parser.add_argument('--no_fl_loss', dest='fl_loss', action='store_false')
    parser.add_argument('--fl_gamma', type=float, default=0.0)
    parser.add_argument('--fl_alpha', type=float, default=None)
    parser.add_argument('--mfe_loss', default=False, action='store_true')

    return parser


def set_args():
    parser = argparse.ArgumentParser()
    parser = data_config(parser)
    parser = model_config(parser)
    parser = train_config(parser)
    args = parser.parse_args()
    return args
