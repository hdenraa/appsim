# Motorskills Control Center

## Module Overview

This project consists of several modules that work together to create a graphical user interface (GUI) application with WebSocket communication and Azure integration. Below is an overview of the main modules:

- `appsim.py`: Initializes and runs the main application, setting up the GUI, WebSocket server, and other components.
- `connection.py`: Manages the WebSocket server for the application.
- `exer_elem_rec.py`: Manages exercise elements.
- `gui.py`: Manages the graphical user interface of the application.
- `headsUp.py`: Contains the `HeadsUp` class for creating and managing heads-up display elements.
- `hockeyrink.py`: Contains the `HockeyRink` class for managing the hockey rink elements.
- `interpreter.py`: Handles communication between the WebSocket server and the GUI.
- `json_display.py`: Manages the display of JSON data.
- `json_pandas.py`: Manages the conversion of JSON data to pandas DataFrames.
- `test_client.py`: Contains tests for the application.
- `test random.py`: Contains random tests for the application.

## Module Communication

The modules in this project communicate with each other through various mechanisms, including direct method calls, queues, and WebSocket messages. Below is a description of how the different modules interact:

- **`appsim.py`**:
  - Initializes the main components and sets up the communication channels.
  - Uses `asyncio.Queue` for communication between the WebSocket server, interpreter, and GUI.
- Calls methods from `exer_elem_rec.py`, `connection.py`, `interpreter.py`, and `gui.py` to initialize and manage the application state.
- **`connection.py`**:
  - Manages the WebSocket server and handles inbound and outbound messages.
  - Uses `asyncio.Queue` to receive messages from and send messages to the `interpreter.py`.
  - Communicates with `exer_elem_rec.py` to update exercise elements based on WebSocket messages.

- **`exer_elem_rec.py`**:
  - Manages exercise elements and their states.
  - Called by `appsim.py` to load exercise data.
  - Interacts with `connection.py` to update elements based on WebSocket messages.
  - Provides exercise element data to `interpreter.py` and `gui.py`.

- **`gui.py`**:
  - Manages the graphical user interface of the application.
  - Receives updates from `interpreter.py` through `asyncio.Queue`.
  - Calls methods from `exer_elem_rec.py` to display exercise elements.

- **`interpreter.py`**:
  - Handles the logic for running exercises and interpreting WebSocket messages.
  - Uses `asyncio.Queue` to communicate with `connection.py` and `gui.py`.
  - Calls methods from `exer_elem_rec.py` to manage exercise elements.
  - Interacts with `azure_connection.py` to upload exercise results.

- **`headsUp.py`**:
  - Manages heads-up display elements.
  - Called by `gui.py` to display heads-up information.

- **`hockeyrink.py`**:
  - Manages hockey rink elements.
  - Called by `gui.py` to display hockey rink information.

- **`json_display.py`**:
  - Manages the display of JSON data.
  - Called by various modules to display JSON data in the GUI.

- **`json_pandas.py`**:
  - Manages the conversion of JSON data to pandas DataFrames.
  - Called by various modules to process JSON data.

- **`test_client.py`** and **`test random.py`**:
  - Contain tests for the application.
  - Use mock data and methods to test the functionality of the other modules.

