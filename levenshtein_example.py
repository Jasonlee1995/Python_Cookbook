'''
https://github.com/maxbachmann/Levenshtein
pip install levenshtein

'''

import Levenshtein


def error_detail(src, dest):
    error_info = {'deletion'     : [],
                  'substitution' : [],
                  'insertion'    : []}
    
    for operation, src_idx, dest_idx in Levenshtein.editops(src, dest):
        if   operation == 'delete':
            # have to delete -> insertion error
            error_info['insertion'].append((src_idx, dest_idx))
        elif operation == 'replace':
            error_info['substitution'].append((src_idx, dest_idx))
        elif operation == 'insert':
            # have to insert -> deletion error
            error_info['deletion'].append((src_idx, dest_idx))

    return error_info

def CER(hyp, ref, return_detail=False):
    error_info = error_detail(hyp, ref)

    errors = sum(len(error_info[error_type]) for error_type in error_info)
    length = len(ref)

    if return_detail: return (errors, length, error_info)
    else:             return (errors, length, None)

def WER(hyp, ref, return_detail=False):
    hyp, ref = hyp.split(), ref.split()
    error_info = error_detail(hyp, ref)

    errors = sum(len(error_info[error_type]) for error_type in error_info)
    length = len(ref)

    if return_detail: return (errors, length, error_info)
    else:             return (errors, length, None)


if __name__ == '__main__':
    hyp = "Hmm... I think I'll be arrived at 3pm."
    ref = "I think I will arrive at maybe 3pm."

    cer_error, cer_length, _ = CER(hyp, ref, return_detail=False)
    wer_error, wer_length, _ = WER(hyp, ref, return_detail=False)

    print('CER : {:.4f}'.format(cer_error / cer_length))
    print('WER : {:.4f}'.format(wer_error / wer_length))