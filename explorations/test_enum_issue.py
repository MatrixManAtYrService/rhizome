#!/usr/bin/env python3
"""Test script to isolate the enum issue."""

from rhizome.models.meta.reseller_permissions_v1 import ResellerPermissionsType, ResellerPermissionsV1
from sqlmodel import Session, create_engine, select

# Connection string
connection_string = "mysql+pymysql://remotereadonly:test123@dev1-db01.dev.pdx10.clover.network:3306/meta"

print("Enum values in Python:")
for name, member in ResellerPermissionsType.__members__.items():
    print(f"  {name}: {repr(member.value)}")

print("\nTrying to query a row with type='Super'...")
engine = create_engine(connection_string)

try:
    with Session(engine) as session:
        result = session.exec(
            select(ResellerPermissionsV1)
            .where(ResellerPermissionsV1.reseller_id == 15)
            .where(ResellerPermissionsV1.name == "Super Administrator")
        ).first()

        if result:
            print(f"✅ Successfully loaded row!")
            print(f"   type: {result.type}")
            print(f"   type value: {result.type.value}")
        else:
            print("❌ No row found")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
