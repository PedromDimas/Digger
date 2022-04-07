from cProfile import run
import os
import configparser
from multiprocessing import Process


def tunnel(config, parsed):
    print('tunneling')
    query = 'ssh -N -i ' + config['DEFAULT']['DefaultKeyLocation'] + ' ' + config['DEFAULT']['JumpUser'] + '@' + config['DEFAULT']['JumpServer'] + ' -L ' + parsed['lp'] + ':' + config[parsed['env']][parsed['addr']] + ':' + config[parsed['env']][parsed['port']]
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
    print('Syntax:\n lp=8080 env=DEVOPS addr=ServerAddress port=Jenkins \n lp=<localport>\n env=<env inside cfg []>\n addr=<name of addr inside cfg>\n port=<name portinside cfg>\n')
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
            else:
                parsed = parse_input(inn)
                print(parsed)
                p = Process(target=tunnel, args=[config,parsed])
                p.start()
                tunnels.append(p)