# Digger

## Usage

### Config file
- The config file must be called `digger.cfg`, here is an example
    ```cfg
    [DEFAULT]
    JumpServer = xxxx.xxxx.xxxx.xxxx
    JumpUser = opc
    DefaultKeyLocation = C:\Users\dimas\Desktop\ssh-key-2021-12-02.key

    [DEVOPS]
    ServerAddress = 10.3.2.10
    Jenkins = 8080
    Nexus = 8081
    Sonar = 9000
    Grafana = 3000

    [DEV]
    

    [TST]
    

    [PRD]
    
    ```
- You can specify multiple servers and service ports per enviroment and can also specify more 