def do_connect(forCheck=True):
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ssid', 'passwd')
        import time
        while not sta_if.isconnected():
            time.sleep(1)
            print('.',)
    if forCheck:
        print('')
        print('network config:', sta_if.ifconfig())