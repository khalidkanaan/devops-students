# Running webapp Instructions:

## For MAC OS/Linux:
- Install pip3
    ```sh
    sudo apt-get install python3-pip
    ```

- Install virtualenv
    ```sh
    pip3 install virtualenv
    ```

- Change Directory
    ```sh
    cd <project-path>/devops-students/webapp
    ```

- Create Virtual Env
    ```sh
    virtualenv -p python3 venv
    ```

- Activate Virtual Env
    ```sh
    source venv/bin/activate
    ```

- Install Project Requirements
    ```sh
    pip3 install -r requirements.txt
    ```

## For Windows 10/11:
- Install pip
    Automatically comes with Python if downloading from [python.org](https://www.python.org/).

- Install virtualenv
    ```sh
    pip install virtualenv
    ```

- Change Directory
    ```sh
    cd <project-path/devops-students/webapp>
    ```

- Create Virtual Env
    ```sh
    virtualenv -p python3 venv
    ```

- Activate Virtual Env
    ```sh
    source venv/Scripts/activate
    ```

- Install Project Requirements
    ```sh
    pip install -r requirements.txt
    ```

- Deactivating Virtual Env
    ```sh
    deactivate
    ```