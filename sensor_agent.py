from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import asyncio
from environment import DisasterEnvironment

class SensorAgent(Agent):

    class MonitorBehaviour(CyclicBehaviour):
        async def run(self):
            event = self.environment.generate_event()

            msg = Message(
                to="rescueagent@localhost",
                body=str(event)
            )
            msg.set_metadata("performative", "inform")

            await self.send(msg)
            print(f"[SensorAgent] Sent event: {event}")

            await asyncio.sleep(5)

        async def on_start(self):
            self.environment = DisasterEnvironment()

    async def setup(self):
        print("SensorAgent started.")
        self.add_behaviour(self.MonitorBehaviour())