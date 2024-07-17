def transform_url_proxy_to_java(url):
    protocol = url.split('://')[0]
    domain = url.split('://')[1].split(':')[0]
    port = url.split(':')[-1]
    return f'-D{protocol}.proxyHost={domain} -D{protocol}.proxyPort={port}'

tranform_funcs = {
    'upper': lambda x: x.upper(),
    'java_proxy': transform_url_proxy_to_java
}
