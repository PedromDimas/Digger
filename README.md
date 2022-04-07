# Digger

## Prep:
- Install the following packages if needed:
    ```sh
    pip install configparser
    pip install multiprocessing
    ```

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

### App
- This is a simple cli app with only one command.
- After configuring the `digger.cfg` file, run the app with 
    ```shell
    python main.py
     ```
- Inside the app there are only 2 commands
    - `exit` which exits the application and closes all open connections
    - `connect` which connects a new tunnel
        - Args of connect:
        1. `lp` : local port on machine to map
        2. `env`: the enviroment defined in the cfg
        3. `addr`: the name of the addres specified in the cfg
        4. `svc`: the name of the service specified in the cfg
        - Example:
        ```
        connect lp=8080 env=DEVOPS addr=ServerAddress svc=Jenkins
        ```
