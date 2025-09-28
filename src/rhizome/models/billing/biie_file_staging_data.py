"""
SQLModel definition for the biie_file_staging_data table.

This module provides the SQLModel class for the biie_file_staging_data table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class BiieFileStagingData(RhizomeModel, table=False):
    """
    SQLModel for the `biie_file_staging_data` table.

    This model represents biie_file_staging_data records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    biie_file_instance_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    record_num: int = Field(description="record_num")
    record_status: str | None = Field(default=None, description="record_status")
    reason_code: str | None = Field(default=None, description="reason_code")
    reason_detail: str | None = Field(default=None, description="reason_detail")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    raw_record: str | None = Field(default=None, description="raw_record")
    field1: str | None = Field(default=None, max_length=100, description="field1")
    field2: str | None = Field(default=None, max_length=100, description="field2")
    field3: str | None = Field(default=None, max_length=100, description="field3")
    field4: str | None = Field(default=None, max_length=100, description="field4")
    field5: str | None = Field(default=None, max_length=100, description="field5")
    field6: str | None = Field(default=None, max_length=100, description="field6")
    field7: str | None = Field(default=None, max_length=100, description="field7")
    field8: str | None = Field(default=None, max_length=100, description="field8")
    field9: str | None = Field(default=None, max_length=100, description="field9")
    field10: str | None = Field(default=None, max_length=100, description="field10")
    field11: str | None = Field(default=None, max_length=100, description="field11")
    field12: str | None = Field(default=None, max_length=100, description="field12")
    field13: str | None = Field(default=None, max_length=100, description="field13")
    field14: str | None = Field(default=None, max_length=100, description="field14")
    field15: str | None = Field(default=None, max_length=100, description="field15")
    field16: str | None = Field(default=None, max_length=100, description="field16")
    field17: str | None = Field(default=None, max_length=100, description="field17")
    field18: str | None = Field(default=None, max_length=100, description="field18")
    field19: str | None = Field(default=None, max_length=100, description="field19")
    field20: str | None = Field(default=None, max_length=100, description="field20")
    key1: str | None = Field(default=None, max_length=100, description="key1")
    key2: str | None = Field(default=None, max_length=100, description="key2")

    def sanitize(self) -> BiieFileStagingData:
        """Return a sanitized copy of this BiieFileStagingData instance."""
        return BiieFileStagingData(
            id=self.id,
            biie_file_instance_id=self.biie_file_instance_id,
            record_num=self.record_num,
            record_status=self.record_status,
            reason_code=self.reason_code,
            reason_detail=self.reason_detail,
            created_time=self.created_time,
            modified_time=self.modified_time,
            raw_record=self.raw_record,
            field1=self.field1,
            field2=self.field2,
            field3=self.field3,
            field4=self.field4,
            field5=self.field5,
            field6=self.field6,
            field7=self.field7,
            field8=self.field8,
            field9=self.field9,
            field10=self.field10,
            field11=self.field11,
            field12=self.field12,
            field13=self.field13,
            field14=self.field14,
            field15=self.field15,
            field16=self.field16,
            field17=self.field17,
            field18=self.field18,
            field19=self.field19,
            field20=self.field20,
            key1=self.key1,
            key2=self.key2,
        )
