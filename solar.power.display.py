#written by Carlos Nikolaus Krämer aka carloscomputer https://github.com/carloscomputer
import asyncio
from APsystemsEZ1 import APsystemsEZ1M

IP = ""

async def main():
    dev = APsystemsEZ1M(IP)
    out = await dev.get_output_data()

    east = round(out.p1, 4)
    south = round(out.p2, 4)
    total = round(out.p1 + out.p2, 4)
    east_d = round(out.e1, 4)
    south_d = round(out.e2, 4)
    total_d = round(out.e1 + out.e2, 4)
    east_lt = round(out.te1, 4)
    south_lt = round(out.te2, 4)
    total_lt = round(out.te1 + out.te2,4)
    
    print("☀️ ACTUAL POWER☀️ ")
    print("east:", out.p1, "W")
    print("south:", out.p2, "W")
    print("total", total, "W⚡️")
    print("🌳 DAILY POWER 🌳")
    print("east:", east_d, "kWh")
    print("south:", south_d, "kWh")
    print("total:", total_d, "kWh⚡️")
    print("🌳☀️ LIFETIME POWER☀️🌳")
    print("east:", east_lt, "kWh")
    print("south:", south_lt, "kWh")
    print("total:", total_lt, "kWh⚡️")

asyncio.run(main())

