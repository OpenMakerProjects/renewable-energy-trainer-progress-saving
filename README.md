# Renewable Energy Trainer Progress Saving

Build a education prototype that uses buttons, current sensor to save completed lessons locally. Include setup instructions, a circuit diagram, tested firmware, and sample output.

## Project details

| Field | Value |
| --- | --- |
| Roadmap ID | 1459 |
| Category | Education |
| Platform | micro:bit |
| Difficulty | Advanced |
| Estimated build time | 44 hours |
| Connectivity | Wi-Fi |
| Core components | buttons, current sensor |
| Control mode | interactive monitor |

## Repository layout

- `firmware/main.py`: runnable firmware or application
- `docs/wiring.md`: suggested low-voltage wiring plan
- `docs/architecture.md`: system data flow
- `docs/test-plan.md`: repeatable verification steps
- `sample-data/example.json`: example telemetry record
- `tools/validate.py`: dependency-free repository validation

## Quick start

1. Open `firmware/main.py` in the micro:bit Python editor.
2. Flash it to the board.
3. Connect a 0–3.3 V input to pin 0 and a protected output to pin 1.

## Expected behavior

Progress Saving demonstration with repeatable test steps. The default implementation supports simulated or generic analog inputs so the control path can be exercised before hardware-specific drivers are added.

## Hardware adaptation

The included code is a safe reference implementation. Update pin assignments and sensor conversions from the exact component datasheets, then repeat the test plan before connecting actuators.

## License

MIT
