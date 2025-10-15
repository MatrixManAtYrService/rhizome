#!/usr/bin/env python3
"""
Script to check the actual enum values in the reseller_permissions.type column.
Run this on the VPN to see what values exist in the database.
"""

import pymysql

# Database connection details (dev1)
HOST = "dev1-db01.dev.pdx10.clover.network"
PORT = 3306
USER = "remotereadonly"
PASSWORD = "test123"
DATABASE = "meta"

def main():
    print(f"Connecting to {HOST}:{PORT}/{DATABASE}...")

    connection = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
    )

    try:
        with connection.cursor() as cursor:
            # Get distinct type values from reseller_permissions
            query = "SELECT DISTINCT type FROM reseller_permissions ORDER BY type"
            cursor.execute(query)
            results = cursor.fetchall()

            print("\nDistinct values in reseller_permissions.type column:")
            print("=" * 60)
            for row in results:
                type_value = row[0]
                # Show the value with quotes and repr to see any hidden characters
                print(f"  '{type_value}' (repr: {repr(type_value)})")

            print("\n" + "=" * 60)
            print(f"Total distinct values: {len(results)}")

            # Also check the column definition to see the ENUM definition
            print("\nColumn definition:")
            print("=" * 60)
            cursor.execute("SHOW COLUMNS FROM reseller_permissions LIKE 'type'")
            column_info = cursor.fetchone()
            if column_info:
                print(f"  Type definition: {column_info[1]}")

    finally:
        connection.close()
        print("\nConnection closed.")

if __name__ == "__main__":
    main()
