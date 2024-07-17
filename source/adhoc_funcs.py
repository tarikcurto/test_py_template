def parse_noproxy(value):
    return ','.join(value)

adhoc_funcs = {
    'noProxy': parse_noproxy 
}
