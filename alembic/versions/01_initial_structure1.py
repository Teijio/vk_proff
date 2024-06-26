"""Initial structure1

Revision ID: 01
Revises: 
Create Date: 2024-05-03 16:04:32.253441

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy_utils

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "01"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("login", sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
        sa.Column("password", sqlalchemy_utils.types.encrypted.encrypted_type.StringEncryptedType(), nullable=False),
        sa.Column("project_id", sa.UUID(), nullable=False),
        sa.Column("env", sa.String(), nullable=False),
        sa.Column("domain", sa.String(), nullable=False),
        sa.Column("locktime", sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_index(op.f("ix_user_login"), "user", ["login"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_login"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