[`appsim`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A83%2C%22character%22%3A47%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") catalog:
[`appsim`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A83%2C%22character%22%3A47%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") catalog:



### Description
This module initializes and runs the main application, setting up the GUI, WebSocket server, and other components.

### Classes

#### [`AppState`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A15%2C%22character%22%3A6%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
A state machine class that manages the different states of the application.

- **States:**
  - [`start`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A16%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A416%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Initial state.
  - [`gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A539%2C%22character%22%3A19%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): GUI state.
  - [`popup_params`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A4%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for popup parameters.
  - [`popup_elem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A19%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A60%2C%22character%22%3A33%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for popup elements.
  - [`exer_countdown`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A20%2C%22character%22%3A4%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for exercise countdown.
  - [`exer_running`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A21%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A146%2C%22character%22%3A22%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for exercise running.
  - [`exer_result`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A4%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for exercise result.
  - [`exer_over`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A23%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A519%2C%22character%22%3A30%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): State for exercise over.
  - [`end`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A494%2C%22character%22%3A33%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A86%2C%22character%22%3A7%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Final state.

- **Events:**
  - [`evt_ready`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A28%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A486%2C%22character%22%3A25%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Transition from [`start`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A16%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A416%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") to [`gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A539%2C%22character%22%3A19%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition").
  - [`evt_exer_cycle`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A29%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A69%2C%22character%22%3A33%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Transition through exercise cycle states.
  - [`evt_cancle_exer_cycle`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A38%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A54%2C%22character%22%3A33%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Cancel exercise cycle and return to [`gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A539%2C%22character%22%3A19%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition").
  - [`evt_show_elem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A47%2C%22character%22%3A4%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Show elements popup.
  - [`evt_popup_cancle`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A49%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A75%2C%22character%22%3A33%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Cancel popup and return to [`gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A539%2C%22character%22%3A19%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition").
  - [`evt_end`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A55%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A57%2C%22character%22%3A33%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Transition to [`end`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A494%2C%22character%22%3A33%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A86%2C%22character%22%3A7%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition").

- **Methods:**
  - [`before_evt_exer_cycle`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A60%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Logs event transitions for exercise cycle.
  - [`before_evt_cancle_exer_cycle`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A64%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Logs event transitions for canceling exercise cycle.
  - [`set_current_exercise`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A68%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A89%2C%22character%22%3A27%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Sets the current exercise.
  - [`on_enter_gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A71%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Logs entry into the [`gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A539%2C%22character%22%3A19%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") state.

### Functions

#### [`main(host, port, file)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A77%2C%22character%22%3A10%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
The main function that initializes and starts the application.

- **Parameters:**
  - [`host`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A77%2C%22character%22%3A15%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): The host address for the WebSocket server.
  - [`port`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A77%2C%22character%22%3A20%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A38%2C%22character%22%3A25%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A92%2C%22character%22%3A32%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): The port number for the WebSocket server.
  - [`file`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A77%2C%22character%22%3A25%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A132%2C%22character%22%3A13%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A34%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A85%2C%22character%22%3A61%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): The file path for exercise data.

- **Description:**
  - Initializes queues for WebSocket communication and heads-up display.
  - Sets up logging.
  - Initializes application state, Azure connection, exercise elements, WebSocket server, interpreter, and GUI.
  - Starts the GUI and WebSocket server.
  - Waits for tasks to complete and closes handlers.

### Example Usage

```python
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main("192.168.8.123", 8080, "file"))
```

## 

interpreter.py



### Description
This module contains the [`Interpreter`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A24%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") class, which handles communication between the WebSocket server and the GUI.

### Classes

#### [`Interpreter`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A24%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
Handles communication between the WebSocket server and the GUI.

- **Methods:**
  - `wait_for_answer`: Waits for an answer from the WebSocket server.

## 

gui.py



### Description
This module contains the [`Gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A16%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A11%2C%22character%22%3A6%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") class, which manages the graphical user interface of the application.

### Classes

#### [`Gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A16%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A11%2C%22character%22%3A6%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
Manages the graphical user interface of the application.

- **Methods:**
  - [`__init__`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A12%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Initializes the GUI with the interpreter, exercise elements, heads-up queue, logger, and application state.
  - [`handle_events`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A45%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Handles GUI events.
  - [`prepare_exercise`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A81%2C%22character%22%3A27%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Prepares the exercise based on the selected button.
  - [`start_exercise`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A72%2C%22character%22%3A21%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Starts the exercise.
  - [`draw`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A139%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws the GUI elements.
  - [`create_parameter_window`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A94%2C%22character%22%3A109%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Creates a window for exercise parameters.
  - [`draw_heads_up_elements`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A148%2C%22character%22%3A27%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws heads-up display elements.
  - [`init_heads_up_elements`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A102%2C%22character%22%3A31%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Initializes heads-up display elements.
  - [`draw_element`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A264%2C%22character%22%3A27%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws a specific element.
  - [`reset_scoreboard`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A85%2C%22character%22%3A13%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Resets the scoreboard.
  - [`draw_scoreboard`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A153%2C%22character%22%3A17%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws the scoreboard.
  - [`draw_countdown`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A352%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws the countdown timer.
  - [`create_element_window`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A62%2C%22character%22%3A89%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Creates a window for displaying elements.
  - [`update_exer_list`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A142%2C%22character%22%3A13%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Updates the exercise list.
  - [`draw_control_gui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A415%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Draws the control GUI.
  - [`start`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A16%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A416%2C%22character%22%3A8%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Starts the GUI.

## connection.py



### Description
This module contains the [`WebsocketServer`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A23%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") class, which manages the WebSocket server for the application.

### Classes

#### [`WebsocketServer`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A23%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
Manages the WebSocket server for the application.

- **Methods:**
  - [`start_server`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A106%2C%22character%22%3A20%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Starts the WebSocket server.

## exer_elem_rec.py

### Description
This module contains the [`ExerElem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A26%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition") class, which manages exercise elements.

### Classes

#### [`ExerElem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A26%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition")
Manages exercise elements.

- **Methods:**
  - [`load_exer`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A94%2C%22character%22%3A14%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Loads exercise data from a file.
  - [`load_elem`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fappsim.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A95%2C%22character%22%3A15%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Loads element data from a file.
  - [`get_runtime_dict`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flarshostruppedersen%2Fmotorskills%2Fappsim%2Fgui.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A96%2C%22character%22%3A34%7D%7D%5D%2C%2228d9993b-dfd1-4d44-8f82-f65a98863537%22%5D "Go to definition"): Returns the runtime dictionary of exercise elements.
