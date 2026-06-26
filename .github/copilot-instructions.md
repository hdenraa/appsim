# Copilot instructions for `appsim`

- Primary entry point: `appsim.py`. It sets up the `AppState` state machine, creates `asyncio.Queue` objects for websocket inbound/outbound flow, and starts the `Gui` and `WebsocketServer`.
- `connection.py` is the websocket layer. It maps `deviceId` to websocket connections, handles `connected` handshake payloads, and puts non-initial messages onto `ws_inbound_queue`.
- `interpreter.py` is the exercise engine. `Interpreter.run_exercise(...)` consumes `ws_inbound_queue`, drives task execution, and pushes display events to `heads_up_queue`.
- `gui.py` contains the UI and user flow. It uses `pygame` + `pygame_gui`, listens for button events, transitions `AppState` with `state.send(...)`, and starts interpreter tasks with `asyncio.create_task(...)`.
- `exer_elem_rec.py` loads exercise metadata from `json/exercises_test.json` and exposes runtime exercise definitions via `get_runtime_dict()`.

## Important patterns

- Communication is mostly queue-based: `ws_inbound_queue`, `ws_outbound_queue`, and `heads_up_queue` are the main async channels.
- State changes are handled through `AppState` events like `evt_exer_cycle`, `evt_cancle_exer_cycle`, and `evt_popup_cancle`.
- `Gui.start_exercise()` builds `app_parameter_values` and `elem_parameter_values` from UI fields, then launches interpreter work asynchronously.
- `Interpreter.set_task()` creates outbound messages with a `payload.task == "set"` and places them on `ws_outbound_queue`.
- `WebsocketServer.outbound_loop()` continuously drains `ws_outbound_queue` and sends messages to the appropriate connected client.

## Run / debug workflow

- Run the app from the repo root: `python appsim.py`
- Simulate a device client with `python test_client.py <client-number>` against `ws://localhost:8080`
- The GUI loads exercise definitions from `json/exercises_test.json`.

## Helpful file references

- `appsim.py` — orchestration and app startup
- `connection.py` — websocket handling and device registration
- `interpreter.py` — exercise task execution and result handling
- `gui.py` — UI event handling, popups, and drawing logic
- `exer_elem_rec.py` — exercise metadata and runtime element state
- `test_client.py` — sample websocket client for manual testing

## Notes for code changes

- Avoid introducing new cross-thread communication; follow the existing `asyncio.Queue` pattern.
- Use `state.send(...)` for UI/state transitions rather than changing the state directly.
- Exercise definitions are data-driven; modify or extend `json/exercises_test.json` instead of hardcoding new tasks.
