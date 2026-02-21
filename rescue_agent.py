import asyncio
from environment import DisasterEnvironment

class RescueAgent:

    def __init__(self):
        self.environment = DisasterEnvironment()
        self.current_state = "IDLE"

    async def run(self):
        print("RescueAgent started.")

        while True:
            if self.current_state == "IDLE":
                print("\n[STATE] IDLE")
                await asyncio.sleep(1)
                self.current_state = "ASSESS"

            elif self.current_state == "ASSESS":
                event = self.environment.generate_event()
                print(f"[STATE] ASSESS - Severity: {event['severity']}")
                await asyncio.sleep(1)

                if event["severity"] >= 6:
                    self.current_state = "RESCUE"
                else:
                    self.current_state = "STANDBY"

            elif self.current_state == "RESCUE":
                print("[STATE] RESCUE - Performing rescue...")
                await asyncio.sleep(2)
                print("Rescue completed.")
                self.current_state = "IDLE"

            elif self.current_state == "STANDBY":
                print("[STATE] STANDBY - Monitoring situation.")
                await asyncio.sleep(2)
                self.current_state = "IDLE"