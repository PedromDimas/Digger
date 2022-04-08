import os
import configparser
from multiprocessing import Process


def tunnel(config, parsed):
    print('tunneling')
    query = 'ssh -N -i ' + config['DEFAULT']['DefaultKeyLocation'] + ' ' + config['DEFAULT']['JumpUser'] + '@' + config['DEFAULT']['JumpServer'] + ' -L ' + parsed['lp'] + ':' + config[parsed['env']][parsed['addr']] + ':' + config[parsed['env']][parsed['svc']]
    print(query)
    os.system(query)

def parse_input(input):
    ret = dict()
    splited = input.split(' ')
    for pair in splited:
        k, v = pair.split('=')
        ret[k] = v
    
    return ret

def help():
    print('Syntax:\n connect lp=8080 env=DEVOPS addr=ServerAddress svc=Jenkins \n lp=<localport>\n env=<env inside cfg []>\n addr=<name of addr inside cfg>\n svc=<name portinside cfg>\n')
    print('To quit type exit')
    

if __name__ == '__main__':

    config = configparser.ConfigParser()

    print('Welcome to Digger, lets make tunnels!')
    print('Please edit the digger.cfg file')
    

    config.read('digger.cfg')

    running = True
    tunnels = []
    
    help()
    while running:
        inn = input('> ')
        if inn == "exit":
            running = False
            for tunnel in tunnels:
                tunnel.kill()
                tunnel.join()
        else:
            if inn == "help":
                help()
            if inn.split(' ')[0] == "connect":
                parsed = parse_input(inn.split(' ',1)[1])
                print(parsed)
                p = Process(target=tunnel, args=[config,parsed])
                p.start()
                tunnels.append(p)
            else:
                print('Invalid Command')