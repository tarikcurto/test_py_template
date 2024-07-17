def parse_noproxy(value, ctx):
    local_proxy = ctx.get('local_value') or []
    global_proxy = ctx.get('global_value') or []
    proxy = local_proxy + global_proxy
    return ','.join(proxy)

adhoc_funcs = {
    'noProxy': parse_noproxy 
}
